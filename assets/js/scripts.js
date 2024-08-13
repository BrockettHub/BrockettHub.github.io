
let currentIndex = 0;

function changeSlide(direction) {
    const items = document.querySelectorAll('.carousel-item');
    currentIndex += direction;

    if (currentIndex >= items.length) {
        currentIndex = 0;
    } else if (currentIndex < 0) {
        currentIndex = items.length - 1;
    }

    const offset = -currentIndex * 100;
    document.querySelector('.carousel-inner').style.transform = `translateX(${offset}%)`;
}