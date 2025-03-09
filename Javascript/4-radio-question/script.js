const btn = document.querySelector('button');
// const benar = document.getElementById('hijau');
// const salah = document.getElementById('salah');

const benar = document.getElementById('hijau');
const salah = document.getElementById('merah');


benar.style.display = 'none';
salah.style.display = 'none';

btn.addEventListener('click', () => {
    const yes = document.querySelector('input[value="benar"]');
    const no = document.querySelector('input[value="salah"]');


    if (no.checked) {
        salah.style.display = 'none';
        benar.style.display = 'none';
    }
    else if (yes.checked) {
        benar.style.display = 'none';
        salah.style.display = 'block';
    }
    else {
        benar.style.display = 'none';
        salah.style.display = 'block';
    }
});