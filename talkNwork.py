#!/usr/bin/env python3
import SpeechRego as sr
import tts
import subprocess as sp

#intro message
tts.convert_text_n_speak("Welcome")
tts.convert_text_n_speak("What You Want to be done")

#getting text of user audio
user_query = sr.get_audio_to_text()

#checking query is empty or not
if user_query != None :
	cmd_output = ""
	try :
		cmd_output = sp.run([user_query],check=True,shell=True,stdout=sp.PIPE,)
	except  sp.CalledProcessError :
		print("CalledProcessError")
		exit()

	if cmd_output != None :

		if cmd_output.returncode != 0 :
			print(user_query," Not Found")
		
		else :
			print(cmd_output.stdout.decode())
