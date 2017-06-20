#!/usr/bin python

import sys

print "Number of arguments: " + str(len(sys.argv))
print "Argument List: " + str(sys.argv)
print "\n"

#f = open('/home/pi/background_substraction/outfile.txt', 'a')
#f.write('Hello World\n')
#f.close()

class Config:
	runMode = ''
	active_time_start_h = ''
	active_time_start_m = ''
	active_time_stop_h = ''
	active_time_stop_m = ''
	php_script = ''
	image_folder_root = ''
	

def readConfigFile():
	CONFIG_FILE = '/var/www/surveillance_config.txt'
	linestring = open(CONFIG_FILE, 'r').read()
	begPos = linestring.find('RUN_MODE')
	begPos = linestring.find('#', begPos) + 1
	endPos = linestring.find('#', begPos)
	runMode = linestring[begPos:endPos]
	begPos = linestring.find('ACTIVE_TIME_START_HOUR')
	begPos = linestring.find('#', begPos) + 1
	endPos = linestring.find('#', begPos)
	active_time_start_h = linestring[begPos:endPos]
	begPos = linestring.find('ACTIVE_TIME_START_MINUTES')
	begPos = linestring.find('#', begPos) + 1
	endPos = linestring.find('#', begPos)
	active_time_start_m = linestring[begPos:endPos]
	begPos = linestring.find('ACTIVE_TIME_STOP_HOUR')
	begPos = linestring.find('#', begPos) + 1
	endPos = linestring.find('#', begPos)
	active_time_stop_h = linestring[begPos:endPos]
	begPos = linestring.find('ACTIVE_TIME_STOP_MINUTES')
	begPos = linestring.find('#', begPos) + 1
	endPos = linestring.find('#', begPos)
	active_time_stop_m = linestring[begPos:endPos]
	begPos = linestring.find('PHP_SCRIPT')
	begPos = linestring.find('#', begPos) + 1
	endPos = linestring.find('#', begPos)
	php_script = linestring[begPos:endPos]
	begPos = linestring.find('IMAGE_FOLDER_ROOT')
	begPos = linestring.find('#', begPos) + 1
	endPos = linestring.find('#', begPos)
	image_folder_root = linestring[begPos:endPos]

	print "runMode = %s" %runMode
	print "active_time_start_h = %s" %active_time_start_h
	print "active_time_start_m = %s" %active_time_start_m
	print "active_time_stop_h = %s" %active_time_stop_h
	print "active_time_stop_m = %s" %active_time_stop_m
	print "php_script = %s" %php_script
	print "image_folder_root = %s" %image_folder_root
	
	config = Config()
	config.runMode = runMode
	config.active_time_start_h = active_time_start_h
	config.active_time_start_m = active_time_start_m
	config.active_time_stop_h = active_time_stop_h
	config.active_time_stop_m = active_time_stop_m
	config.php_script = php_script
	config.image_folder_root = image_folder_root
	return config
	
import fileinput
#use this method because it does not change permission
def replace(file,searchExp,replaceExp):
    found = False
    for line in fileinput.input(file, inplace=1):
        if(searchExp in line):
            if(not found):
                line = line.replace(searchExp,replaceExp)
                found = True
        sys.stdout.write(line)
        

print "old Config:"
c = readConfigFile()
#print sys.argv[1]
#print sys.argv[2]
#print sys.argv[3]
#print sys.argv[4]
#print sys.argv[5]


replace('/var/www/surveillance_config.txt', c.runMode, 'Active')


print "\nnew Conig:"
c = readConfigFile()

