import simpleaudio as sa
import time

# creating an empty list for the rhythm forloop
rhytmList = []

print("how many samples?")
numPlaybackTimes = input("")

# import snare sample
wave_obj = sa.WaveObject.from_wave_file("audio_files/rim_short.wav")

print("which rhythm")

# creating "numPlaybackTimes" amount of inputs and appending those inputs to create a list
for rhythm in range(0, int(numPlaybackTimes)):
    tijd = input()
    rhytmList.append(tijd)
print(rhytmList)

print("which BPM?")
bpm = input()
aantalSecondeperbeat = 60/int(bpm);
print(aantalSecondeperbeat)

# plays the sample with the delay-values from someList
for x in rhytmList:
    print(x)
    play_obj = wave_obj.play()
    # calculating the seconds per beat by multiplying them with the note values from rhythmList
    time.sleep(aantalSecondeperbeat * float(x))
