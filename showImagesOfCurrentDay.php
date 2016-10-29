

<?php
$serverIP = $_SERVER['SERVER_ADDR'];
$currentDay = "2016-10-27";
echo nl2br("Today: ".$currentDay."\n");
echo nl2br("\nServer:".$serverIP);
$dirPathRoot = "images"; 
$files = array();
$dir = new DirectoryIterator("/var/www/".$dirPathRoot."/".$currentDay."/");
foreach ($dir as $fileinfo) {
    #echo  nl2br ("\n".$fileinfo." _ ".$fileinfo->getMTime()."\n");
    #echo "<img src=\"http://192.168.178.30/".$dirPathRoot."/".$currentDay."/".$fileinfo->getFilename()."\" align=middle>";
    $files[$fileinfo->getMTime()] = $fileinfo->getFilename();
}

ksort($files);

foreach($files as $file)
{
   echo nl2br ("\n".$file."\n");
   echo "<img src=\"http://".$serverIP."/".$dirPathRoot."/".$currentDay."/".$file."\" align=middle>";
}
?>
