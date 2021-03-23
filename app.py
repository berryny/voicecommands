import os, time, playsound
import speech_recognition as sr
from gtts import gTTS

# Give text to the computer and have it reply back to us
def speak(text):
    # repeat text in english
        # text (string) – The text to be read.
        # lang (string, optional)
    tts = gTTS(text=text, lang="en")
    # save and play audio file
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)

speak("Hello World")