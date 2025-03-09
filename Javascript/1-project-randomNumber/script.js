const createLucky = document.getElementById('number-lucky');
const generateBtn = document.getElementById('generate-luck-btn');

generateBtn.addEventListener('click', () => {


    const randomLuck = Math.floor(Math.random() * 100) + 1;
    createLucky.textContent = randomLuck;

    let lucky = randomLuck;
    console.log(lucky);

    if (lucky > 50) {
        createLucky.
        alert('You are lucky');
    } else {
        alert('You are unlucky');
    }
}
);