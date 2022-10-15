import pyttsx3,time
i = 1
while(i <21):
    if i < 6:
        time.sleep(1)
        x = "You are in Floor "+str(i)
        print(x)
        pyttsx3.speak(x)
    elif i < 11:
        time.sleep(1)
        x = "You are in Floor"+str(11-i)
        print(x)
        pyttsx3.speak(x)
    elif i < 16:
        time.sleep(1)
        x = "You are in Floor "+str(i-10)
        print(x)
        pyttsx3.speak(x)
    else:
        time.sleep(1)
        x = "You are in Floor "+str(21-i)
        print(x)
        pyttsx3.speak(x)
    i += 1