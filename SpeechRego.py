#!/usr/bin/env python3

#this module is to recognize speech and convert to text

#to recognize speech using Api or speech engine
import speech_recognition as sr
import tts
#to commuticate to microphone install pyaudio


import tts
#recognizer instance
r=sr.Recognizer()

#function to get audio from microphone
def listen_from_microphone() :
	#fetching audio from microphone
	mic=sr.Microphone()
	print("Listening ....")
	#capturing microphone input
	with mic as source :
		#handling noise
		r.adjust_for_ambient_noise(source)
		audio = r.listen(source)
	return audio

def get_audio_to_text() :

	audio = listen_from_microphone()

	text_frm_audio = ""
	print("Converting to text")
	#passing audio to recongnizer
	#recognizer method for recognizing speech from audio source
	#using google web speech api - requires internet conn./
	try :
		text_frm_audio = r.recognize_google(audio)
		print("You said : ",text_frm_audio)
	except sr.RequestError :
	#Api Unreachable
		tts.convert_text_n_speak("Please Check internet Connection")
		return
	except sr.UnknownValueError :
	#Audio Can Not be Detected
		tts.convert_text_n_speak("Audio is Not Recognizable")

	if text_frm_audio == "" or text_frm_audio == None :
		text_frm_audio = get_audio_to_text()

	return text_frm_audio

#get_audio_to_text()