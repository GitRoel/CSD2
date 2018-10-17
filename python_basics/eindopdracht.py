import simpleaudio as sa
import time
import random

#sample-list, seen as [0,1,2]
samples = [sa.WaveObject.from_wave_file("audio_files/Dog2.wav"), sa.WaveObject.from_wave_file("audio_files/pop.wav"), sa.WaveObject.from_wave_file("audio_files/Laser1.wav")]

print("which rhythm?")
rhythmChoice = input()

print("which bpm?")
bpm = int(input())

print(rhythmChoice, bpm)

lijst1 = [0.25, 0.5, 0.25, 0.5, 0.5, 1, 1]
lijst2 = [0]
item = 0

for duration in lijst1:
    timestamp = duration * 4
    final = lijst2[item] + timestamp
    lijst2.append(final)
    item = item + 1
print(lijst2)
