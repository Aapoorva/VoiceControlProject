#!/usr/bin/env python3
import SpeechRego as sr
import tts
import subprocess as sp

#intro message
tts.convert_text_n_speak("Welcome")
tts.convert_text_n_speak("What You Want to be done")

#getting text of user audio
while True:
	user_query = sr.get_audio_to_text()

	# program exit keywords
	exit_keyword = ['quit','exit','cancel','close']
	
	#checking query is empty or not
	if user_query != None :
		# if query has exit keywords, close the application
		if user_query in exit_keyword :
			tts.convert_text_n_speak('exiting')
			break;
		# else execute the command
		else :
			cmd_output = ""
			try :
				#executing command
				cmd_output = sp.run([user_query],check=True,shell=True,stdout=sp.PIPE,)
			except  sp.CalledProcessError :
				print("CalledProcessError Encountered")
				exit()

			if cmd_output != None :
				#command Not Found
				if cmd_output.returncode != 0 :
					print(user_query,"Command Not Found")
				else :
					print(cmd_output.stdout.decode())
	
	#asking for next query
	tts.convert_text_n_speak('What else do you want ?')