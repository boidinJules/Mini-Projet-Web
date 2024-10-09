<?php
if (isset($_POST['color'])) {
    $color = explode(",",$_POST['color']);

    $R = $color[0];
    $G = $color[1];
    $B = $color[2];
    $command = `curl -X POST -H "Content-Type: application/json" -d '{"R":$R,"G":$G,"B":$B}' http://localhost:8080/`; 
    
    $res = exec("sudo -u www-data $command ");
   

    echo($res);
}
?>
