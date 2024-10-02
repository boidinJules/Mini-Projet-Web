<?php
// Vérifie si l'action a été envoyée via une requête POST
if (isset($_POST['action'])) {
    // Récupère l'action choisie par l'utilisateur (on ou off)
    $action = escapeshellarg($_POST['action']); // Sécurise l'argument pour éviter les injections
    // Définit la commande pour exécuter le script Python avec l'argument approprié
    if ($action == "'on'"){
    $command = "python3 /var/www/html/Mini-Projet-Web/led_control.py on"; 
    }
    else{
    $command = "python3 /var/www/html/Mini-Projet-Web/led_control.py off"; 
    }

    // Exécute la commande shell
    $shell = shell_exec($command); // Appelle le script Python pour allumer ou éteindre la LED
    echo($shell);
}
?>
