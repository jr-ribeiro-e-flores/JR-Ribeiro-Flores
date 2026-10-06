"""Gera as imagens otimizadas do site (WebP redimensionado, capas, favicons, OG).

Uso:  python3 _build/images.py
As fontes originais ficam em assets/img/ e os arquivos gerados em assets/img/opt/.
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter, ImageFont, ImageEnhance

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "assets" / "img"
OUT = SRC / "opt"
OUT.mkdir(exist_ok=True)
FONTS = Path(__file__).resolve().parent / "fonts"

GOLD = (197, 162, 83)
INK = (10, 10, 11)


def font(name, size):
    return ImageFont.truetype(str(FONTS / name), size)


def webp(img, name, width, q=80):
    im = img.copy()
    if im.width > width:
        im = im.resize((width, round(im.height * width / im.width)), Image.LANCZOS)
    im.save(OUT / f"{name}-{width}.webp", "WEBP", quality=q, method=6)
    return im.size


def crop_ratio(img, box):
    return img.crop(box)


def gradient_overlay(size, stops):
    """stops: list of (x_fraction, alpha) horizontal gradient of ink colour."""
    w, h = size
    g = Image.new("L", (w, 1))
    for x in range(w):
        f = x / (w - 1)
        for (x0, a0), (x1, a1) in zip(stops, stops[1:]):
            if x0 <= f <= x1:
                t = (f - x0) / (x1 - x0) if x1 > x0 else 0
                g.putpixel((x, 0), int(a0 + (a1 - a0) * t))
                break
    g = g.resize((w, h))
    layer = Image.new("RGBA", (w, h), INK + (0,))
    layer.putalpha(g)
    return layer


def vertical_overlay(size, top, bottom):
    w, h = size
    g = Image.new("L", (1, h))
    for y in range(h):
        t = y / (h - 1)
        g.putpixel((0, y), int(top + (bottom - top) * t))
    g = g.resize((w, h))
    layer = Image.new("RGBA", (w, h), INK + (0,))
    layer.putalpha(g)
    return layer


def wrap(draw, text, fnt, max_w):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if draw.textlength(t, font=fnt) <= max_w:
            cur = t
        else:
            lines.append(cur)
            cur = w
    lines.append(cur)
    return lines


# ---------------------------------------------------------------- hero
hero = Image.open(SRC / "hero.jpg").convert("RGB")  # 1402x1122
for w in (1400, 960, 640):
    webp(hero, "hero", w, q=78)

# Recortes do hero usados como base visual das áreas e das capas
CROPS = {
    "trabalhista": (250, 520, 900, 1000),     # malhete
    "previdenciario": (1000, 540, 1402, 900), # livros
    "consumidor": (700, 120, 920, 520),       # balança
    "civil": (760, 120, 1180, 900),           # estátua
    "empresarial": (0, 600, 560, 900),        # livros antigos
    "advocacia": (0, 0, 1402, 1122),          # composição completa
}


def cover_base(key, size):
    box = CROPS[key]
    im = hero.crop(box)
    tw, th = size
    # preencher mantendo proporção (object-fit: cover)
    r = max(tw / im.width, th / im.height)
    im = im.resize((round(im.width * r), round(im.height * r)), Image.LANCZOS)
    l = (im.width - tw) // 2
    t = (im.height - th) // 2
    im = im.crop((l, t, l + tw, t + th))
    im = ImageEnhance.Brightness(im).enhance(0.92)
    return im


def make_cover(key, eyebrow, title, size, path, fmt="WEBP", q=82):
    """Capa tipográfica: fundo grafite, moldura fina, brasão em marca d'água."""
    w, h = size
    base = Image.new("RGBA", size, (18, 18, 20, 255))
    # brilho suave à direita
    glow = Image.new("L", size, 0)
    gd = ImageDraw.Draw(glow)
    gd.ellipse((int(w * .45), int(-h * .4), int(w * 1.5), int(h * 1.2)), fill=60)
    glow = glow.filter(ImageFilter.GaussianBlur(w // 8))
    layer = Image.new("RGBA", size, (176, 141, 87, 0)); layer.putalpha(glow.point(lambda v: int(v * .35)))
    base.alpha_composite(layer)
    # brasão em marca d'água
    lh = int(h * .92)
    lg = _logo_for_cover.resize((round(_logo_for_cover.width * lh / _logo_for_cover.height), lh), Image.LANCZOS)
    a = lg.split()[3].point(lambda v: int(v * .07))
    lg.putalpha(a)
    base.alpha_composite(lg, (w - lg.width + int(w * .06), (h - lh) // 2))
    d = ImageDraw.Draw(base)
    pad = round(w * .045)
    d.rectangle((pad, pad, w - pad, h - pad), outline=(176, 141, 87, 110), width=max(1, w // 900))
    inner = pad + round(w * .05)
    fe = font("inter-600.ttf", max(11, round(w * .0165)))
    d.text((inner, inner + round(h * .04)), eyebrow.upper(), font=fe, fill=(201, 169, 110, 255))
    ft = font("cormorant-garamond-latin-500-normal.ttf", round(w * .062))
    lines = wrap(d, title, ft, w * .66)
    lh_t = round(w * .066)
    y = h - inner - round(h * .15) - lh_t * len(lines)
    for ln in lines:
        d.text((inner, y), ln, font=ft, fill=(240, 236, 228, 255))
        y += lh_t
    d.rectangle((inner, h - inner - round(h * .045), inner + round(w * .05), h - inner - round(h * .045) + max(1, w // 600)), fill=(176, 141, 87, 255))
    fm = font("inter-500.ttf", max(10, round(w * .0135)))
    d.text((inner + round(w * .065), h - inner - round(h * .045) - round(w * .009)), "RIBEIRO & FLORES ADVOCACIA", font=fm, fill=(190, 184, 172, 255))
    out = base.convert("RGB")
    if fmt == "WEBP":
        out.save(path, "WEBP", quality=q, method=6)
    else:
        out.save(path, "JPEG", quality=86, optimize=True, progressive=True)


def make_area_banner(key, path_prefix):
    for w in (1600, 800):
        size = (w, round(w * 0.42))
        im = cover_base(key, size)
        im.save(OUT / f"{path_prefix}-{w}.webp", "WEBP", quality=74, method=6)


# ---------------------------------------------------------------- retratos
def portrait(src, box, name):
    im = Image.open(SRC / src).convert("RGB").crop(box)
    im = im.resize((720, 960), Image.LANCZOS)
    for w in (720, 420):
        webp(im, name, w, q=80)
    return im


josue = portrait("josue-2.jpg", (180, 30, 730, 763), "josue")
renata = portrait("renata.jpg", (0, 40, 900, 1240), "renata")


def bw(im, name):
    """Retrato em preto e branco editorial, com tons padronizados."""
    from PIL import ImageOps
    g = ImageOps.grayscale(im)
    g = ImageOps.autocontrast(g, cutoff=(0.5, 0.3))
    g = ImageEnhance.Contrast(g).enhance(1.08)
    g = ImageEnhance.Brightness(g).enhance(0.97)
    # leve tom quente (papel fotográfico)
    toned = ImageOps.colorize(g, black=(14, 13, 12), white=(246, 243, 236), mid=(128, 124, 118))
    for w in (720, 420):
        webp(toned, name, w, q=82)


bw(josue, "josue-bw")
bw(renata, "renata-bw")

# Recorte vertical da estátua da Justiça (usado em seções institucionais)
_j = hero.crop((735, 110, 1185, 710)).resize((720, 960), Image.LANCZOS)
_j = ImageEnhance.Brightness(_j).enhance(1.05)
for w in (720, 420):
    webp(_j, "justice", w, q=78)

# ---------------------------------------------------------------- logo / favicons
logo = Image.open(SRC / "logo-rf.png").convert("RGBA")
# remove o fundo branco/cinza claro em volta do brasão
px = logo.load()
for y in range(logo.height):
    for x in range(logo.width):
        r, g, b, a = px[x, y]
        lum = (r + g + b) / 3
        sat = max(r, g, b) - min(r, g, b)
        if sat < 40 and lum > 170:
            # quase branco -> transparente (com suavização)
            px[x, y] = (r, g, b, int(a * max(0, min(1, (235 - lum) / 65)) if lum < 235 else 0))
bbox = logo.getbbox()
logo = logo.crop(bbox)
_logo_for_cover = logo
for h in (104, 208):
    w = round(logo.width * h / logo.height)
    lg = logo.resize((w, h), Image.LANCZOS)
    lg.save(OUT / f"crest-{h}.png", optimize=True)
    lg.save(OUT / f"crest-{h}.webp", "WEBP", quality=88, method=6)


def icon(size, path, pad_ratio=0.14):
    bg = Image.new("RGBA", (size, size), INK + (255,))
    inner = round(size * (1 - 2 * pad_ratio))
    w = round(logo.width * inner / logo.height)
    lg = logo.resize((w, inner), Image.LANCZOS)
    bg.alpha_composite(lg, ((size - w) // 2, (size - inner) // 2))
    bg.save(path, optimize=True)


icon(512, OUT / "icon-512.png")
icon(192, OUT / "icon-192.png")
icon(180, OUT / "apple-touch-icon.png")
icon(48, OUT / "favicon-48.png", 0.08)
icon(32, ROOT / "favicon.png", 0.06)
ico = Image.open(OUT / "favicon-48.png")
ico.save(ROOT / "favicon.ico", sizes=[(16, 16), (32, 32), (48, 48)])

# ---------------------------------------------------------------- OG padrão
make_cover(None, "Advocacia · Atendimento em todo o Brasil", "Ribeiro & Flores Advocacia", (1200, 630), OUT / "og-default.jpg", fmt="JPEG")

# ---------------------------------------------------------------- capas (chamadas pelo build)
if __name__ == "__main__":
    import json, sys
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from content import ARTICLES, AREAS
    for a in ARTICLES:
        make_cover(a["cover"], a["category_label"], a["title"], (1200, 675), OUT / f"cover-{a['slug']}-1200.webp")
        make_cover(a["cover"], a["category_label"], a["title"], (640, 360), OUT / f"cover-{a['slug']}-640.webp")
        make_cover(a["cover"], a["category_label"], a["title"], (1200, 630), OUT / f"og-{a['slug']}.jpg", fmt="JPEG")
    for ar in AREAS:
        make_area_banner(ar["cover"], f"area-{ar['key']}")
        make_cover(ar["cover"], "Área de atuação", ar["name"], (1200, 630), OUT / f"og-area-{ar['key']}.jpg", fmt="JPEG")
    print("imagens geradas em", OUT)
