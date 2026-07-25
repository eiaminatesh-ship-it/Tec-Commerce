// Welcome Message
console.log("Welcome to Tec-Commerce");

// Smooth Scroll

document.querySelectorAll("a[href^='#']").forEach(anchor => {

    anchor.addEventListener("click", function(e){

        e.preventDefault();

        document.querySelector(this.getAttribute("href")).scrollIntoView({

            behavior:"smooth"

        });

    });

});

// Button Hover Animation

const buttons = document.querySelectorAll(".btn");

buttons.forEach(btn=>{

    btn.addEventListener("mouseenter",()=>{

        btn.style.transform="scale(1.05)";

    });

    btn.addEventListener("mouseleave",()=>{

        btn.style.transform="scale(1)";

    });

});

// Card Animation

const cards = document.querySelectorAll(".card");

window.addEventListener("scroll",()=>{

    cards.forEach(card=>{

        let top = card.getBoundingClientRect().top;

        if(top < window.innerHeight-100){

            card.style.opacity="1";

            card.style.transform="translateY(0px)";

        }

    });

});