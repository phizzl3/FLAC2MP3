# FLAC2MP3
Convert .FLAC files in a folder to MP3 with metadata using ffmpeg and Python on MacOS.  

Convert .flac to .mp3 with ffmpeg, keeping all metadata  

ffmpeg -i input.flac -ab 320k -map_metadata 0 -id3v2_version 3 output.mp3
