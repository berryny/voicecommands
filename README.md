# STF and TTS in Python

## Setup

Create directory
```
mkdir voicecommands
cd voicecommands
```

Add virtual environment in VSCode (powershell terminal)
```
virtualenv venv 
venv\Scripts\activate.ps1    
```

## Python Packages

Install individual packages
- [SpeechRecognition · PyPI](https://pypi.org/project/SpeechRecognition/)
    - install `pip install SpeechRecognition`
    - install using python3 `py -m pip install SpeechRecognition`
    - To quickly try it out, run python -m speech_recognition after installing.

- [pyttsx3](https://pypi.org/project/pyttsx3/)
    - install `pip install pyttsx3 `
    - install using python3 `py -m pip install pyttsx3`

- [PyAudio](https://pypi.org/project/PyAudio/)
    - install `pip install PyAudio`
    - install on Windows [pipwin](https://pypi.org/project/pipwin/)
    ```
    py -m pip install pipwin
    pipwin install Pyaudio
    ```

- [PyWhatKit](https://pypi.org/project/pywhatkit/)
    - install `pip install pywhatkit`

- [wikipedia ](https://pypi.org/project/wikipedia/)
    - install `pip install wikipedia`

### Requirements file

Command to install all packages: 

- mac iOS
```
pip3 install -r requirements.txt
```
    - **Error** with installing pyaudio
    ```
    brew install portaudio
    pip3 install pyaudio
    ```

- Windows
```
pip install -r requirements.txt
```

## Execute Command

```
py app.py
```

## GitHub

- …or create a new repository on the command line
```
echo "# voicecommands" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/berryny/voicecommands.git
git push -u origin main
```
- …or push an existing repository from the command line
```
git remote add origin https://github.com/berryny/voicecommands.git
git branch -M main
git push -u origin main
```