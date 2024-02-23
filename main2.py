from gtts import *
import os

s = 'escape'
file = 'file.mp3'

# tts = gTTs(s,'en')
# tts.save(file)


f = 'f.mp3'
os.system("mpg123 " + f)