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
