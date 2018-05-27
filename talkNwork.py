#!/usr/bin/env python3
import SpeechRego as sr
import tts
import subprocess

# intro message
tts.convert_text_n_speak("Welcome What You Want to be done")
# getting text of user audio
while True:
	user_query = sr.get_audio_to_text()
	print(user_query)
    # program exit keywords
	exit_keyword = ['quit','exit','cancel','close']
    # cheching query is empty or not
	if user_query != None :
		# if query has exit keywords, close the application
		if user_query in exit_keyword:
			tts.convert_text_n_speak('exiting')
			break;
		# else execute the command
		else:
			output = ""
			try:
				output = subprocess.run([user_query])
			except TypeError:
				print("Getting None as user query")
			print(output)
	tts.convert_text_n_speak('What else do you want ?')
