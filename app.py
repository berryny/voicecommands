import os
import time
import playsound
import speech_recognition as sr
from gtts import gTTS

# Give text to the computer and have it reply back to us
def speak(text):
    # repeat text in english
        # text (string) – The text to be read.
        # lang (string, optional)
        # slow (bool, optional) – Reads text more slowly. Defaults to False.
    tts = gTTS(text=text, lang="en", slow=True)
    # save and play audio file
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)

# getting microphone input
def get_audio():
    print("listening...")
    # call a recognizer object from speech recognition module
    r = sr.Recognizer()
    r.energy_threshold = 4000
    with sr.Microphone() as source:
        print('source',source)
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        said = ""

        # Google API
        try:
            said = r.recognize_google(audio)
            said = said.lower()
            # This is basically how sensitive the recognizer is to when recognition should start. Higher values mean that it will be less sensitive, which is useful if you are in a loud room.
            # r.energy_threshold = 40000
            print('said',said)
        except Exception as e:
            # microphone error 
            print("Exception:" + str(e))

    return said

# speak("Welcome to Claira")
# get_audio()

text = get_audio()

if "hey claira" or "hey clara" in text:
    speak("Hello, how can I assist you?")

if "what is your name" in text:
    speak("My name is Claira")