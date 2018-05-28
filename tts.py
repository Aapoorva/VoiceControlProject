#!/usr/bin/env python3
from gtts import gTTS
import os

#to convert text to speech
def convert_text_n_speak(textInput) :
	#converting text
	tts = gTTS(text=textInput, lang='en')
	#saving audio to file
	tts.save("query.wav")
	#playing audio
	os.system("mpg321 query.wav")

#to play existing file
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

# #to convert text to speech and saving to given file name
# def convert_text_n_speak(textInput,file_name) :
# 	#converting text
# 	tts = gTTS(text=textInput, lang='en')
# 	#saving audio to file
# 	tts.save(file_name+".wav")
# 	#playing audio
# 	os.system("mpg321 "+file_name+".wav")


# # usr_input = input("Text : ")
# # file_name = input("File Name : ")
# # convert_text_n_speak(usr_input,file_name)