# -*- coding: utf-8 -*-

import speechrecognition as sr

r= sr.Recognizer()
with sr.Microphone() as source:
    print("Dinleniyor")
    audio= r.listen(source)
    # try:
    #     str=r.recognize_google(audio,language="tr-tr")