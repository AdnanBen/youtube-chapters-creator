import glob, os
from pymediainfo import MediaInfo

"""
Youtube Chapters Generator
"""

def msFormatter(x):
    x = x/1000
    hrs = int(x // 3600)
    x = x - (hrs * 3600)
    mins = int(x // 60)
    x = x - (mins * 60)
    secs = int(x)
    return (str((hrs if hrs else 0)) + ':' + str((mins if mins>=10 else ('0' + str(mins) if mins else '00'))) 
    + ':' + str((secs if secs>=10 else ('0' + str(secs) if secs else '00'))))


def main():
    print("hello world")
    running_total = 0
    for file in glob.glob("*.mp4"):
        media_info = MediaInfo.parse(file)
        dur = media_info.tracks[0].duration
        print(msFormatter(running_total) + ' ' + file[:-4])
        running_total += dur



if __name__ == "__main__":
    main()