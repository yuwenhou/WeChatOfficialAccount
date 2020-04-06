# 需要链接外网使用谷歌的服务
from gtts import gTTS
import os

tts = gTTS(text="come on",lang="en")
tts.save("test.mp3")
os.system("mpg321 test.mp3")
