from gtts import gTTS
import subprocess as s

#tts = gTTS('david', lang='pt')
#tts.save('david.mp3')

s.call(['mplayer','ola.mp3', 'victor.mp3', 'comovai.mp3'])
