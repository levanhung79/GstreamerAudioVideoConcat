#!/usr/bin/python

import json
import os
import sys
import time
import shutil
import math
#https://mediaarea.net/en/MediaInfo/Download/Ubuntu
#sudo apt-get install mediainfo
from pymediainfo import MediaInfo

_MP3 = ".mp3"
_WAV = ".wav"
_OGG = ".ogg"
_M4A = ".m4a"
_WMA = ".wma"
_AUDIO_TAGS = [_MP3, _WAV, _OGG, _M4A, _WMA]

_MP4 = ".mp4"
_MKV = ".mkv"
_M4V = ".m4v"
_AVI = ".avi"
_WMV = ".wmv"
_VIDEO_TAGS = [_MP4, _MKV, _M4V, _AVI, _WMV]

_JPG = ".jpg"
_PNG = ".png"
_IMAGE_TAGS = [_JPG, _PNG]

_SPACE = " "
_GES_LAUNCH = "ges-launch-1.0"

class MediaConcater(object):    
    gesExist = False

    def __init__(self):
        self.gesExist = shutil.which(_GES_LAUNCH) is not None

    def ConcatMedia(self, folderPath, outputPath):
        if self.gesExist == False:
            print("Error: " + _GES_LAUNCH + " is not existed!")
            return False

        start_time = time.time()

        absFolderPath = os.path.abspath(folderPath)
        listFiles = os.listdir(folderPath)
        if len(listFiles) == 0:
            print("Error: Check again input folder.")
            return False

        # Parse videos in folder
        videoCount = 0
        command = _GES_LAUNCH + _SPACE
        listFiles.sort()
        totalLength = 0
        imageFile = ''
        for mfile in listFiles:
            fname = os.path.join(absFolderPath, mfile)
            fnameOnly = os.path.splitext(mfile)[0]
            if self.isVideoFile(mfile) or self.isAudioFile(mfile):
                length = self.getLength(fname) / 1000.0 - 0.001
                #length = round(length, 3)
                #length = math.ceil(length)
                videoStr = "+clip" + _SPACE + fname + _SPACE + "start=" + str(totalLength) + _SPACE + "duration=" + str(length) + _SPACE + "layer=" + str(videoCount) + _SPACE
                totalLength = totalLength + length
                command = command + videoStr
                videoCount = videoCount + 1
            if self.isImageFile(mfile):
                imageFile = fname
                
        if videoCount == 0:
            print("Error: There is no media file in input folder. Check again.")
            return False
            
        imageStr = "+clip" + _SPACE + imageFile + _SPACE + "start=0" + _SPACE + "duration=" + str(totalLength) + _SPACE + "layer=" + str(videoCount) + _SPACE

        absOutputFolderPath = os.path.abspath(outputPath)
        command = command + imageStr + "--outputuri=file:///" + absOutputFolderPath # + _SPACE + "--format=\"avimux:openh264enc,rate_control=2:audio/mpeg,mpegversion=4,bitrate=128000\""

        # Run ges-launch for merging videos
        os.system(command)

        print("Command: " + command)
        print("--- %s seconds ---" % (time.time() - start_time))
        return True

    def getLength(self, mediaPath):
        media_info = MediaInfo.parse(mediaPath)
        length = 0.0
        for track in media_info.tracks:
            if (track.track_type == 'Video') or (track.track_type == 'Audio'):
                #print(track.bit_rate + track.bit_rate_mode + track.codec + track.duration)
                #print(str(track.duration))
                length = track.duration
        #print(" -> mediaPath: " + mediaPath)
        #print(" -> Length: " + str(length))
        return length

    def isAudioFile(self, mediaPath):
        for tag in _AUDIO_TAGS:
            if mediaPath.endswith(tag):
                return True
        return False

    def isVideoFile(self, mediaPath):
        for tag in _VIDEO_TAGS:
            if mediaPath.endswith(tag):
                return True
        return False

    def isImageFile(self, mediaPath):
        for tag in _IMAGE_TAGS:
            if mediaPath.endswith(tag):
                return True
        return False

if __name__ == "__main__":
    start_time = time.time()

    if len(sys.argv) != 3:
        print("Usage: " + sys.argv[0] + " <video folder path> <output file path>")
    else:
        empl = MediaConcater()
        empl.ConcatMedia(sys.argv[1], sys.argv[2])

    print("--- Running time: %s seconds ---" % (time.time() - start_time))
