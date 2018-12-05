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
    sys.exit(0)

CHUNK = 256
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

signal.signal(signal.SIGINT, signal_handler)
print('Press Ctrl+C')

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK,
                input_device_index=2) #change this to change device   

while(True):
    try:
        data = stream.read(CHUNK)
        rms = audioop.rms(data, 2)
        print(rms)
    except IOError as ex:
        print("Error")

stream.stop_stream()
stream.close()
p.terminate()