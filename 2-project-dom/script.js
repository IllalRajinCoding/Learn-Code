const btnElement = document.querySelector('button');
const spanElement = document.getElementById('updateTittle');

btnElement.onclick = function() {
    const urName = prompt('Enter your name: ');
    spanElement.textContent = urName;
}