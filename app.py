import os
import time
import speech_recognition as sr
from playsound import playsound
from gtts import gTTS

#----------------------------------------------------------------------------#
# Use API key to access OpenAI
#----------------------------------------------------------------------------#
import openai
# from gpt3 import gpt3

from dotenv import load_dotenv, find_dotenv # imports module for dotenv
load_dotenv(find_dotenv()) # loads .env from root directory

# The root directory requires a .env file with API_KEY assigned/defined within
ai_api_key = os.environ['OPENAI_API_KEY']

openai.api_key = ai_api_key

# response = openai.Completion.create(
#   engine="davinci",
#   prompt="The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.\n\nHuman: Hello, who are you?\nAI: I am an AI created by OpenAI. How can I help you today?\nHuman: I'd like to cancel my subscription.\nAI:",
#   temperature=0.4,
#   max_tokens=60,
#   top_p=1.0,
#   frequency_penalty=0.5,
#   presence_penalty=0.0,
#   stop=["\n", " Human:", " AI:"]
# )

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
    if "what is ai" in text:
        speak("Artificial intelligence")
    elif "what is your name" in text:
        speak("My name is Claira")
    else:
        speak('Please repeat command.')
        
start_chat_log = '''Human: Hello, who are you?
AI: I am doing great. How can I help you today?
'''

def ask(question, chat_log=None):
    if chat_log is None:
        chat_log = start_chat_log
    prompt = f'{chat_log}Human: {question}\nAI:'
    response = openai.Completion.create(
        prompt=prompt, 
        engine="davinci", 
        stop=['\nHuman'], 
        temperature=0.9,
        top_p=1, 
        frequency_penalty=0, 
        presence_penalty=0, 
        best_of=1,
        max_tokens=150
    )
    # temperature=0.9, top_p=1, frequency_penalty=0, presence_penalty=0.6, best_of=1, max_tokens=150
    answer = response.choices[0].text.strip()
    print('AI answer',answer)
    return answer

# allow voice command in a loop

if __name__ == "__main__":
    while True:
        # command to exit out of program
        getAudioFunc = get_audio()
        if 'exit' in getAudioFunc:
            speak("good bye")
            break
        else:
            speak(ask(getAudioFunc)
)

