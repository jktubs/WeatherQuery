<?php
echo "Starting Surveillance Application";

$command = escapeshellcmd('sudo -u www-data python /var/www/image_observation_refactored.py');
$output = shell_exec($command);
#echo nl2br($output);
?>
