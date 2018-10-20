#importeer de benodigde modules om de code te laten werken
import simpleaudio as sa
import time
import random

#de samples worden gedefinieerd: sample snare is 0, sample hat is 1, sample tom is 2
samples = [sa.WaveObject.from_wave_file("audio_files/pop.wav"), sa.WaveObject.from_wave_file("audio_files/Dog2.wav"),sa.WaveObject.from_wave_file("audio_files/Laser1.wav") ]

#we vragen welke maatsoort en welk bpm er gebruikt moet worden, en die worden gedefinieerd
print("wil je maatsoort 3/4 of 5/4?")
rythmChoice = input()

if rythmChoice != ("3/4" or "5/4"):
    print("whoops hihi nee kies uit 3/4 of 5/4 ;)")
    print("wil je maatsoort 3/4 of 5/4?, niet geinig doen")
    rythmChoice = input()
    if rythmChoice != ("3/4" or "5/4"):
        print("jammer dat je dit niet kan doei")
        exit()

print("welk bpm wil je?")
bpm = int(input())

print("je hebt gekozen voor het bpm", bpm, "en de maatsoort", rythmChoice)

# calculate the duration of a quarter note
quarterNoteDuration = 60 / int(bpm)
# calculate the duration of a sixteenth note
sixteenthNoteDuration = quarterNoteDuration / 4.0

timestamps = []

# create a list to hold the rhythm sequence
rythmList = []
print(rythmList)

#nu maken we een functie die de durations omzet naar timestamps16th
timestamps16th = [0]

noteValues = [0.25, 0.5, 1.0]

item = 0

#3/4 lijst aanmaken
if rythmChoice == '3/4':
    while sum(rythmList) <= 2:
        rythmList.append(random.choice(noteValues))

    if sum(rythmList) == 2:
        rythmList.append(1)

    if sum(rythmList) == 2.25:
        rythmList.append(0.75)

    if sum(rythmList) == 2.5:
        rythmList.append(0.5)

    if sum(rythmList) == 2.75:
        rythmList.append(0.25)

#5/4 lijst aanmaken
if rythmChoice == '5/4':
    while sum(rythmList) <= 4:
        rythmList.append(random.choice(noteValues))

    if sum(rythmList) == 4:
        rythmList.append(1)

    if sum(rythmList) == 4.25:
        rythmList.append(0.75)

    if sum(rythmList) == 4.5:
        rythmList.append(0.5)

    if sum(rythmList) == 4.75:
        rythmList.append(0.25)

print("Timestamps opgeteld:", sum(rythmList))

print("ritmesequence:", rythmList)

for duration in rythmList:
    timestamp = duration * 4
    final = timestamps16th[item] + timestamp
    timestamps16th.append(final)
    item = item + 1

print("timestamps16th:", timestamps16th)

#nu zetten we de originele timestamps om in de timestamps op basis van het bpm
for timestamp in timestamps16th:
  timestamps.append(timestamp * sixteenthNoteDuration)
print("bpm-timestamp lijst:", timestamps)

#nu maken we de samplelijst
sampleList = []

for timestamp in timestamps:
    sampleList.append(random.randrange(0, 3, 1))

print("samplelijst:", sampleList)

#nu gaan we de samplelijst afspelen

#NOTE: pop(0) returns and removes the element at index 0
timestamp = timestamps.pop(0)
# retrieve the startime: current time
startTime = time.time()
keepPlaying = True
# play the sequence

while keepPlaying:
  # retrieve current time
  currentTime = time.time()
  # check if the timestamp's time is passed
  if(currentTime - startTime >= timestamp):
    # play sample
    samples[sampleList[0]].play()
    sampleList.pop(0)
    # if there are timestamps left in the timestamps list
    if timestamps:
      # retrieve the next timestamp
      timestamp = timestamps.pop(0)
    else:
      # list is empty, stop loop
      keepPlaying = False
  else:
    # wait for a very short moment
    time.sleep(0.001)

while True:
  answer = input('Do you want to continue? (yes/no):')
  if answer.lower().startswith("y"):
      print("..generating new rhythm..")
  elif answer.lower().startswith("n"):
      print("ok, bye")
      exit()
