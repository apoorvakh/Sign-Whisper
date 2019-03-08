# -*- coding: utf-8 -*-
from google.cloud import translate
from google.cloud import texttospeech
from gtts import gTTS as tts 
import os
def spconvert(fname):
    txt1 = ""
    with open(fname, "r") as file:
        for line in file:
            txt1 += line
    speech = tts(txt1, 'en')
    speech.save("spout.mp3")
    os.system('start spout.mp3')
def translate_text(text, target = 'de'):
    translate_client = translate.Client()
    result = translate_client.translate(text, target_language = target)

    print(result['translatedText'])
    return result

with open("fout.txt", "r") as file:
    txt2=""
    for line1 in file:
        txt2 = line1
        translate_text(txt2)

spconvert("fout.txt")