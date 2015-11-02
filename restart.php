<?php
echo "Restarting RaspberryPi";

$command = escapeshellcmd('sudo -u www-data python /var/www/restart.py');
$output = shell_exec($command);
echo nl2br($output);
?>
