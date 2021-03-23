# import pyaudio
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia 

# create a listener to recognize your voice
listener = sr.Recognizer()
# create an engin to speak back to user
engine = pyttsx3.init()

# get all the voices and set to an array
voices = engine.getProperty('voices')
# get the female voice
engine.setProperty('voices', voices[1].id)

def talk(text):
    print('voices')
    # engine.say('Hello World!')
    # engine.say('what can i do for you')
    engine.say(text)
    engine.runAndWait()


# create a try block to check microphone
def take_command():
    try:
        # use the microphone
        with sr.Microphone() as source:
            print("listening...")
            # source of audio to collect the voice and listen to the source
            voice = listener.listen(source)
            print("voice: ",voice)
            # convert voice to text. using google to provide the text
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alex', '')
                print("command: ",command)
                # talk(command)
    except :
        pass

    return command

def run_alexa():
    command = take_command()
    print('run alexa', command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing music' + song)
        print('play the song', song)
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print('time',time)
        talk('current time is' + time)

    elif 'wikipedia' in command:
        searchtext = command.replace('wikipedia', '')
        info = wikipedia.summary(searchtext, 1)
        print("info",info)
        talk(info)

    else:
        talk('Please repeat command.')

# allow voice command in a loop
while True:
    run_alexa()

