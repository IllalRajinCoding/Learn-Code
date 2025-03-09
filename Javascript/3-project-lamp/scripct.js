const switchBtn = document.querySelector('.switch');
const body = document.body;

switchBtn.addEventListener('click', () => {
    body.classList.toggle('on');
})