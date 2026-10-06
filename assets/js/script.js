/* =====================================================================
   RIBEIRO & FLORES ADVOCACIA — Scripts do site
   ===================================================================== */
(function () {
  "use strict";
  var doc = document.documentElement;
  doc.classList.add("js");
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  function $(s, c) { return (c || document).querySelector(s); }
  function $$(s, c) { return Array.prototype.slice.call((c || document).querySelectorAll(s)); }
  function store(k, v) { try { if (v === undefined) return localStorage.getItem(k); localStorage.setItem(k, v); } catch (e) { return null; } }

  /* ---------- Header sólido ao rolar + barra de leitura ---------- */
  var header = $(".site-header");
  var progress = $(".progress");
  var article = $(".prose");
  var ticking = false;
  function onScroll() {
    var y = window.scrollY || 0;
    if (header && !header.classList.contains("site-header--solid")) header.classList.toggle("is-solid", y > 40);
    if (progress && article) {
      var r = article.getBoundingClientRect();
      var total = r.height - window.innerHeight * 0.6;
      var p = Math.min(1, Math.max(0, -r.top / (total || 1)));
      progress.style.transform = "scaleX(" + p + ")";
    }
    ticking = false;
  }
  window.addEventListener("scroll", function () { if (!ticking) { requestAnimationFrame(onScroll); ticking = true; } }, { passive: true });
  onScroll();

  /* ---------- Menu mobile ---------- */
  var menu = $("#mobile-nav");
  var openBtn = $(".menu-btn");
  var closeBtn = menu && $(".menu-close", menu);
  function setMenu(open) {
    if (!menu) return;
    menu.classList.toggle("is-open", open);
    menu.setAttribute("aria-hidden", open ? "false" : "true");
    if (openBtn) openBtn.setAttribute("aria-expanded", open ? "true" : "false");
    document.body.classList.toggle("menu-open", open);
    $$(".mobile-item", menu).forEach(function (el, i) { el.style.transitionDelay = open ? (80 + i * 45) + "ms" : "0ms"; });
    if (open && closeBtn) closeBtn.focus();
    else if (!open && openBtn) openBtn.focus();
  }
  if (openBtn) openBtn.addEventListener("click", function () { setMenu(true); });
  if (closeBtn) closeBtn.addEventListener("click", function () { setMenu(false); });
  document.addEventListener("keydown", function (e) { if (e.key === "Escape" && menu && menu.classList.contains("is-open")) setMenu(false); });
  if (menu) $$("a", menu).forEach(function (a) { a.addEventListener("click", function () { setMenu(false); }); });

  /* ---------- Animações ao rolar ---------- */
  $$("[data-stagger]").forEach(function (group) {
    var step = parseInt(group.getAttribute("data-stagger"), 10) || 90;
    $$("[data-reveal]", group).forEach(function (el, i) { el.style.setProperty("--d", (i * step) + "ms"); });
  });
  var revealEls = $$("[data-reveal]");
  if (reduce || !("IntersectionObserver" in window)) {
    revealEls.forEach(function (el) { el.classList.add("is-in"); });
  } else {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add("is-in"); io.unobserve(en.target); }
      });
    }, { rootMargin: "0px 0px -8% 0px", threshold: 0.08 });
    revealEls.forEach(function (el) { io.observe(el); });
  }

  /* ---------- Contadores (stats) ---------- */
  $$("[data-count]").forEach(function (el) {
    var to = parseInt(el.getAttribute("data-count"), 10);
    var suffix = el.getAttribute("data-suffix") || "";
    if (reduce || !("IntersectionObserver" in window)) return;
    var o = new IntersectionObserver(function (ents) {
      if (!ents[0].isIntersecting) return;
      o.disconnect();
      var t0 = performance.now(), dur = 1200;
      (function tick(t) {
        var k = Math.min(1, (t - t0) / dur), e = 1 - Math.pow(1 - k, 3);
        el.textContent = Math.round(to * e) + suffix;
        if (k < 1) requestAnimationFrame(tick);
      })(t0);
    }, { threshold: 0.6 });
    o.observe(el);
  });

  /* ---------- Blog: categorias + busca ---------- */
  var list = $("[data-posts]");
  if (list) {
    var posts = $$("[data-post]", list);
    var chips = $$(".chip");
    var input = $("#busca-artigos");
    var empty = $(".empty");
    var params = new URLSearchParams(location.search);
    var cat = params.get("categoria") || "todos";
    var norm = function (s) { return (s || "").toLowerCase().normalize("NFD").replace(/[̀-ͯ]/g, ""); };
    if (input && params.get("q")) input.value = params.get("q");
    function apply() {
      var q = norm(input ? input.value.trim() : "");
      var shown = 0;
      posts.forEach(function (p) {
        var okCat = cat === "todos" || p.getAttribute("data-cat") === cat;
        var okQ = !q || norm(p.getAttribute("data-search")).indexOf(q) > -1;
        var on = okCat && okQ;
        p.hidden = !on;
        if (on) shown++;
      });
      chips.forEach(function (c) { c.setAttribute("aria-pressed", c.getAttribute("data-filter") === cat ? "true" : "false"); });
      if (empty) empty.classList.toggle("is-visible", shown === 0);
      var feat = $("[data-featured]");
      if (feat) feat.hidden = !(cat === "todos" && !q);
      var url = new URL(location.href);
      cat === "todos" ? url.searchParams.delete("categoria") : url.searchParams.set("categoria", cat);
      q ? url.searchParams.set("q", input.value.trim()) : url.searchParams.delete("q");
      history.replaceState(null, "", url);
    }
    chips.forEach(function (c) { c.addEventListener("click", function () { cat = c.getAttribute("data-filter"); apply(); }); });
    if (input) input.addEventListener("input", apply);
    apply();
  }

  /* ---------- Compartilhar ---------- */
  $$("[data-copy]").forEach(function (b) {
    b.addEventListener("click", function () {
      var url = location.href.split("?")[0];
      if (navigator.share) { navigator.share({ title: document.title, url: url }).catch(function () {}); return; }
      if (navigator.clipboard) navigator.clipboard.writeText(url).then(function () {
        b.setAttribute("aria-label", "Link copiado"); b.title = "Link copiado";
      });
    });
  });

  /* ---------- Formulário de contato ---------- */
  var form = $("#form-contato");
  if (form) {
    var fields = $$("input[required], select[required], textarea[required]", form);
    function validate(el) {
      var ok = el.type === "checkbox" ? el.checked : el.checkValidity() && el.value.trim() !== "";
      if (el.name === "telefone" && ok) ok = el.value.replace(/\D/g, "").length >= 10;
      el.setAttribute("aria-invalid", ok ? "false" : "true");
      var err = $("#" + el.id + "-err");
      if (err) err.classList.toggle("is-visible", !ok);
      return ok;
    }
    fields.forEach(function (el) {
      el.addEventListener("blur", function () { if (el.value) validate(el); });
      el.addEventListener("change", function () { if (el.getAttribute("aria-invalid") === "true") validate(el); });
    });
    var tel = $("#telefone", form);
    if (tel) tel.addEventListener("input", function () {
      var d = tel.value.replace(/\D/g, "").slice(0, 11);
      var f = d;
      if (d.length > 2) f = "(" + d.slice(0, 2) + ") " + d.slice(2);
      if (d.length > 7) f = "(" + d.slice(0, 2) + ") " + d.slice(2, d.length - 4) + "-" + d.slice(-4);
      tel.value = f;
    });
    form.addEventListener("submit", function (e) {
      var ok = fields.map(validate).every(Boolean);
      if (!ok) { e.preventDefault(); var first = $("[aria-invalid='true']", form); if (first) first.focus(); return; }
      if (!window.fetch || !window.FormData) return; // envio normal (página de obrigado)
      e.preventDefault();
      var btn = $("button[type=submit]", form);
      var status = $(".form-status", form);
      btn.setAttribute("aria-busy", "true");
      var label = btn.innerHTML;
      btn.textContent = "Enviando…";
      var data = new FormData(form);
      fetch(form.getAttribute("data-ajax"), { method: "POST", headers: { Accept: "application/json" }, body: data })
        .then(function (r) { return r.json().then(function (j) { return { ok: r.ok, j: j }; }); })
        .then(function (res) {
          if (!res.ok || String(res.j.success) === "false") throw new Error(res.j.message || "Falha no envio");
          form.hidden = true;
          var succ = $(".form-success");
          if (succ) { succ.classList.add("is-visible"); succ.setAttribute("tabindex", "-1"); succ.focus(); }
          if (window.gtag) window.gtag("event", "generate_lead", { form: "contato" });
        })
        .catch(function () {
          // Se o envio via AJAX falhar, tenta o envio tradicional
          status.className = "form-status is-error";
          status.textContent = "Não foi possível enviar agora. Tentando novamente…";
          btn.innerHTML = label; btn.removeAttribute("aria-busy");
          setTimeout(function () { form.submit(); }, 900);
        });
    });
    // Pré-seleciona a área vinda da URL (?area=trabalhista)
    var area = new URLSearchParams(location.search).get("area");
    var sel = $("#area", form);
    if (area && sel) $$("option", sel).forEach(function (o) { if (o.getAttribute("data-key") === area) sel.value = o.value; });
  }

  /* ---------- WhatsApp: rastreio de clique ---------- */
  $$("a[href*='wa.me']").forEach(function (a) {
    a.addEventListener("click", function () { if (window.gtag) window.gtag("event", "whatsapp_click", { page: location.pathname }); });
  });

  /* ---------- Consentimento (LGPD) + Google Analytics ---------- */
  var gaId = document.body.getAttribute("data-ga");
  var bar = $(".consent-bar");
  function loadGA() {
    if (!gaId || window.gtag) return;
    var s = document.createElement("script");
    s.async = true; s.src = "https://www.googletagmanager.com/gtag/js?id=" + gaId;
    document.head.appendChild(s);
    window.dataLayer = window.dataLayer || [];
    window.gtag = function () { window.dataLayer.push(arguments); };
    window.gtag("js", new Date());
    window.gtag("config", gaId, { anonymize_ip: true });
  }
  if (gaId && bar) {
    var choice = store("rf-consent");
    if (choice === "yes") loadGA();
    else if (choice !== "no") setTimeout(function () { bar.classList.add("is-visible"); }, 1200);
    $$("[data-consent]", bar).forEach(function (b) {
      b.addEventListener("click", function () {
        var v = b.getAttribute("data-consent");
        store("rf-consent", v);
        bar.classList.remove("is-visible");
        if (v === "yes") loadGA();
      });
    });
  }
  $$("[data-consent-reset]").forEach(function (a) {
    a.addEventListener("click", function (e) { e.preventDefault(); store("rf-consent", ""); if (bar) bar.classList.add("is-visible"); });
  });

  /* Ano atual no rodapé */
  $$("[data-year]").forEach(function (el) { el.textContent = new Date().getFullYear(); });
})();
