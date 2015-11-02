#!/usr/bin python
from skimage import io
from skimage.data import data_dir
from skimage.util import img_as_ubyte
from skimage.util import img_as_int
import numpy
from skimage.morphology import erosion, dilation, opening, closing, white_tophat
from skimage.morphology import black_tophat, skeletonize, convex_hull_image
from skimage.morphology import disk
import time
import picamera
import os
import datetime
import fileinput
import sys

global today
today = datetime.date.today()
global thereWasADiff
global image0

#IMAGE_FOLDER_ROOT = r'O:/DATEN/_PRIVAT/backgroundSubstraction/images/'
#PHP_SCRIPT = 'O:/DATEN/_PRIVAT/backgroundSubstraction/showAllImages.php'
#PHP_SCRIPT = '/var/www/showAllImages.php'
#IMAGE_FOLDER_ROOT = '/var/www/images/test/'

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
    config = Config()
    linestring = open(CONFIG_FILE, 'r').read()
    begPos = linestring.find('RUN_MODE')
    begPos = linestring.find('#', begPos) + 1
    endPos = linestring.find('#', begPos)
    config.runMode = linestring[begPos:endPos]
    begPos = linestring.find('ACTIVE_TIME_START_HOUR')
    begPos = linestring.find('#', begPos) + 1
    endPos = linestring.find('#', begPos)
    config.active_time_start_h = linestring[begPos:endPos]
    begPos = linestring.find('ACTIVE_TIME_START_MINUTES')
    begPos = linestring.find('#', begPos) + 1
    endPos = linestring.find('#', begPos)
    config.active_time_start_m = linestring[begPos:endPos]
    begPos = linestring.find('ACTIVE_TIME_STOP_HOUR')
    begPos = linestring.find('#', begPos) + 1
    endPos = linestring.find('#', begPos)
    config.active_time_stop_h = linestring[begPos:endPos]
    begPos = linestring.find('ACTIVE_TIME_STOP_MINUTES')
    begPos = linestring.find('#', begPos) + 1
    endPos = linestring.find('#', begPos)
    config.active_time_stop_m = linestring[begPos:endPos]
    begPos = linestring.find('PHP_SCRIPT')
    begPos = linestring.find('#', begPos) + 1
    endPos = linestring.find('#', begPos)
    config.php_script = linestring[begPos:endPos]
    begPos = linestring.find('IMAGE_FOLDER_ROOT')
    begPos = linestring.find('#', begPos) + 1
    endPos = linestring.find('#', begPos)
    config.image_folder_root= linestring[begPos:endPos]
    print "runMode = %s" %config.runMode
    print "active_time_start_h = %s" %config.active_time_start_h
    print "active_time_start_m = %s" %config.active_time_start_m
    print "active_time_stop_h = %s" %config.active_time_stop_h
    print "active_time_stop_m = %s" %config.active_time_stop_m
    print "php_script = %s" %config.php_script
    print "image_folder_root = %s" %config.image_folder_root
    return config
    

def readInImage(path):
    image = img_as_int(io.imread(path, as_grey=True))
    #image = img_as_uint(io.imread(path, as_grey=True))
    return image
   
#use this method because it does not change permission
def replace(file,searchExp,replaceExp):
    for line in fileinput.input(file, inplace=1):
        if searchExp in line:
            line = line.replace(searchExp,replaceExp)
        sys.stdout.write(line)

def ensure_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
        updatePhpScript()
        return False
    else:
        return True
        
def updatePhpScript():
    global today
    linestring = open(PHP_SCRIPT, 'r').read()
    start = linestring.find('"') + 1
    end = linestring.find('"', start)
    yesterday = linestring[start:end] #letzter eingetragener Ordner
    today = datetime.date.today()
    print "replace %s in showAllImages_php by %s" %(str(yesterday), str(today))
    replace(PHP_SCRIPT,str(yesterday),str(today))
    

def getFolderSize(folder):
    total_size = os.path.getsize(folder)
    for item in os.listdir(folder):
        itempath = os.path.join(folder, item)
        if os.path.isfile(itempath):
            total_size += os.path.getsize(itempath)
        elif os.path.isdir(itempath):
            total_size += getFolderSize(itempath)
    return total_size
    
    
