<?php
if (isset($_POST['color'])) {
    $action = escapeshellarg($_POST['color']);
    $command = "/usr/bin/python3 /var/www/html/Mini-Projet-Web/led_control.py $color"; 

    $res = exec("sudo -u www-data $command ");
   

    echo($res);
}
?>
