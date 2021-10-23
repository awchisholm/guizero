
import cv2
import glob
import os
import shutil
from PIL import Image

# Open the vidoe
cap = cv2.VideoCapture('InstallVirtualBox.webm')

# Read all the frames of the video and make a jpg image of each
i=0
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == False:
        break
    cv2.imwrite('videos/tester'+str(i)+'.jpg',frame)
    i+=1

cap.release()
cv2.destroyAllWindows()

# Find all the jpg images and make a list 
jpgs = 'videos/*.jpg'
img, *imgs = [Image.open(f) for f in sorted(glob.glob(jpgs))]
# Append every 100th image to the first one to make an animated gif
img.save(fp='videos/animation.gif', format='GIF', append_images=imgs[::100], save_all=True, duration=200, loop=0)