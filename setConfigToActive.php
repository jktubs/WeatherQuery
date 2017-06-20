<?php
echo "Set Configuration to Active\n";

$command = escapeshellcmd('sudo -u www-data python /var/www/setConfigToActive.py');
$output = shell_exec($command);
echo nl2br($output);
?>
