# STF and TTS in Python

## Setup

Create directory
```
mkdir romanticAlexa
cd romanticAlexa
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

### requirements file

Command to run and install all packages: `pip install -r requirements.txt`