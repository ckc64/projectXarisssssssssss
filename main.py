import speech_recognition as sr
import playsound
import os
import random
from gtts import gTTS
import time 
from time import ctime
import webbrowser
import youtube_dl as yt
from bs4 import BeautifulSoup
import urllib.request

r = sr.Recognizer()
videoList = []
def get_musicID(music):
    # query = os.system('youtube-dl --print-json "ytsearch1:{0}"'.format(music))
    
    # print(query)
    query = urllib.parse.quote(music)
    url = "https://www.youtube.com/results?search_query=" + query
    response = urllib.request.urlopen(url)
    html = response.read()
    soup = BeautifulSoup(html, 'html.parser')
    
    for vid in soup.findAll(attrs={'class':'yt-uix-tile-link'}):
        videoList.append('https://www.youtube.com' + vid['href'])
        print('https://www.youtube.com' + vid['href'])
     

def record_audio(ask=False):
    with sr.Microphone() as source:
        
        if ask:
            xaris_speak(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
          
        except sr.UnknownValueError:
            xaris_speak("Sorry, please repeat your request")
           
        except sr.RequestError:
            xaris_speak("Sorry, I am undermaintenance")
           
        return voice_data

def xaris_speak(audio_string):
    tts = gTTS(text=audio_string,lang="en")
    r = random.randint(1,1000000)
    audio_file = 'audio-' + str(r)+'.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)

def respond(voice_data):
    if 'what is your name' in voice_data:
        xaris_speak('My Name is Xaris version 0.1')
    if 'who is your master' in voice_data:
        xaris_speak('My master is charles')
    if 'tell me about yourself' in voice_data:
        xaris_speak('I am Xaris 0.1 my creator is Charles Kurt, He created me because he is bored.')
    if 'search' in voice_data:
        search = record_audio("What do you want to search ?")
        url = 'https://www.google.com/search?tbm=isch&q=' + search
        xaris_speak("Here is the "+search)
        webbrowser.get().open(url)
    if 'music' in voice_data:
        music = record_audio("What music do you want ?")
        get_musicID(music)
        
        url = videoList[0]
        xaris_speak("Here is the "+music)
       
        webbrowser.get().open_new(url)
       
    if 'exit' in voice_data:
        xaris_speak('Thank You, Master Charles')
        exit()

time.sleep(1)
xaris_speak('Hello Master Charles, How can i help you ?')
while 1:
    voice_data = record_audio()
    respond(voice_data)
  
