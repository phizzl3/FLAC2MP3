# FLAC2MP3

Convert .FLAC files in a folder to MP3 with metadata using ffmpeg and Python 
on MacOS.  

* Gets folder containing FLAC files
	* Checks to see if a folder location was passed via command line
	* Asks for a folder via user input/drag-and-drop if not passed
* Recursively searches that folder for FLAC files and generates a list
* Uses a terminal command to call ffmpeg to convert the FLAC file to mp3
* Saves new mp3 file in same directory as located FLAC file

## Requirements

* MacOS (Might work on Linux...haven't messed with that just yet.)
* ffmpeg (brew install ffmpeg)
