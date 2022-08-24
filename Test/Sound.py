from gtts import gTTS
import Video


def makeSound(text, name):
    reddittext = text.replace("fuck", "duck")
    reddittext1 = reddittext.replace("dick", "pp")
    tts = gTTS(reddittext1, 'co.ck', "en")
    tts.save(name+'.wav')
