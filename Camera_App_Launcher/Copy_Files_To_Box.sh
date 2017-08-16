cd /
cd /var/www

IN_DIRECTORY="/var/www/images/$(date +\%Y-\%m-\%d)"
BOX_DIRECTORY="/media/JENS_KRAMER/box"
OUT_DIRECTORY="/media/JENS_KRAMER/box/Surveillance_Images/$(date +\%Y-\%m-\%d)"
IN_CHRONLOGS_DIRECTORY="/home/pi/Desktop/Camera_App_Launcher/Logs"
OUT_CHRONLOGS_DIRECTORY="/media/JENS_KRAMER/box/Surveillance_Images/CronLogs"

#sudo mount $BOX_DIRECTORY
#sudo mkdir $OUT_DIRECTORY
#sudo python copyFilesToBox.py $IN_DIRECTORY $OUT_DIRECTORY
#sudo mkdir $CHRONLOGSDIR
#sudo python copyFilesToBox.py $IN_CHRONLOGS_DIRECTORY $OUT_CHRONLOGS_DIRECTORY
#sleep 1m
#sudo umount $BOX_DIRECTORY
cd /