def wait(filename_current, filename_last):
    print"\n%s\n%s\n%s" %(time.ctime(), filename_current, filename_last)
    diffable = True
    
    if(os.path.isfile(filename_current)):
        print "Start imread current"
        start = time.clock()
        image1 = readInImage(filename_current)
        end = time.clock()
        print "End imread current: %.3f s" %(end-start)
    else:
        diffable = False
    
    if(not os.path.isfile(filename_last)):
        print "%s not found!" %filename_last
        diffable = False

    if(diffable):
        print "Start calculate diff"
        start = time.clock()
        diff = numpy.absolute(image1 - image0)
        end = time.clock()
        print "End calculate diff: %.3f s" %(end-start)
        selem = disk(3)
        
        #print "Start calc max"
        #max = numpy.amax(diff)
        #end = time.clock()
        #print "End calc max: %.3f s" %(end-start)
        
        print "Start thresholding"
        start = time.clock()
        low_values_indices = diff < 10000
        diff[low_values_indices] = 0
        end = time.clock()
        print "End thresholding: %.3f s" %(end-start)
        
        #print "Start calculate erosion"
        #start = time.clock()
        #eroded = erosion(diff, selem)
        #end = time.clock()
        #print "End calculate erosion: %.3f s" %(end-start)
        #sum = numpy.sum(eroded)
        sum = numpy.sum(diff)
        
        print "sum = %d" %sum
        global thereWasADiff
        if( sum < 10000000 ): #1000000
            
            if(os.path.isfile(filename_last) and thereWasADiff==False):
                print "Start removing last"
                start = time.clock()
                os.remove(filename_last)
                end = time.clock()
                print "End  removing last: %.3f s" %(end-start)
            
            thereWasADiff = False
        else:
            eroded_filename = filename_current.replace('.jpg','')+"_sum"+str(sum)+".jpg"
            print "Start saving diff"
            start = time.clock()
            #io.imsave(eroded_filename, eroded)
            io.imsave(eroded_filename, diff)
            end = time.clock()
            print "End saving diff:  %.3f s" %(end-start)
            thereWasADiff = True
                    
    global image0
    image0 = image1

try:
    #read in configuration file
    config = readConfigFile()
    PHP_SCRIPT = config.php_script
    IMAGE_FOLDER_ROOT = config.image_folder_root
    RUN_MODE = config.runMode
    runTimeBegin_h = int(config.active_time_start_h)
    runTimeBegin_m = int(config.active_time_start_m)
    runTimeEnd_h   = int(config.active_time_stop_h)
    runTimeEnd_m   = int(config.active_time_stop_m)
    
    camera = picamera.PiCamera()
    camera.resolution = (640, 480) #default: 1920x1080
    camera.framerate = 30
    #https://picamera.readthedocs.org/en/release-1.10/recipes1.html#consistent-capture
    
    CURRENT_IMAGE_FOLDER_PATH = IMAGE_FOLDER_ROOT + '%s/' %(datetime.date.today())
    ensure_dir(CURRENT_IMAGE_FOLDER_PATH)
    
    filename_last = CURRENT_IMAGE_FOLDER_PATH + 'X.jpg'
    
    global thereWasADiff
    thereWasADiff = False
    start_total = 0
    
    updatePhpScript()
    
    doExit = False
    while(not doExit):
        print "not doExit"
        for i, filename in enumerate(camera.capture_continuous(CURRENT_IMAGE_FOLDER_PATH+'image{counter:015d}.jpg')):
            print "filename: " + filename
            CURRENT_IMAGE_FOLDER_PATH = IMAGE_FOLDER_ROOT + '%s/' %(datetime.date.today())
            if( ensure_dir(CURRENT_IMAGE_FOLDER_PATH) == False ):
                print "break due to new folder" 
                break;
            end_total = time.clock()
            print "\n1 cycle took: %.3f s" %(end_total-start_total)
            start_total = time.clock()
            try:
                wait(filename, filename_last);
            except ValueError, e:
                f = open(CURRENT_IMAGE_FOLDER_PATH+'errorLog.txt', 'a')
                f.write('Error ocurred:\n')
                z = e
                f.write(z)
                f.close()
            except IOError, e:
                f = open(IMAGE_FOLDER_PATH+'/errorLog.txt', 'a')
                f.write('Error ocurred:\n')
                z = e
                f.write(z)
                f.close()
                
            filename_last = filename
            folderSize = getFolderSize(IMAGE_FOLDER_ROOT)
            print "folderSize = %d Bytes" %(folderSize)
            if(folderSize > 2000*1000000): #2000 MB
                doExit = True
                break;
            
            goOn = False
            while(not goOn):
                config = readConfigFile()
                RUN_MODE = config.runMode
                if(RUN_MODE == 'Exit'):
                    sys.exit()
                runTimeBegin_h = int(config.active_time_start_h)
                runTimeBegin_m = int(config.active_time_start_m)
                runTimeEnd_h   = int(config.active_time_stop_h)
                runTimeEnd_m   = int(config.active_time_stop_m)
                now = datetime.datetime.now()
                begin_time = datetime.datetime(now.year,now.month,now.day,runTimeBegin_h,runTimeBegin_m)
                end_time   = datetime.datetime(now.year,now.month,now.day,runTimeEnd_h,runTimeEnd_m)
                if( (now >= begin_time) and (now <= end_time) and (RUN_MODE == 'Active')):
                    goOn = True
                else:
                    print now
                    print " in IDLE mode"
                    time.sleep(2)

finally:
    print "finally camera.close()"
    camera.close()