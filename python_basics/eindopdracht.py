#importeer de benodigde modules om de code te laten werken
import simpleaudio as sa
import time
import random
from midiutil.MidiFile import MIDIFile
from midiutil import MIDIFile
#de samples worden gedefinieerd: sample snare is 0, sample hat is 1, sample tom is 2
samples = [sa.WaveObject.from_wave_file("audio_files/pop.wav"), sa.WaveObject.from_wave_file("audio_files/Dog2.wav"),sa.WaveObject.from_wave_file("audio_files/Laser1.wav") ]
MyMIDI = MIDIFile(2)

#we vragen welke maatsoort en welk bpm er gebruikt moet worden, en die worden gedefinieerd
print("wil je maatsoort 3/4 of 5/4?")
rythmChoice = input()

while rythmChoice not in ("3/4", "5/4"):
    if rythmChoice == "3/4":
        print("")
    elif rythmChoice == "5/4":
        print("")
    else:
        print("sorry doei")
        exit()

print("welk bpm wil je?")
bpm = int(input())
print("je hebt gekozen voor het bpm", bpm, "en de maatsoort", rythmChoice)

track = 0
channel  = 9
velocity = 100
MyMIDI.addTempo(track, 0, bpm)

#bereken de duratie van een kwartnoot
quarterNoteDuration = 60 / int(bpm)
#bereken de duratie van een 16de noot
sixteenthNoteDuration = quarterNoteDuration / 4.0

#start van de code-loop main() die later wordt aangevraagd
def main():
    timestamps = []
    #creeert een lijst om de ritme sequence in te bewaren
    rythmList = []
    #creeert een lijst om de timestamps sequence in te bewaren
    timestamps16th = [0]
    #creeert een lijst met de nootwaarden (16de, 8ste en kwart)
    noteValues = [0.25, 0.5, 1.0]
    item = 0
    #creeert een lijst om de midiDuration sequence in te bewaren
    midiDurationList = []
    #creeert een lijst om de midiPitch waardes in te bewaren
    pitchList = []

    #3/4 lijst aanmaken
    if rythmChoice == '3/4':
        numeratorChoice = 3
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
        numeratorChoice = 5
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
    #print("Timestamps opgeteld:", sum(rythmList))
    #print("ritmesequence:", rythmList)

    #conversie van ritmewaarden naar timestamps16th
    for duration in rythmList:
        timestamp = duration * 4
        final = timestamps16th[item] + timestamp
        timestamps16th.append(final)
        item = item + 1
    #print("timestamps16th:", timestamps16th)

    #nu zetten we de originele timestamps16th om in de timestamps op basis van het bpm
    for timestamp in timestamps16th:
      timestamps.append(timestamp * sixteenthNoteDuration)
    #print("bpm-timestamp lijst:", timestamps)

    #nu maken we de samplelijst
    sampleList = []

    #random lijst genereren van 0 tot 2 om de smaples te kiezen
    for timestamp in timestamps:
        sampleList.append(random.randrange(0, 3, 1))
    #print("samplelijst:", sampleList)

    for sampleNumber in sampleList:
        if sampleNumber == 0:
            pitchList.append(35)
        if sampleNumber == 1:
            pitchList.append(38)
        if sampleNumber == 2:
            pitchList.append(42)
    #print("pitchList:", pitchList)

    #nu gaan we de samplelijst afspelen
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

    #beat opslaan en midi conversie:
    for midiTime in rythmList:
        midiDurationList.append(midiTime * 2)
    #print("midi Duration-ritme:", midiDurationList)

    midiDurationList.append(0)

    MyMIDI.addTimeSignature(track, 0, numeratorChoice, 2, 24)

    #maakt een midi file aan met de duratie, pitch en timestamps op basis van de eerder gemaakte lijsten
    for i, x, y in zip(midiDurationList, timestamps16th, pitchList):
        MyMIDI.addNote(track, channel, y, x * 0.25, i, velocity)
        #print(i, x, y)

    #vraagt of je de besat wil exporteren als midi file en daarna of je een nieuwe beat wilt maken.
    while True:
      midiAnswer = input('wil je deze sequence exporteren als midi file? (yes/no)')
      if midiAnswer.lower().startswith("y"):
          print("..exporting rythm to midi file..")
          #write to MIDIfile
          with open("bloeb.mid", "wb") as output_file:
              MyMIDI.writeFile(output_file)
          while True:
            answer = input('Do you want to generate a new rythm? (yes/no):')
            if answer.lower().startswith("y"):
                print("..generating new rythm..")
                main()
            elif answer.lower().startswith("n"):
                print("ok, bye")
                exit()
      elif midiAnswer.lower().startswith("n"):
        while True:
          answer = input('Do you want to generate a new rythm? (yes/no):')
          if answer.lower().startswith("y"):
              print("..generating new rythm..")
              main()
          elif answer.lower().startswith("n"):
              print("ok, bye")
              exit()
main()
