import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
for voice in voices:
    print(voice)
    # engine.setProperty('voice', 'com.apple.speech.synthesis.voice.sin-ji') # 粤语
    engine.setProperty('voice', voice.id)
    engine.say('一行数据')
engine.runAndWait()