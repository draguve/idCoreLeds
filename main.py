#!/usr/bin/env python
import signal
import sys
import pyaudio
import wave
import audioop

def signal_handler(sig, frame):
    stream.stop_stream()
    stream.close()
    p.terminate()
    print('You pressed Ctrl+C!')
    sys.exit(0)

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 5

signal.signal(signal.SIGINT, signal_handler)
print('Press Ctrl+C')

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)



# for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
#     data = stream.read(CHUNK)
#     rms = audioop.rms(data, 2)    # here's where you calculate the volume
#     print(rms)

while(True):
    data = stream.read(CHUNK)
    rms = audioop.rms(data, 2)    # here's where you calculate the volume
    print(rms)

stream.stop_stream()
stream.close()
p.terminate()