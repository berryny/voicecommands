import os
import time
import speech_recognition as sr
from playsound import playsound
from gtts import gTTS

# Give text to the computer and have it reply back to us
def speak(text):
    print('speak text:', text)
    # repeat text in english
        # text (string) – The text to be read.
        # lang (string, optional)
        # slow (bool, optional) – Reads text more slowly. Defaults to False.
    tts = gTTS(text=text, lang="en", slow=True)
    # save and play audio file
    filename = "voice.mp3"
    tts.save(filename)
    playsound(filename)
    os.remove(filename)

# getting microphone input
def get_audio():
    print("listening...")
    # call a recognizer object from speech recognition module
    r = sr.Recognizer()
    r.energy_threshold = 10000
    mic = sr.Microphone(device_index=1)
    with mic as source:
        print('source',source)
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source, phrase_time_limit=2)
        said = ""

        # Google API
        try:
            said = r.recognize_google(audio)
            said = said.lower()
            # This is basically how sensitive the recognizer is to when recognition should start. Higher values mean that it will be less sensitive, which is useful if you are in a loud room.
            print('said',said)
        except Exception as e:
            # microphone error 
            print("Exception:" + str(e))

    return said


def run_claira():
    text = get_audio()
    if "hey clara" in text:
        speak("Hello, how can I assist you?")
    elif "ai" in text:
        speak("Artificial intelligence is intelligence demonstrated by machines, unlike the natural intelligence displayed by humans and animals, which involves consciousness and emotionality.")
    elif "what is your name" in text:
        speak("My name is Claira")
    else:
        speak('Please repeat command.')


# allow voice command in a loop

if __name__ == "__main__":
    while True:
        run_claira()

        # command to exit out of program
        if 'quit' in get_audio():
            break
            

