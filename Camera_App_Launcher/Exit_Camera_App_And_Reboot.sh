cd /
cd /var/www
sudo python setConfigToExit.py
echo "setConfigToExit DONE"
sleep 20

IN_DIRECTORY="/var/www/images/$(date +\%Y-\%m-\%d)"
BOX_DIRECTORY="/media/JENS_KRAMER/box"
OUT_DIRECTORY="/media/JENS_KRAMER/box/Surveillance_Images/$(date +\%Y-\%m-\%d)"
IN_CHRONLOGS_DIRECTORY="/home/pi/Desktop/Camera_App_Launcher/Logs"
OUT_CHRONLOGS_DIRECTORY="/media/JENS_KRAMER/box/Surveillance_Images/CronLogs"

#sudo mount $BOX_DIRECTORY
sudo mkdir $OUT_DIRECTORY
sudo python copyFilesToBox.py $IN_DIRECTORY $OUT_DIRECTORY
sudo mkdir $OUT_CHRONLOGS_DIRECTORY
sudo python copyFilesToBox.py $IN_CHRONLOGS_DIRECTORY $OUT_CHRONLOGS_DIRECTORY
sleep 90m
#sudo umount $BOX_DIRECTORY
echo "sleep DONE. Now reboot the PI."
sudo python restart.py
cd /