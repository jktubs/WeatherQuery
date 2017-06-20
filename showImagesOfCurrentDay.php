

<?php
$serverIP = $_SERVER['SERVER_ADDR'];
$currentDay = "2017-06-12";
echo nl2br("Today: ".$currentDay."\n");
echo nl2br("\nServer:".$serverIP);
$dirPathRoot = "images"; 
$files = array();
$dir = "/var/www/".$dirPathRoot."/".$currentDay."/";
$dirIterator = new DirectoryIterator($dir);
foreach ($dirIterator as $fileinfo) {
    #echo  nl2br ("\n".$fileinfo." _ ".$fileinfo->getMTime()."\n");
    #$files[$fileinfo->getMTime()] = $fileinfo->getFilename();
    $files[$fileinfo->getFilename()] = $fileinfo->getFilename();
}

ksort($files);

foreach($files as $file)
{
   $currentFile = $dir . $file;
   echo nl2br ("\n".$file. " >>> " . date ("F d Y H:i:s.", filemtime($currentFile)). "\n");
   echo "<img src=\"http://".$serverIP."/".$dirPathRoot."/".$currentDay."/".$file."\" align=middle>";
}
?>
