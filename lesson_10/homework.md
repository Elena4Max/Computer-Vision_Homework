## Homework 10

In this homework, I am going to use and compare three different trackers - MIL, KCF, CSRT - and compare the results.

### Coding
I uploaded a video of the road with cars and tried to track the car in front. Before tracking, I start cutting the video into frames.
Further, as in the example from the lecture, I indicate the coordinates of what to track for the first frame.
Then I set up the tracker, set the template, and initialize it. Next, in a loop, I perform tracking.

### Experiment with tracker MIL
The algorithm tracks the object well, but has a relatively low speed. It is not possible to stop tracking when the object is lost, and the box does not change size when the tracking object approaches.
<p align="center">
  <img align="center" src="https://github.com/Elena4Max/Computer-Vision_Homework/tree/main/lesson_10/data/MIL-2023-07-02_19.26.04.gif" alt="demo"/>
</p>

### Experiment with tracker KCF
The algorithm tracks the object well. Unlike MIL, it stops tracking when the object is lost, but the box also does not change size when the tracking object approaches.
<p align="center">
  <img align="center" src="https://github.com/Elena4Max/Computer-Vision_Homework/tree/main/lesson_10/data/KCF-2023-07-02_19.27.13.gif" alt="demo"/>
</p>

### Experiment with tracker CSRT
The algorithm seems to be similar to MIL.
<p align="center">
  <img align="center" src="https://github.com/Elena4Max/Computer-Vision_Homework/tree/main/lesson_10/data/CSRT-2023-07-02_19.28.13.gif" alt="demo"/>
</p>

### Step 6
Compare the results:
* Do you see any differences? If so, what are they?

MIL
- Shows fairly good accuracy
- Relatively low speed and the impossibility of stopping tracking when the object is lost.

KCF
- Sufficiently high speed and accuracy, stops tracking when the tracked object is lost.
- Inability to continue tracking after the loss of the object.

CSRT
- Among the previous algorithms it shows comparatively better accuracy, resistance to overlapping by other objects.
- Sufficiently low speed, an unstable operation when the object is lost.

* Does one tracker perform better than the other? In what way?

I like the result of the KCF algorithm the most. It seems logical to me to stop tracking an object that has ceased to be in the field of view.

P.S. can not submit video to github due to size limit. Link provided:
https://www.pexels.com/video/traveling-a-road-built-on-mountain-sides-3055764/
