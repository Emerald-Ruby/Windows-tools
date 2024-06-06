Made to prevent external devices from modifing the volume of you programs

The system audio is the max volume for your device
The sub processes is a percent of the system volume

"Timing" is divided by 100, so 100 is one second per process

Black listen items are ignored usless they are higher then the system volume

An example of json fromating and how it must look
```
process :
[
    {
        "opera" : 20,
        "steam" : 90
    }
]

black listed :
[
    {
        "
        "opera" : 21308994
    }
]
```

You need to download python and run ` pip install pyinstaller `
Then open a terminal, and cd paste the location of the Audio.py file, eg
` cd C:/user/public/download/Audio `
Then to compile, use ` pyinstaller -onefile Audio.py `, the .exe will in the "disk" folder

if there is a " access violation reading 0xFFFFFFFFFFFFFFFF " it seems to run fine after,
and I havn't seen it in the compiled version