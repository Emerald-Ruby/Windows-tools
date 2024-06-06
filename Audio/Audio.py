##############################
# First made     :    23/02/24
# Last edited    :    06/06/2024
# Author         :    Emm
##############################

from ctypes import cast, POINTER
from  comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume, ISimpleAudioVolume

import json
from time import sleep

sessions = AudioUtilities.GetAllSessions()

for session in sessions:
    if session.Process:
        print(session.Process.name())

wait_time = 1
processes = {
    "system" : 100,
    "sub processes" : 100,
}
black_listed = {}

with open("./config.json", "r") as f:
    file = json.load(f)
    wait_time = file["timing"] / 100
    for i in file["processes"][0]:
        processes.update( { i : file["processes"][0][i] } )
    for i in file["black listed"][0]:
        black_listed.update( { i : 0 } )
    f.close()

# Loop
while True:

# Master volume ( system )
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate( IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))

    if ("system" not in black_listed) and volume.GetMasterVolumeLevelScalar() != processes["system"]:
        volume.SetMasterVolumeLevelScalar(processes["system"] / 100, None)

# Sub processes
    sessions = AudioUtilities.GetAllSessions()
    volume = session._ctl.QueryInterface(ISimpleAudioVolume)

    for session in sessions:
        volume = session._ctl.QueryInterface(ISimpleAudioVolume)
        
        if session.Process:
            if session.Process.name().strip(".exe") in black_listed:
                continue
            elif session.Process.name().strip(".exe") in processes:
                vol = processes[session.Process.name().strip(".exe")]
            elif "sub processes" not in black_listed:
                vol = processes["sub processes"]
            else:
                continue


            if volume.GetMasterVolume() != vol / 100:
                volume.SetMasterVolume(vol / 100, None)
            if volume.GetMute() == 1:
                volume.SetMute(0, None)
    sleep(1)
