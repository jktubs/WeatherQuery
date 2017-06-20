#!/usr/bin python

print "\nTaking a picture ... "

#https://www.raspberrypi.org/documentation/usage/camera/python/README.md

import picamera

try:
    camera = picamera.PiCamera()
    camera.resolution = (2592, 1944) #default: 1920x1080
    #camera.resolution = (1920, 1080)
    camera.framerate = 30
    camera.capture('/var/www/images/currentImage/currentImage.jpg')

finally:
    print "finally camera.close()"
    camera.close()