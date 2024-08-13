let currentIndex = 0;

document.addEventListener('DOMContentLoaded', () => {
    const images = [
        'https://drive.google.com/file/d/0B8S7-5SSksg_V3hScFYyUmZ5cTg/view?usp=drive_link&resourcekey=0-3MkW2IrugOALy0cNkRBHHA',
        'https://drive.google.com/file/d/1LBSnggZJP4a1vmQiODhYvOG3J8Q6xuic/view?usp=drive_link',
        'https://drive.google.com/file/d/106n47I9uPEcjYeoADgSgqO-E6Lpl8Up9/view?usp=drive_link'
        // Add more image URLs as needed
    ];
    
    const carouselInner = document.getElementById('carouselInner');
    images.forEach((image, index) => {
        const div = document.createElement('div');
        div.classList.add('carousel-item');
        if (index === 0) div.classList.add('active');
        const img = document.createElement('img');
        img.src = image;
        img.alt = `Image ${index + 1}`;
        div.appendChild(img);
        carouselInner.appendChild(div);
    });
});

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
