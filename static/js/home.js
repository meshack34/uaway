const wrapper = document.querySelector(".testimonial-wrapper");
const prevBtn = document.querySelector(".prev");
const nextBtn = document.querySelector(".next");

let index = 0;

function updateSlide() {
    wrapper.style.transform = `translateX(-${index * 100}%)`;
}

nextBtn.addEventListener("click", () => {
    if (index < wrapper.children.length - 1) {
        index++;
    } else {
        index = 0;
    }
    updateSlide();
});

prevBtn.addEventListener("click", () => {
    if (index > 0) {
        index--;
    } else {
        index = wrapper.children.length - 1;
    }
    updateSlide();
});
