function switch_led(action) {
    fetch('control.php', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: new URLSearchParams({
            'action': action
        })
    })
    .then(response => response.text())
    .then(res => {
        action = JSON.parse(res);
        console.log(action.led);
        
        const ledImage = document.getElementById('ledImage');
        if (action.led === 'on') {
            ledImage.src = 'led_on.jpg';
            ledImage.alt = 'LED is on';
        } else {
            ledImage.src = 'led_off.jpg';
            ledImage.alt = 'LED is off';
        }
        ledImage.style.display = 'block';
    }
    )
    .catch(error => console.error('Error:', error));
}