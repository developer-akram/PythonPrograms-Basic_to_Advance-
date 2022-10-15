import pyttsx3

engine = pyttsx3.init()

# rate
engine.setProperty('rate', 175)

# voice
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(text):
    engine = pyttsx3.init()
    engine.say(text=text)
    engine.runAndWait()
