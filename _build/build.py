# -*- coding: utf-8 -*-
"""Gerador estático do site Ribeiro & Flores Advocacia.

Uso:
    python3 _build/build.py            # gera as páginas
    python3 _build/images.py           # (re)gera as imagens otimizadas, quando trocar fotos

As páginas são escritas na raiz do repositório com URLs amigáveis
(ex.: /areas/direito-trabalhista/index.html), prontas para o GitHub Pages.
"""
import html
import re
import shutil
import time
from datetime import date
from pathlib import Path
from urllib.parse import urlparse

from jinja2 import Environment, FileSystemLoader, select_autoescape

import content as C
import legal as L

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
VERSION = time.strftime("%Y%m%d%H%M")
MONTHS = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto",
          "setembro", "outubro", "novembro", "dezembro"]
SITE = C.SITE
BASE_PATH = urlparse(SITE["url"]).path.rstrip("/")  # "/JR-Ribeiro-Flores" ou ""

env = Environment(loader=FileSystemLoader(str(HERE / "templates")), autoescape=select_autoescape(["html"]),
                  trim_blocks=True, lstrip_blocks=True)

_state = {"depth": 0, "absolute": False}


def url(path):
    """Converte um caminho do site ("/areas/") em link relativo à página atual."""
    if path.startswith(("http", "mailto:", "tel:", "#")):
        return path
    clean = path.lstrip("/")
    if _state["absolute"]:
        return f"{BASE_PATH}/{clean}"
    prefix = "../" * _state["depth"]
    return (prefix + clean) or "./"


def asset(p):
    return url("/assets/" + p)


env.globals.update(url=url, asset=asset, site=SITE, wa=C.wa, wa_default=C.wa(), version=VERSION,
                   areas=C.AREAS, area_by_key=C.AREA_BY_KEY, partners=C.PARTNERS, categories=C.CATEGORIES,
                   wa_sent="Olá! Acabei de enviar uma mensagem pelo site da Ribeiro & Flores Advocacia.")

NAV = [
    {"key": "escritorio", "label": "Escritório", "href": "/escritorio/"},
    {"key": "areas", "label": "Áreas de atuação", "href": "/areas/",
     "children": [{"label": a["name"], "href": f"/areas/{a['slug']}/", "icon": a["icon"]} for a in C.AREAS]},
    {"key": "artigos", "label": "Artigos", "href": "/artigos/"},
    {"key": "socios", "label": "Sócios", "href": "/socios/"},
    {"key": "contato", "label": "Contato", "href": "/contato/"},
]
env.globals["nav"] = NAV

written = []
sitemap = []


def fmt_date(iso):
    d = date.fromisoformat(iso)
    return f"{d.day} de {MONTHS[d.month - 1]} de {d.year}"


# ---------------------------------------------------------------- structured data
ORG_ID = SITE["url"] + "/#escritorio"


def org_ld():
    ld = {
        "@context": "https://schema.org",
        "@type": "LegalService",
        "@id": ORG_ID,
        "name": SITE["name"],
        "url": SITE["url"] + "/",
        "logo": SITE["url"] + "/assets/img/opt/icon-512.png",
        "image": SITE["url"] + "/assets/img/opt/og-default.jpg",
        "description": "Escritório de advocacia com atuação Trabalhista, Previdenciária, Cível, do Consumidor e "
                       "Empresarial. Atendimento online em todo o Brasil.",
        "telephone": SITE["phone_e164"],
        "email": SITE["email"],
        "priceRange": "Consulte",
        "areaServed": {"@type": "Country", "name": "Brasil"},
        "address": {"@type": "PostalAddress", "addressLocality": SITE["city"], "addressRegion": SITE["region"],
                    "addressCountry": "BR"},
        "openingHoursSpecification": [{"@type": "OpeningHoursSpecification",
                                       "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
                                       "opens": "08:00", "closes": "19:00"}],
        "knowsAbout": [a["name"] for a in C.AREAS],
        "founder": [{"@type": "Person", "name": p["name"]} for p in C.PARTNERS],
        "contactPoint": {"@type": "ContactPoint", "telephone": SITE["phone_e164"], "contactType": "customer service",
                         "availableLanguage": "Portuguese", "areaServed": "BR"},
    }
    same = [SITE[k] for k in ("instagram", "linkedin", "facebook") if SITE.get(k)]
    if same:
        ld["sameAs"] = same
    return ld


def breadcrumb_ld(items):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList",
            "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n,
                                 "item": SITE["url"] + p} for i, (n, p) in enumerate(items)]}


