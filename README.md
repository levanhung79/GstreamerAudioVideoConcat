# GstreamerAudioVideoConcat

Concatenate audio/video/image files into one using Gstreamer Editing Service (gst-editing-services)

Prerequisites:
Ubuntu 16.04 or higher

Environment installation:
1. Install Gstreamer Editing Service:
$ sudo apt-get update
$ sudo apt-get -y upgrade
$ sudo apt-get install libgstreamer1.0-0 gstreamer1.0-plugins-base gstreamer1.0-plugins-good gstreamer1.0-plugins-bad gstreamer1.0-plugins-ugly gstreamer1.0-libav gstreamer1.0-doc gstreamer1.0-tools gstreamer-editing-services1.0
  
2. Check python version
$ python3 -V
  
3. Install MediaInfo
$ sudo apt-get install mediainfo
  
Run app:
1. Prepare input: Copy videos, audios, image you want to concatenate into the same folder <input folder>

2. Run app:
$ python3 MediaConcat.py <input folder> <output file path>
  
3. Note:
a. If <input folder> contains only video files or video files and audio files, app concatenates these files to create output video (in .ogv format).
b. If <input folder> contains audio files and ONLY one image, app concatenates these audio files and combine with image file to create output video (in .ogv format).
