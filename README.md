# GstreamerAudioVideoConcat

##### Concatenate video/audio files using Gstreamer Editing Service (gst-editing-services)
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
1. Concatenate video/audio files:
   - Prepare input: Copy *video/audio files* you want to concatenate into the same folder <input folder>
   - Run app:
     ```
     $ python MediaConcat.py <input folder> <output file path>
     ```
2. Create video from one still image and multiple audio files:
   - Prepare input: Copy *image file and audio files* you want to concatenate into the same folder <input folder>
   - Run app:
     ```
     $ python MediaConcat.py <input folder> <output file path>
     ```  
3. Note: Output video is in .ogv format (other formats are not supported at this moment)
