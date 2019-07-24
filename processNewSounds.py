# Python code to rename sound effect files
# To run this:
# 1. Navigate to inside the folder containing the subfolders representing CD names.
# 2. Run this script from the command line by entering "python ../Add-New-SFX/processNewSounds.py"

import os
import re

#Rename track files
def renameTracks(origFolder):

    tracks = sorted(os.listdir("."))
    for track in tracks:
        if track.lower().endswith(".txt") or track.lower().endswith(".pdf"):
            os.remove(track)

        if track.lower().endswith(".aiff") or track.lower().endswith(".aif"):
            trackSplit = track.split(".")
            trackSplit[-1] = "wav"
            wavTrack = ".".join(trackSplit)
            os.system("ffmpeg -hide_banner -loglevel panic -n -i "+track+" "+wavTrack)

            # Remove original track once it has been converted to WAV
            # os.remove(track)
            track = wavTrack

        try:
            trackName = track.lower()
            trackDesc = track.split(".")
            trackDesc = trackDesc[:len(trackDesc)-1]
            trackDesc = " ".join(trackDesc)

            # Add description to a separate metadata file
            f.write(trackName + "\t" + trackDesc + "\t" + folder + "\n")

            # Rename the track
            newPath = "../../../RLMG-Local/" # Enter the path relative to the folder where the new files are
            #print(track, newPath+trackName)
            os.rename(track, newPath+"DELETE_"+trackName)
        except:
            print("Skipped "+track)

#Identify all directories
folderList = []
dirContents = os.listdir(".")
for item in dirContents:
    if os.path.isdir(item):
        folderList.append(item)

f = open("../../metadata.txt","a")

for folder in folderList:
    mainDir = os.getcwd()
    os.chdir(os.path.join(mainDir,folder))
    renameTracks(folder)
    os.chdir(mainDir)
    os.rmdir(folder)

f.close()
