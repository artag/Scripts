# For files batch convertation
# 1. Converts pairs of video (*.ts) and audio (*.aac) files in selected directory to *.mp4 file.
# 2. File pairs *.ts and *.aac must have identical names.
# Usage:
# py convert.py <directory_with_files>

import sys
import os
import subprocess

from msvcrt import getch
from os import *


def check_args():
    if (len(sys.argv) != 2):
        print("Usage: convert.py path")
        return False

    path = sys.argv[1]

    if (not os.path.exists(path)):
        print(path, "does't exists")
        return False

    if (not os.path.isdir(path)):
        print(path, "is not a directory")
        return False

    return True


def get_files(pathname):
    f = []
    for (dirpath, dirnames, filenames) in walk(pathname):
        f.extend(filenames)
        break
    
    return f


def get_files_by_pairs(files):
    video = []
    audio = []
    
    for file in files:
        filename = os.path.splitext(file)[0]
        extension = os.path.splitext(file)[1]

        if (extension == ".ts"):
            video.append(file)
        elif (extension == ".aac"):
            audio.append(file)

    return list(zip(video, audio))


def display_file_pairs(pairs):
    for pair in pairs:
        print(pair[0] + "\n" + pair[1] + "\n\n")


def display_question():
    print("Do you want process these files?" + "\n" +
          "Press Enter to continue or press other keys to quit")
    
    key = ord(getch())
    if key == 13:    #Enter
        return True
    else:
        return False


def process_pairs(pairs):
    for pair in pairs:
        filename = os.path.splitext(pair[0])[0]
        filename_with_extension = filename + ".mp4"
        subprocess.call(["ffmpeg", "-i", pair[0], "-i", pair[1], filename_with_extension])


def main():
    input_success = check_args()
    if (not input_success):
        exit()
    
    path = sys.argv[1]
    filenames = get_files(path)

    pairs = get_files_by_pairs(filenames)
    display_file_pairs(pairs)
    
    answer = display_question()
    if (answer is True):
        process_pairs(pairs)


if __name__ == "__main__":
    main()
