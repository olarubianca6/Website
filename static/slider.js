const slides = document.querySelectorAll(".slide");

slides.forEach((slide, i) => {
  slide.style.transform = `translateX(${i * 100}%)`;
});

const nextSlide = document.querySelector(".btn-next");

let curSlide = 0;
let maxSlide = slides.length;

nextSlide.addEventListener("click", function () {
  curSlide = (curSlide + 1) % maxSlide;

  slides.forEach((slide, i) => {
    slide.style.transform = `translateX(${(i - curSlide + maxSlide) % maxSlide * 100}%)`;
  });
});

const prevSlide = document.querySelector(".btn-prev");

prevSlide.addEventListener("click", function () {
  curSlide = (curSlide - 1 + maxSlide) % maxSlide;

  slides.forEach((slide, i) => {
    slide.style.transform = `translateX(${(i - curSlide + maxSlide) % maxSlide * 100}%)`;
  });
});