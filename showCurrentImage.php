<?php
$serverIP = $_SERVER['SERVER_ADDR'];
echo nl2br("Server: ".$serverIP."\n\n");
$now = date('l jS \of F Y h:i:s A');
echo nl2br("Now: ".$now."\n\n");
echo "<img src=\"http://".$serverIP."/images/currentImage/currentImage.jpg\" align=middle>";
?>
