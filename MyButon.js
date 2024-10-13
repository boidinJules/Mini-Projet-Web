const colorCircle = document.getElementById('colorCircle');
const redSlider = document.getElementById('red');
const greenSlider = document.getElementById('green');
const blueSlider = document.getElementById('blue');
const redValue = document.getElementById('redValue');
const greenValue = document.getElementById('greenValue');
const blueValue = document.getElementById('blueValue');
const toggleButton = document.getElementById('toggleButton');

function updateColor() {
    const red = redSlider.value;
    const green = greenSlider.value;
    const blue = blueSlider.value;
    colorCircle.style.backgroundColor = `rgb(${red}, ${green}, ${blue})`;
    redValue.textContent = red;
    greenValue.textContent = green;
    blueValue.textContent = blue;
    LED_Color();
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
        console.log(res);
        btn.disabled = false;
    }
    )
    .catch(error => console.error('Error:', error));
}
function LED_OFF() {
    const btn= document.getElementById('turnOffButton') 
    btn.disabled = true;
    val =[0,0,0]

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
        console.log(res);
        btn.disabled = false;
    }
    )
    .catch(error => console.error('Error:', error));
}

tsParticles.load("tsparticles", {
    background: {
      color: {
        value: "Wallpapers.jpeg",
      },
    },
    fpsLimit: 120,
    interactivity: {
      events: {
        onClick: {
          enable: true,
          mode: "repulse",
        },
        onHover: {
          enable: true,
          mode: 'grab',
        },
      },
      modes: {
        push: {
          distance: 200,
          duration: 15,
        },
        grab: {
          distance: 150,
        },
      },
    },
    particles: {
      color: {
        value: "#FFFFFF",
      },
      links: {
        color: "#FFFFFF",
        distance: 150,
        enable: true,
        opacity: 0.3,
        width: 1,
      },
      move: {
        direction: "none",
        enable: true,
        outModes: {
          default: "bounce",
        },
        random: true,
        speed: 1,
        straight: false,
      },
      number: {
        density: {
          enable: true,
        },
        value: 150,
      },
      opacity: {
        value: 1.0,
      },
      shape: {
        type: "circle",
      },
      size: {
        value: { min: 1, max: 3 },
      },
    },
    detectRetina: true,
  }); 