#!/usr/bin/env python3
# Requires PyAudio and PySpeech.
 
import speech_recognition as sr
import re
from time import ctime
import time
import os
from gtts import gTTS
 
keyWordsHora = ['hora', 'que', 'es', 'cual' , 'la']

#Source: https://stackoverflow.com/questions/10668282/one-liner-to-check-if-at-least-one-item-in-list-exists-in-another-list/10668319
any_in = lambda a, b: any(i in b for i in a)

def speak(audioString):
    print(audioString)
    tts = gTTS(text=audioString, lang='es')
    tts.save("audio.mp3")
    os.system("rhythmbox audio.mp3")
 
def recordAudio():
    # Record Audio
    # r = sr.Recognizer()
    # with sr.Microphone() as source:
    #     r.adjust_for_ambient_noise(source)
    #     print("Di algo!")
    #     audio = r.listen(source)
 
    # # Speech recognition using Google Speech Recognition
    # data = ""
    # try:
    #     # Uses the default API key
    #     # To use another API key: `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    #     data = r.recognize_google(audio)
    #     print("Tu dijiste: " + data)
    # except sr.UnknownValueError:
    #     print("Google Speech Recognition no puede entender lo que dices")
    # except sr.RequestError as e:
    #     print("Could not request results from Google Speech Recognition service; {0}".format(e))

    data = input("Ingresa que quieres que haga: ")

    return data
 
def jarvis(data):
    pattern = r'\s'

    if "como estas" in data:
        speak("Estoy de puta madre")
 
    if any_in(re.split(pattern, data), keyWordsHora):
        speak(ctime())
 
    if "donde esta" in data:
        data = data.split(" ")
        location = data[2]
        speak("Espera, te mostrare donde " + location + " is.")
        os.system("firefox https://www.google.nl/maps/place/" + location + "/&amp;")
 
# initialization
time.sleep(2)
speak("Hola, que puedo hacer por ti?")
while 1:
    data = recordAudio()
    jarvis(data)