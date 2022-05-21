let allImages = document.querySelectorAll('.image_content img');

let indexImage = 0

function changeImage() {
    allImages[indexImage].classList.remove('activated');
    indexImage++;
    if (indexImage >= allImages.length) {
        indexImage = 0;
    };
    allImages[indexImage].classList.add('activated');
}

function start() {
    setInterval(() => {
        changeImage()
    }, 8000)
}

window.addEventListener('load', start)