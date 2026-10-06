# Site Ribeiro & Flores Advocacia — guia de manutenção

O site é estático (HTML/CSS/JS puros) e hospedado no GitHub Pages. As páginas são **geradas** a partir
dos arquivos desta pasta `_build/`. Não edite os `index.html` gerados diretamente: edite o conteúdo aqui e rode o build.

## Estrutura

| Arquivo | O que contém |
|---|---|
| `content.py` | Contato, WhatsApp, redes sociais, sócios, áreas de atuação, FAQs e lista de artigos |
| `articles/*.html` | Corpo de cada artigo |
| `legal.py` | Política de Privacidade e Termos de Uso |
| `templates/` | Layout das páginas |
| `images.py` | Gera imagens otimizadas (WebP), capas dos artigos, favicons e imagens de compartilhamento |
| `../assets/css/style.css` | Todo o visual do site (cores, fontes, espaçamentos) |
| `../assets/js/script.js` | Menu, animações, busca de artigos, formulário, consentimento de cookies |

## Como atualizar

```bash
pip install jinja2 pillow brotli fonttools   # uma vez
python3 _build/images.py   # só quando trocar fotos ou criar artigo novo (gera a capa)
python3 _build/build.py    # sempre que alterar textos
```

### Publicar um artigo novo
1. Crie `_build/articles/meu-artigo.html` com o texto (use `<p>`, `<h2>`, `<ul>`, `<strong>`).
2. Adicione um item em `ARTICLES` no `content.py` (slug, título, resumo, categoria, data).
3. Rode `images.py` e `build.py`. O artigo entra automaticamente no blog, no sitemap, nos relacionados e na página da área.

### Completar os perfis dos sócios
Em `PARTNERS` (content.py), preencha `oab`, `education` (formação) e `experience`. Campos vazios ficam ocultos.
**O número de inscrição na OAB é obrigatório na publicidade da advocacia (Provimento 205/2021).**

## Domínio próprio (ribeiroeflores.adv.br)
1. Registre o domínio no Registro.br (domínios `.adv.br` exigem inscrição na OAB).
2. No Registro.br, aponte o DNS: registros **A** para `185.199.108.153`, `185.199.109.153`, `185.199.110.153`,
   `185.199.111.153` e um **CNAME** `www` → `jr-ribeiro-e-flores.github.io`.
3. No GitHub: Settings → Pages → Custom domain → `ribeiroeflores.adv.br` e marque **Enforce HTTPS**.
4. Em `content.py`, troque `"url"` para `"https://ribeiroeflores.adv.br"` e rode o build
   (atualiza links canônicos, sitemap, formulário e imagens de compartilhamento).

## E-mail profissional (contato@ribeiroeflores.adv.br)
Após o domínio ativo, contrate um provedor (Google Workspace, Zoho Mail ou Microsoft 365) e cadastre os registros MX
indicados por ele no Registro.br. Depois troque `email` e `form_email` no `content.py`
(o FormSubmit envia um e-mail de ativação no primeiro envio para o novo endereço).

## Google Search Console e Analytics
- **Search Console**: adicione a propriedade, escolha verificação por *Meta tag*, cole o código em
  `gsc_verification` (content.py), rode o build e publique. Depois envie `sitemap.xml` em *Sitemaps*.
- **Analytics (GA4)**: crie a propriedade e cole o ID (`G-XXXXXXX`) em `ga_id`. O site passa a exibir o aviso de
  cookies e só carrega o Analytics após o consentimento (LGPD). A Política de Privacidade é ajustada automaticamente.
