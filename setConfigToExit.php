<?php
echo "Set Configuration to Exit\n";

$command = escapeshellcmd('sudo -u www-data python /var/www/setConfigToExit.py');
$output = shell_exec($command);
echo nl2br($output);
?>
