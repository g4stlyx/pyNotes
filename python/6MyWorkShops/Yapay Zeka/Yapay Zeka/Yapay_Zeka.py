import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
	print("Dinleniyor...")
	audio = r.listen(source)