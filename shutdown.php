<?php
echo "Shutdown RaspberryPi";

$command = escapeshellcmd('sudo -u www-data python /var/www/shutdown.py');
$output = shell_exec($command);
echo nl2br($output);
?>
