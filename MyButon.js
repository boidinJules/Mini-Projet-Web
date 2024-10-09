const colorCircle = document.getElementById('colorCircle');
const redSlider = document.getElementById('red');
const greenSlider = document.getElementById('green');
const blueSlider = document.getElementById('blue');
const redValue = document.getElementById('redValue');
const greenValue = document.getElementById('greenValue');
const blueValue = document.getElementById('blueValue');

function updateColor() {
    const red = redSlider.value;
    const green = greenSlider.value;
    const blue = blueSlider.value;

    colorCircle.style.backgroundColor = `rgb(${red}, ${green}, ${blue})`;
    redValue.textContent = red;
    greenValue.textContent = green;
    blueValue.textContent = blue;
}

redSlider.addEventListener('input', updateColor);
greenSlider.addEventListener('input', updateColor);
blueSlider.addEventListener('input', updateColor);

function LED_Color() {
    const btn= document.getElementById('send_btn') 
    btn.disabled = true;
    const red = redSlider.value;
    const green = greenSlider.value;
    const blue = blueSlider.value;
    val =[red,green,blue]

    fetch('control.php', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: new URLSearchParams({
            'color': val
        })
    })
    .then(response => response.text())
    .then(res => {
        // action = JSON.parse(res);
        console.log(res);
        btn.disabled = false;
        
        // const ledImage = document.getElementById('ledImage');
        // if (action.led === 'on') {
        //     ledImage.src = 'led_on.jpg';
        //     ledImage.alt = 'LED is on';
        // } else {
        //     ledImage.src = 'led_off.jpg';
        //     ledImage.alt = 'LED is off';
        // }
        // ledImage.style.display = 'block';
    }
    )
    .catch(error => console.error('Error:', error));
}