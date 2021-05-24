#!/usr/bin/env python3
"""
Gets a source folder and searches it for FLAC files. Converts FLAC files
to mp3 files in the same folder. 
"""
import subprocess
import time
from os import path
from pathlib import Path

import dropfile
import re_file_search


def get_folder() -> Path:
    """
    Get folder Path via drag and drop.

    Returns:
        pathlib.Path: Folder path to recursively search for files.
    """
    return dropfile.get()


def get_source_files(sf: Path) -> list:
    """
    Search for files ending in .FLAC/.flac and add them to a list.

    Args:
        sf (str/pathlib.Path): Folder location to search for files.

    Returns:
        list: List of file locations found to match .FLAC/.fladc.
    """
    return re_file_search.get_list(sf, r".+\.[fF][lL][aA][cC]$")


def convert_files(fl: list) -> None:
    """
    Loops through the list of located FLAC files and uses terminal/ffmpeg
    to convert them to mp3 files.

    Args:
        fl (list): List of file paths of located FLAC files. 
    """
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


def main() -> None:
    """
    Call all the functions to search for FLAC files and convert them to mp3.
    """
    # Get source folder
    source_folder = get_folder()
    # Search source folder for FLAC files and generate a list.
    flac_list = get_source_files(source_folder)
    # If the list of files isn't empty, show number found and convert
    # them to mp3.
    if flac_list:
        print(f"\n{len(flac_list)} files found.\n")
        time.sleep(1)
        # Convert FLAC files to mp3.
        convert_files(flac_list)
        print("\nAll done.")
        time.sleep(3)
    else:
        print("\nNo matching files found.\nDouble check that your path"
              " matches when dropped. (check extra characters, etc.)")


if __name__ == '__main__':
    main()
