from gtts import gTTS
import subprocess as s
import threading
import time 

class speaker():
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name
    def sendSound(self):
        s.call(['mplayer','ola.mp3', self.name+'.mp3', 'comovai.mp3'])