<?php
echo "Starting Surveillance Application";

$command = escapeshellcmd('sudo -u www-data python /var/www/image_observation_threading_and_stream.py');
$output = shell_exec($command);
#echo nl2br($output);
?>