def faq_ld(faq):
    return {"@context": "https://schema.org", "@type": "FAQPage",
            "mainEntity": [{"@type": "Question", "name": q,
                            "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faq]}


# ---------------------------------------------------------------- render
def render(tpl, out_path, page, priority="0.7", changefreq="monthly", in_sitemap=True, absolute=False, **ctx):
    out_path = out_path.strip("/")
    is_index = out_path.endswith("index.html")
    depth = out_path.count("/")
    _state["depth"], _state["absolute"] = depth, absolute
    public = "/" + (out_path[: -len("index.html")] if is_index else out_path)
    page.setdefault("canonical", SITE["url"] + public)
    page.setdefault("jsonld", [])
    html_out = env.get_template(tpl).render(page=page, **ctx)
    html_out = re.sub(r"\n\s*\n+", "\n", html_out)
    dest = ROOT / out_path
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(html_out, encoding="utf-8")
    written.append(out_path)
    if in_sitemap and not page.get("noindex"):
        sitemap.append((page["canonical"], priority, changefreq, page.get("lastmod")))
    _state["absolute"] = False


def word_count(h):
    return len(re.sub(r"<[^>]+>", " ", h).split())


def main():
    today = date.today().isoformat()
    # ------------- artigos (prepara)
    arts = []
    for a in C.ARTICLES:
        body = (HERE / "articles" / f"{a['body']}.html").read_text(encoding="utf-8").strip()
        a = dict(a)
        a["body"] = body
        a["minutes"] = max(3, round(word_count(body) / 200 + 0.5))
        a["date_display"] = fmt_date(a["date"])
        a["author"] = C.DEFAULT_AUTHOR
        a["keywords"] = re.sub(r"<[^>]+>", " ", " ".join(re.findall(r"<h2>(.*?)</h2>", body)))
        arts.append(a)
    arts.sort(key=lambda x: x["date"], reverse=True)
    by_slug = {a["slug"]: a for a in arts}
    env.globals["articles"] = arts

    # ------------- home
    render("home.html", "index.html", {
        "title": "Ribeiro & Flores Advocacia | Advogados Online em Todo o Brasil",
        "description": "Advocacia estratégica nas áreas Trabalhista, Previdenciária, Cível, do Consumidor e "
                       "Empresarial. Atendimento direto com os sócios, online em todo o Brasil.",
        "section": "home",
        "jsonld": [org_ld(), {"@context": "https://schema.org", "@type": "WebSite", "name": SITE["name"],
                              "url": SITE["url"] + "/", "inLanguage": "pt-BR", "publisher": {"@id": ORG_ID}}],
        "lastmod": today,
    }, priority="1.0", changefreq="weekly")

    # ------------- escritório
    render("escritorio.html", "escritorio/index.html", {
        "title": "O Escritório | Ribeiro & Flores Advocacia",
        "description": "Conheça a Ribeiro & Flores Advocacia: advocacia moderna, técnica e próxima, com atendimento "
                       "humanizado e online para pessoas e empresas de todo o Brasil.",
        "section": "escritorio",
        "jsonld": [breadcrumb_ld([("Início", "/"), ("O Escritório", "/escritorio/")])],
    }, priority="0.8")

    # ------------- sócios
    persons = []
    for p in C.PARTNERS:
        ld = {"@context": "https://schema.org", "@type": "Person", "name": p["name"],
              "jobTitle": p["role"].replace("·", "-"), "worksFor": {"@id": ORG_ID},
              "image": f"{SITE['url']}/assets/img/opt/{p['photo']}-720.webp",
              "url": f"{SITE['url']}/socios/#{p['key']}", "description": p["summary"],
              "knowsAbout": [C.AREA_BY_KEY[k]["name"] for k in p["areas"]]}
        if p.get("instagram"):
            ld["sameAs"] = [f"https://www.instagram.com/{p['instagram']}/"]
        persons.append(ld)
    render("socios.html", "socios/index.html", {
        "title": "Sócios | Josué Ribeiro e Renata Flores | Ribeiro & Flores Advocacia",
        "description": "Conheça Josué Ribeiro e Renata Flores, advogados sócios fundadores da Ribeiro & Flores "
                       "Advocacia: trajetória, áreas de atuação e forma de trabalho.",
        "section": "socios",
        "jsonld": [breadcrumb_ld([("Início", "/"), ("Sócios", "/socios/")])] + persons,
    }, priority="0.8")

    # ------------- áreas
    render("areas.html", "areas/index.html", {
        "title": "Áreas de Atuação | Ribeiro & Flores Advocacia",
        "description": "Direito Trabalhista, Previdenciário, do Consumidor, Civil e Empresarial. Conheça as áreas de "
                       "atuação da Ribeiro & Flores Advocacia, com atendimento online em todo o Brasil.",
        "section": "areas",
        "jsonld": [breadcrumb_ld([("Início", "/"), ("Áreas de atuação", "/areas/")])],
    }, priority="0.9")
    for a in C.AREAS:
        related = [x for x in arts if x["category"] == a["key"]]
        related += [x for x in arts if x not in related]
        render("area.html", f"areas/{a['slug']}/index.html", {
            "title": f"{a['seo_title']} | Ribeiro & Flores Advocacia",
            "description": a["description"],
            "section": "areas",
            "wa": a["wa"],
            "og_image": f"og-area-{a['key']}.jpg",
            "jsonld": [
                breadcrumb_ld([("Início", "/"), ("Áreas de atuação", "/areas/"), (a["name"], f"/areas/{a['slug']}/")]),
                {"@context": "https://schema.org", "@type": "Service", "name": a["name"], "serviceType": a["name"],
                 "description": a["description"], "provider": {"@id": ORG_ID},
                 "areaServed": {"@type": "Country", "name": "Brasil"}},
                faq_ld(a["faq"]),
            ],
        }, priority="0.9", a=a, related=related[:3])

    # ------------- artigos
    render("blog.html", "artigos/index.html", {
        "title": "Artigos Jurídicos | Ribeiro & Flores Advocacia",
        "description": "Artigos sobre direitos trabalhistas, INSS, direito do consumidor, contratos e empresas, "
                       "escritos em linguagem clara pela Ribeiro & Flores Advocacia.",
        "section": "artigos",
        "jsonld": [breadcrumb_ld([("Início", "/"), ("Artigos", "/artigos/")]),
                   {"@context": "https://schema.org", "@type": "Blog", "name": "Artigos Jurídicos — Ribeiro & Flores",
                    "url": SITE["url"] + "/artigos/", "publisher": {"@id": ORG_ID},
                    "blogPost": [{"@type": "BlogPosting", "headline": x["title"],
                                  "url": f"{SITE['url']}/artigos/{x['slug']}/", "datePublished": x["date"]} for x in arts]}],
        "lastmod": max(x["date"] for x in arts),
    }, priority="0.8", changefreq="weekly", used_categories={x["category"] for x in arts})
    for p in arts:
        canonical = f"{SITE['url']}/artigos/{p['slug']}/"
        related = [by_slug[s] for s in p["related"] if s in by_slug]
        related += [x for x in arts if x["category"] == p["category"] and x is not p and x not in related]
        related += [x for x in arts if x is not p and x not in related]
        render("article.html", f"artigos/{p['slug']}/index.html", {
            "title": f"{p['title']} | Ribeiro & Flores Advocacia",
            "description": p["excerpt"],
            "section": "artigos",
            "og_type": "article",
            "og_image": f"og-{p['slug']}.jpg",
            "article": p,
            "progress": True,
            "solid_header": True,
            "lastmod": p["date"],
            "wa": C.AREA_BY_KEY[p["category"]]["wa"] if p["category"] in C.AREA_BY_KEY else None,
            "jsonld": [
                breadcrumb_ld([("Início", "/"), ("Artigos", "/artigos/"), (p["title"], f"/artigos/{p['slug']}/")]),
                {"@context": "https://schema.org", "@type": "BlogPosting", "headline": p["title"],
                 "description": p["excerpt"], "datePublished": p["date"], "dateModified": p["date"],
                 "mainEntityOfPage": canonical, "inLanguage": "pt-BR", "articleSection": p["category_label"],
                 "wordCount": word_count(p["body"]),
                 "image": f"{SITE['url']}/assets/img/opt/og-{p['slug']}.jpg",
                 "author": {"@type": "Organization", "name": p["author"]["name"], "url": SITE["url"] + p["author"]["url"]},
                 "publisher": {"@id": ORG_ID}},
            ],
        }, priority="0.7", p=p, related=related[:3], area=C.AREA_BY_KEY.get(p["category"]))

    # ------------- contato
    render("contato.html", "contato/index.html", {
        "title": "Contato | Agende seu Atendimento | Ribeiro & Flores Advocacia",
        "description": f"Fale com a Ribeiro & Flores Advocacia pelo WhatsApp {SITE['phone_display']}, e-mail ou "
                       "formulário. Atendimento online em todo o Brasil, de segunda a sexta, das 8h às 19h.",
        "section": "contato",
        "jsonld": [breadcrumb_ld([("Início", "/"), ("Contato", "/contato/")]), org_ld()],
    }, priority="0.8")

    # ------------- obrigado / legal / 404
    render("simple.html", "obrigado/index.html", {
        "title": "Mensagem enviada | Ribeiro & Flores Advocacia", "description": "Recebemos sua mensagem.",
        "noindex": True, "hide_wa": True,
    }, in_sitemap=False, simple={
        "icon": "check", "eyebrow": "Mensagem recebida", "title": "Obrigado pelo contato.",
        "text": "Nossa equipe vai analisar sua solicitação e retornará em breve pelo telefone ou e-mail informado.",
        "wa": C.wa("Olá! Acabei de enviar uma mensagem pelo site da Ribeiro & Flores Advocacia."),
        "links": [("Artigos", "/artigos/"), ("Áreas de atuação", "/areas/")]})
    lp = L.privacy(SITE)
    render("legal.html", "privacidade/index.html", {
        "title": "Política de Privacidade | Ribeiro & Flores Advocacia",
        "description": "Saiba como a Ribeiro & Flores Advocacia coleta, utiliza e protege seus dados pessoais, nos termos da LGPD.",
    }, priority="0.3", changefreq="yearly", legal=lp)
    lt = L.terms(SITE)
    render("legal.html", "termos-de-uso/index.html", {
        "title": "Termos de Uso | Ribeiro & Flores Advocacia",
        "description": "Termos de uso e aviso legal do site da Ribeiro & Flores Advocacia.",
    }, priority="0.3", changefreq="yearly", legal=lt)
    render("simple.html", "404.html", {
        "title": "Página não encontrada | Ribeiro & Flores Advocacia",
        "description": "A página que você procura não foi encontrada.", "noindex": True,
        "canonical": SITE["url"] + "/404.html",
    }, in_sitemap=False, absolute=True, simple={
        "eyebrow": "Erro 404", "title": "Página não encontrada.",
        "text": "O endereço pode ter mudado. Veja abaixo os caminhos mais procurados ou fale com a gente.",
        "links": [("Áreas de atuação", "/areas/"), ("Artigos", "/artigos/"), ("Sócios", "/socios/"), ("Contato", "/contato/")]})

    # ------------- redirecionamentos das URLs antigas (.html)
    redirects = {
        "escritorio.html": "escritorio/", "socios.html": "socios/", "atuacao.html": "areas/",
        "artigos.html": "artigos/", "contato.html": "contato/", "privacidade.html": "privacidade/",
        "obrigado.html": "obrigado/",
        "direito-trabalhista.html": "areas/direito-trabalhista/",
        "direito-previdenciario.html": "areas/direito-previdenciario/",
        "direito-consumidor.html": "areas/direito-do-consumidor/",
        "direito-civil.html": "areas/direito-civil/",
        "direito-empresarial.html": "areas/direito-empresarial/",
    }
    for a in C.ARTICLES:
        redirects[a["old"]] = f"artigos/{a['slug']}/"
    for old, new in redirects.items():
        target = SITE["url"] + "/" + new
        (ROOT / old).write_text(
            "<!DOCTYPE html><html lang=\"pt-BR\"><head><meta charset=\"utf-8\">"
            f"<title>Redirecionando…</title><link rel=\"canonical\" href=\"{target}\">"
            "<meta name=\"robots\" content=\"noindex\">"
            f"<meta http-equiv=\"refresh\" content=\"0; url={new}\">"
            f"<script>location.replace(\"{new}\"+location.search+location.hash)</script></head>"
            f"<body><p>Esta página mudou de endereço: <a href=\"{new}\">{html.escape(target)}</a></p></body></html>\n",
            encoding="utf-8")

    # ------------- sitemap / robots / manifest
    lines = ['<?xml version="1.0" encoding="UTF-8"?>',
             '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for loc, pr, cf, lm in sitemap:
        lines.append(f"  <url><loc>{html.escape(loc)}</loc><lastmod>{lm or today}</lastmod>"
                     f"<changefreq>{cf}</changefreq><priority>{pr}</priority></url>")
    lines.append("</urlset>")
    (ROOT / "sitemap.xml").write_text("\n".join(lines) + "\n", encoding="utf-8")
    (ROOT / "robots.txt").write_text(
        "User-agent: *\nAllow: /\nDisallow: /obrigado/\nDisallow: /_build/\n\n"
        f"Sitemap: {SITE['url']}/sitemap.xml\n", encoding="utf-8")
    (ROOT / "site.webmanifest").write_text(
        '{"name":"Ribeiro & Flores Advocacia","short_name":"Ribeiro & Flores","lang":"pt-BR",'
        f'"start_url":"{BASE_PATH}/","display":"standalone","background_color":"#0b0b0c","theme_color":"#0b0b0c",'
        '"icons":[{"src":"assets/img/opt/icon-192.png","sizes":"192x192","type":"image/png"},'
        '{"src":"assets/img/opt/icon-512.png","sizes":"512x512","type":"image/png"}]}\n', encoding="utf-8")

    print(f"{len(written)} páginas geradas, {len(redirects)} redirecionamentos, {len(sitemap)} URLs no sitemap.")


if __name__ == "__main__":
    main()
