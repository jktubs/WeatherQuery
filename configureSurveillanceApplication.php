<?php
$RunMode = $_POST["RunMode"];
$StartTimeH = $_POST["StartTimeH"];
$StartTimeM = $_POST["StartTimeM"];
$StopTimeH = $_POST["StopTimeH"];
$StopTimeM = $_POST["StopTimeM"];

if (!isset($_POST['submit'])) { // if page is not submitted to itself echo the form
?>
<html>
<head>
<!--
http://www.tizag.com/phpT/examples/formfinale.php
-->
<title>Configuration Surveillance Application</title>
</head>
<body>
<form method="post" action="<?php echo $PHP_SELF;?>">
<!--
RUN_MODE:<input type="text" size="12" maxlength="36" name="RunMode"><br />
-->
Select RUN_MODE:<br />
<select name="RunMode" size="3">
<option value="Active">Active</option>
<option value="Idle">Idle</option>
<option value="Exit">Exit</option></select><br />

Select Hour of Start Time:<br />
<select name="StartTimeH">
<option value="00">00</option>
<option value="01">01</option>
<option value="02">02</option>
<option value="03">03</option>
<option value="04">04</option>
<option value="05">05</option>
<option value="06">06</option>
<option value="07">07</option>
<option value="08">08</option>
<option value="09">09</option>
<option value="10">10</option>
<option value="11">11</option>
<option value="12">12</option>
<option value="13">13</option>
<option value="14">14</option>
<option value="15">15</option>
<option value="16">16</option>
<option value="17">17</option>
<option value="18">18</option>
<option value="19">19</option>
<option value="20">20</option>
<option value="21">21</option>
<option value="22">22</option>
<option value="23">23</option>
</select><br />
Select Minutes of Start Time:<br />
<select name="StartTimeM">
<option value="00">00</option>
<option value="05">05</option>
<option value="10">10</option>
<option value="15">15</option>
<option value="20">20</option>
<option value="25">25</option>
<option value="30">30</option>
<option value="35">35</option>
<option value="40">40</option>
<option value="45">45</option>
<option value="50">50</option>
<option value="55">55</option>
</select><br />

Select Hour of Stop Time:<br />
<select name="StopTimeH">
<option value="00">00</option>
<option value="01">01</option>
<option value="02">02</option>
<option value="03">03</option>
<option value="04">04</option>
<option value="05">05</option>
<option value="06">06</option>
<option value="07">07</option>
<option value="08">08</option>
<option value="09">09</option>
<option value="10">10</option>
<option value="11">11</option>
<option value="12">12</option>
<option value="13">13</option>
<option value="14">14</option>
<option value="15">15</option>
<option value="16">16</option>
<option value="17">17</option>
<option value="18">18</option>
<option value="19">19</option>
<option value="20">20</option>
<option value="21">21</option>
<option value="22">22</option>
<option value="23">23</option>
</select><br />
Select Minutes of Stop Time:<br />
<select name="StopTimeM">
<option value="00">00</option>
<option value="05">05</option>
<option value="10">10</option>
<option value="15">15</option>
<option value="20">20</option>
<option value="25">25</option>
<option value="30">30</option>
<option value="35">35</option>
<option value="40">40</option>
<option value="45">45</option>
<option value="50">50</option>
<option value="55">55</option>
</select><br />
<br />
<input type="submit" value="submit" name="submit">
<br />
<br />
<a href="startSurveillanceApplicationThreadBased.php">StartSurveillance Application Thread-Based</a>
<br />
<br />
<!--<a href="startSurveillanceApplication.php">StartSurveillance Application (old)</a>-->
<a href="setConfigToExit.php">Set Configuration to Exit</a>
<br />
<br />
<a href="setConfigToActive.php">Set Configuration to Active</a>
<br />
<br />
<br />
<a href="showImagesOfCurrentDay.php">Show All Images of the current Day</a>
<br />
<br />
<a href="/images">Image Folder</a>
<br />
<br />
<br />
<br />
<a href="takeAPicture.php">Grab and Display current Image</a>
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<a href="restart.php">Restart my Pi</a>
<br />
<br />
<a href="shutdown.php">Shutdown my Pi</a>
</form>
<?
} else {
echo "RUN_MODE is ".$RunMode.".<br />";
echo "Start Hour: ".$StartTimeH.".<br />";
echo "Start Minutes: ".$StartTimeM.".<br />";
echo "Stop Hour: ".$StopTimeH.".<br />";
echo "Stop Minutes: ".$StopTimeM.".<br />";


#http://stackoverflow.com/questions/31811253/execute-python-script-from-php
$command = escapeshellcmd('sudo -u www-data python /var/www/configure.py '.$RunMode.' '.$StartTimeH.' '.$StartTimeM.' '.$StopTimeH.' '.$StopTimeM.' ');
$output = shell_exec($command);
echo nl2br($output);

}
?>