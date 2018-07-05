# GstreamerAudioVideoConcat

##### Concatenate video files using Gstreamer Editing Service (gst-editing-services)
##### Create video from one still image and multiple audio files using Gstreamer Editing Service (gst-editing-services)

### Prerequisites:
Ubuntu 16.04 or higher

### Environment installation:
1. Install Gstreamer Editing Service:
```
$ sudo apt-get update && sudo apt-get -y upgrade && sudo apt-get install sudo apt-get install sudo apt-get install libgstreamer1.0-0 gstreamer1.0-plugins-base gstreamer1.0-plugins-good gstreamer1.0-plugins-bad gstreamer1.0-plugins-ugly gstreamer1.0-libav gstreamer1.0-doc gstreamer1.0-tools ges1.0-tools libges-1.0-0 libges-1.0-dev python-pip
```

2. Install MediaInfo:
```
$ sudo apt-get install mediainfo && pip install pymediainfo
```
  
### Run app:
1. Prepare input: Copy videos, audios, image you want to concatenate into the same folder <input folder>

2. Run app:
```
$ python MediaConcat.py <input folder> <output file path>
```
  
3. Note:
   - If <input folder> contains only video files or video files and audio files, app concatenates these files to create output video (in .ogv format).
   - If <input folder> contains audio files and ONLY one image, app concatenates these audio files and combine with image file to create output video (in .ogv format).
