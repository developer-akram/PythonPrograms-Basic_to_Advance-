from pygame import mixer
from datetime import datetime
from time import time
def playmusic(music_name, text_to_stop):
    mixer.init()
    mixer.music.load(music_name)
    mixer.music.play()
    while True:
        a =input()
        if a == text_to_stop :
            mixer.music.stop()
            break
def text_log(text):
    with open("text_log.txt", "a")as f :
        f.write(f"{text} {datetime.now()}\n")
if __name__ == '__main__':
    # playmusic("water.mp3", "stop")
    water_time = time()
    eyes_time = time()
    excercise_time = time()
    water_duration = 60*40
    eyes_duration = 60*30
    excercise_duration = 60*35
    while True:
        if time() - water_time > water_duration:
            print("Time for Drinking water,Type 'drank' to off the Alarm")
            playmusic("water.mp3", "drank")
            water_time = time()
            text_log("Drank water at ")
        if time() - eyes_time > eyes_duration:
            print("Time for Eyes Excercise,Type 'stop' to off the Alarm")
            playmusic("eyes.mp3", "stop")
            eyes_time = time()
            text_log("Drank water at ")
        if time() - excercise_time > excercise_duration:
            print("Time for Physical Excercise,Type 'done' to off the Alarm")
            playmusic("excercise.mp3", "done")
            excercise_time = time()
            text_log("Drank water at ")




