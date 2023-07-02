#!/usr/bin/env python3
import os
import cv2
from matplotlib import pyplot as plt

folder = '/home/elena/cv/Computer-Vision_Homework/lesson_10/data/'
vidcap = cv2.VideoCapture(folder + 'video.mp4')
success,image = vidcap.read()
count = 0

while success:
    lead_zero = ""
    if count < 1000 :
        if count < 100 :
            if count < 10 :
                lead_zero += "0"
            lead_zero += "0"
        lead_zero += "0"
    cv2.imwrite(lead_zero + "%d.jpg" % count, image)     # save frame as JPEG file      
    success,image = vidcap.read()
    print('Read a new frame: ', success)
    count += 1
  
# Load the dataset
frames = os.listdir(folder)

# Sort (alphabetically) to ensure temporal consecutiveness
frames.sort()

idx = frames.index('0000.jpg')

# Let's assume the detector has detected two vehicles with the following bounding boxes
x1, y1 = 2070, 570
x2, y2 = 2250, 720

width = x2 - x1
height = y2 - y1

# Set up tracker
tracker_types = ['MIL','KCF', 'CSRT']
tracker_type = tracker_types[1]

if tracker_type == 'MIL':
    tracker = cv2.TrackerMIL_create() 
if tracker_type == 'KCF':
    tracker = cv2.TrackerKCF_create()
if tracker_type == "CSRT":
    tracker = cv2.TrackerCSRT_create()

# Genrate tracking template
img = cv2.imread(os.path.join(folder, frames[idx]))
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Initialize tracker
bbox = (x1, y1, width, height)
ok = tracker.init(img, bbox)

# Tracking loop
for ii in range(idx, idx + 1000, 20):
    img = cv2.imread(os.path.join(folder, frames[ii]))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)    
        
    ok, bbox = tracker.update(img)
            
    # Show the tracker working
    x1, y1 = bbox[0], bbox[1]
    width, height = bbox[2], bbox[3]
    cv2.rectangle(img, (x1, y1), (x1+width, y1+height), (255, 0, 0), 10)
    plt.imshow(img)
    plt.show(), plt.draw()    
    plt.waitforbuttonpress(0.1)
    plt.clf()

        
