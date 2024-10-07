async function switch_led(state) {
    fetch("control.php",{
        method: "POST",
        action: state,
    }).then(response =>{
        if (!response.ok) {
            throw new Error(`Response status: ${response.status}`);
          }
    }).then(res => {
        
    }
    )
}