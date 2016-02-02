<html>
<head>
</head>
<body>
<ul> 
<?php
$command = escapeshellcmd('sudo -u www-data python /var/www/takeAPicture.py');
$output = shell_exec($command);
echo nl2br($output);

header("Location: showCurrentImage.php");
die();
?>
</ul>
</body>
</html>