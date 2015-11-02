<?php
echo "Starting Surveillance Application";

$command = escapeshellcmd('sudo -u www-data python /home/pi/background_substraction/image_observation_refactored.py');
$output = shell_exec($command);
#echo nl2br($output);
?>
