import simpleaudio as sa
import time


print("how many tiem?")
numPlaybackTimes = input("")
print(numPlaybackTimes)

print("welk ritme")

#ritme1 = float(ritme)

ritme = [float(x) for x in input().split()]
print(ritme)

for times in range(0, int(numPlaybackTimes)):
    for play in ritme:
        wave_obj = sa.WaveObject.from_wave_file("audio_files/rim_short.wav")
        play_obj = wave_obj.play()
        play_obj.wait_done()
        print(play)
        for time in ritme:
            time.sleep(ritme)
    print("end loop")
    print()
