
# [YouTube Downloader]
# Made by @austinyen56
# Allows you to download music from most streaming services (YT, SoundCloud... etc) in multiple formats(mp3, wav, flac)
# Supports thumbnail embedding for mp3 option only

# - Requires yt-dlp to be installed (python -m pip install -U yt-dlp)
# - Must download and add ffmpeg.exe in 'C:\Users\<Name>\AppData\Local\Programs\Python\Python3<ver>\Scripts' in addition with the ffmpeg library

import os
import sys

url = str(input("Enter URL: ")).split("&ab_channel")[0]
# Can change --audio-format to wav if needed

def windows():
    
    while True:
        fmt = str(input("In what format (flac/wav/mp3[support thumbnail embedding]): "))
        if fmt == "wav" or fmt == "flac":
            cmd = "yt-dlp -i -x --audio-format "+ fmt +" --audio-quality 0 -o %UserProfile%/Desktop/YoutubeDL_Downloads/%(title)s.%(ext)s"
            break
        elif fmt == "mp3":
            cmd = f"yt-dlp -i -x --audio-format "+ fmt +" --embed-thumbnail --postprocessor-args \"-write_id3v1 1 -id3v2_version 3\" --audio-quality 0 -o %UserProfile%/Desktop/YoutubeDL_Downloads/%(title)s.%(ext)s"
            break
        else:
            print("Invalid format, try again: ")
    
    return cmd

def linux():
    while True:
        fmt = str(input("In what format (flac/wav/mp3[support thumbnail embedding]): "))
        output_dir = os.path.join(os.path.expanduser("~"), "/mnt/c/Users/Austin/Desktop/ytdownloader")
        if fmt == "wav" or fmt == "flac":
            cmd = f"yt-dlp -i -x --audio-format {fmt} --audio-quality 0 -o '{output_dir}/%(title)s.%(ext)s'"
            break
        elif fmt == "mp3":
            cmd = f"yt-dlp -i -x --audio-format {fmt} --embed-thumbnail --postprocessor-args \"-write_id3v1 1 -id3v2_version 3\" --audio-quality 0 -o '{output_dir}/%(title)s.%(ext)s'"
            break
        else:
            print("Invalid format, try again: ")
    return cmd


if sys.platform == "win32":
    cmd = windows()
    cmdurl = cmd + " " + url
    # print("Running: ",cmdurl)
    if os.system(cmdurl) == 0:
        input("Successfully downloaded, hit ENTER to exit... ")
        exit(0)
    else:
        input("Error downloading, check above for details, hit ENTER to exit... ...")
        exit(1)
    

if sys.platform == "linux":
    cmd = linux()
    cmdurl = cmd + " " + url
    # print("Running: ",cmdurl)
    if os.system(cmdurl) == 0:
        input("Successfully downloaded, hit ENTER to exit... ")
        exit(0)
    else:
        input("Error downloading, check above for details, hit ENTER to exit... ...")
        exit(1)

else:
    print("OS not supported, you have a weird OS bruh\n")


#cmd = "youtube-dl -i -x --audio-format "+ fmt +" --embed-thumbnail --postprocessor-args \"-write_id3v1 1 -id3v2_version 3\" --audio-quality 0 -o C:/Users/Austin/Desktop/ref/%(title)s.%(ext)s"
