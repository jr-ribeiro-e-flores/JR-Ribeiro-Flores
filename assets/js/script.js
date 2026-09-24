/* ==========================================
   JR RIBEIRO & FLORES ADVOCACIA
   SCRIPT GLOBAL
========================================== */

document.addEventListener("DOMContentLoaded", () => {

    /* ==========================
       HEADER AO ROLAR
    ========================== */

    const header = document.querySelector("header");

    if(header){

        window.addEventListener("scroll", () => {

            if(window.scrollY > 50){

                header.classList.add("scrolled");

            }else{

                header.classList.remove("scrolled");

            }

        });

    }

    /* ==========================
       MENU ATIVO
    ========================== */

    const paginaAtual = window.location.pathname.split("/").pop();

    document.querySelectorAll("nav a").forEach(link => {

        const href = link.getAttribute("href");

        if(href === paginaAtual){

            link.style.color = "#C9A227";

        }

    });

});

/* MENU MOBILE (páginas internas) */
document.addEventListener("DOMContentLoaded", () => {
    const btn = document.querySelector(".rf-toggle");
    const nav = document.querySelector("nav.rf-nav");
    if(!btn || !nav) return;
    const hd = btn.closest("header");
    if(hd && getComputedStyle(hd).position === "static"){ hd.style.position = "relative"; hd.style.zIndex = "999"; }
    btn.addEventListener("click", () => {
        const open = nav.classList.toggle("open");
        btn.setAttribute("aria-expanded", open);
        btn.innerHTML = open ? '<i class="fa-solid fa-xmark"></i>' : '<i class="fa-solid fa-bars"></i>';
    });
    nav.querySelectorAll("a").forEach(a => a.addEventListener("click", () => nav.classList.remove("open")));
});
