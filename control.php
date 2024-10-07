<?php
if (isset($_POST['action'])) {
    $action = escapeshellarg($_POST['action']);
    if ($action == "'on'") {
        $command = "/usr/bin/python3 /var/www/html/Mini-Projet-Web/led_control.py on"; 
    } else {
        $command = "/usr/bin/python3 /var/www/html/Mini-Projet-Web/led_control.py off"; 
    }


    $res = exec("sudo -u www-data $command ");
    include( 'MyButon.html' );
    $image = ($res == 'on') ? 'images/led_on.jpg' : 'images/led_off.jpg';
    echo($res);
}
?>
