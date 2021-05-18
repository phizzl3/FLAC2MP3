#!/usr/bin/env python3

import dropfile
import re_file_search
import subprocess


def get_folder():
    return str(dropfile.get())


def get_source_files(sf):
    return re_file_search.get_list(sf, r".+\.[fF][lL][aA][cC]$")


def convert_files(fl):
    for each in fl:
        subprocess.run(f"ffmpeg -i {each} -ab 320k {each.parent}{each.name}.mp3",
                       shell=True)


def main():
    source_folder = get_folder()
    flac_list = get_source_files(source_folder)
    if flac_list:
        convert_files(flac_list)
    else:
        print("No matching files found.")


if __name__ == '__main__':
    main()
    