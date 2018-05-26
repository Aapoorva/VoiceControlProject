#!/usr/bin/env python3
import SpeechRego as sr
import tts
import os

#intro message
tts.convert_text_n_speak("Welcome What You Want to be done")
#getting text of user audio
user_query = sr.get_audio_to_text()

print(user_query)
#cheching query is empty or not
if user_query != None :
	output = ""
	try:
		output = os.system(user_query)
	except TypeError:
		print("Getting None as user query")

	print(output)