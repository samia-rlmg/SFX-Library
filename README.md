# SFX-Library
Processes updates for importing into Soundly

## Adding New SFX to Soundly Library

1. Navigate to RLMG-Share/RLMG/Sound Effects/MASTER SOUND FX_NEW/Add-New-SFX/New-SFX.
2. Copy your folder of new SFX (or multiple folders) inside here. Each folder's name will be entered into Soundly as the "Originator," so name it accordingly.

## Run the script to process new sounds
1. In the terminal, navigate to the same location (the parent directory of the new SFX folders).

    `cd /Volumes/RLMG-Share/RLMG/Sound\ Effects/MASTER\ SOUND\ FX_NEW/Add-New-SFX/New-SFX`


2. Run the following command: 

    `python ../Add-New-SFX/processNewSounds.py`

    This script will do three things: (a) convert any AIFF or CAF to WAV (preserving all channels of CAF files), (b) move the SFX files into RLMG-Local, and (c) update the metadata.txt file with the file’s name, description, and library (called “originator” in the metadata and Soundly).

## Update Shared Network in Soundly
When you add new sounds to the Soundly RLMG folder you need to UPDATE the database. 

1. First disconnect the existing network database. (In Soundly, right-click on "Network" in the top-left and select "Disconnect.")

2. Create a new shared network database. (In the menu, select "Database > New shared network database.")

3. Select database location and name. You can name the file “RLMG-Local.sdb” (yes, overwriting the existing file) or give it a new name.
You will have to choose the metadata.txt file again.

4. Connect to the shared database you just created. (In Soundly, select "Database > Connect to shared network database.")

5. The shared RLMG-Local library should appear in the menu at the top-left under “Network.” This process takes around an hour and a half.
