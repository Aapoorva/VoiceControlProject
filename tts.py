#!/usr/bin/env python3

#this module is to convert text to speech

import gtts
from gtts import gTTS
import os

#to convert text to speech
def convert_text_n_speak(textInput) :
	try :
		#converting text
		tts = gTTS(text=textInput, lang='en')
		#saving audio to file
		tts.save("query.wav")
		#playing audio
		os.system("mpg321 query.wav")
	except gtts.tts.gTTSError :
		print("Please Check Internet Connection")

#to play existing audio file
def speak(msg) :
	if msg == "welcome" :
		os.system("mpg321 welcome.wav")
	elif msg == "ask" :
		os.system("mpg321 ask.wav")
	elif msg == "askNext" :
		os.system("mpg321 askNext.wav")
	elif msg == "exit" :
		os.system("mpg321 exit.wav")
	else :
		os.system("mpg321 notFound.wav")

#to convert text to speech and saving to given file name
def convert_txt_n_store(textInput,file_name) :
	#converting text
	tts = gTTS(text=textInput, lang='en')
	#saving audio to file
	tts.save(file_name+".wav")
	#playing audio
	os.system("mpg321 "+file_name+".wav")
