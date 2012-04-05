# photo-enhancer.py
# Author: T Shrinivasan tshrinivasan@gmail.com
# Required software: Ubuntu 12.04 or above, gthumb, ldtp, python-ldtp


import os,sys
from ldtp import *


def enhance(image):
	print "Working on the Image " + image

        launchapp('gthumb', [image])
        waittillguiexist ('*-gthumb')
        click('frm*gThumb','tbtnEdit')
        click('frm*gThumb', 'btnEnhanceColors')
        wait(3)
        click('frm*gThumb', 'btnSave')
        generatekeyevent ('<ctrl>q')




path = './'

listing = os.listdir(path)

def filetype(file):
        return file.split(".")[-1]

def filename(file):
        return file.split(".")[-2]

for photo in listing:
        if filetype(photo) in ['JPG','jpg','GIF','gif','png','PNG']:
                enhance(photo)





