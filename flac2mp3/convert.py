#!/usr/bin/env python3

import dropfile
import re_file_search
import subprocess
import time


def get_folder():
    return dropfile.get()


def get_source_files(sf):
    return re_file_search.get_list(sf, r".+\.[fF][lL][aA][cC]$")


def convert_files(fl):
    
    # Loop through each file in the list.
    for each in fl:
        
        # Set a new variable for the source and clean characters that need
        # to be escaped for MacOS/Linux.
        source = str(each)
        for fnd, rplc in {" ": "\ ", "'": "\\'", "(": "\\(", ")": "\\)",
                          "[": "\\[", "]": "\\]", "{": "\\{", "}": "\\}",
                          }.items():
            source = source.replace(fnd, rplc)
        
        # Set a target filename by just replacing the extension.
        target = source.replace(".flac", ".mp3")
        
        # Send the terminal command to ffmpeg to do the conversion.
        subprocess.run(f"ffmpeg -i {source} -ab 320k {target}", shell=True)


def main():
    source_folder = get_folder()
    flac_list = get_source_files(source_folder)
    if flac_list:
        print(f"\n{len(flac_list)} files found.\n")
        time.sleep(1)
        convert_files(flac_list)
        print("\nAll done.")
        time.sleep(3)
    else:
        print("\nNo matching files found.\nDouble check that your path"
              " matches when dropped. (check extra characters, etc.)")


if __name__ == '__main__':
    main()
    