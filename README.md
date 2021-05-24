# FLAC2MP3

Convert .FLAC files in a folder to MP3 with metadata using ffmpeg and Python 
on MacOS.  

* Asks for a folder via drag and drop
* Recursively searches that folder for FLAC files and generates a list
* Uses a terminal command to call ffmpeg to convert the FLAC file to mp3
* Saves new mp3 file in same directory as located FLAC file

## Requirements

* MacOS (Might work on Linux...haven't messed with that just yet.)
* ffmpeg (brew install ffmpeg)
