const menuBtn = document.querySelector(".menu-btn");
const navigation = document.querySelector(".navigation");

// For menu button click
menuBtn.addEventListener("click", () => {
    // Toggle "active" class on menu button and navigation
    menuBtn.classList.add("active");
    navigation.classList.add("active");
});
 // Slider functionality
const btns = document.querySelectorAll(".nav-btn");
const slides = document.querySelectorAll(".video-slide");
const contents = document.querySelectorAll(".content");

// Function to activate a specific slide
var sliderNav = function(manual){
    btns.forEach((btn) => {
        btn.classList.remove("active");

});

slides.forEach((slide) => {
    slide.classList.remove("active");
});

contents.forEach((content) => {
    content.classList.remove("active");
});

btns[manual].classList.add("active");
slides[manual].classList.add("active");
contents[manual].classList.add("active");
}

btns.forEach((btn, i) => {
    btn.addEventListener("click", () => {
        // Activate the corresponding slide when a navigation button is clicked
        sliderNav(i);
    });
});