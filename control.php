<?php
if (isset($_POST['color'])) {
    $color = explode(",",$_POST['color']);

    $R = $color[0];
    $G = $color[1];
    $B = $color[2];
    $command = "/usr/bin/python3 led_control.py $R $G $B"; 
    
    $res = exec("sudo -u www-data $command ");
   

    echo($res);
}
?>
