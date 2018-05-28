#!/usr/bin/env python3
import SpeechRego as sr
import tts
import subprocess as sp
import urllib.request
import urllib.parse
import re
import webbrowser

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
		elif user_query.find('youtube')>=0 or user_query.find('play')>=0 or user_query.find('video')>=0:

			video_keywords = user_query.split(' ')
			final_key = []
			remv_keywords = ['Youtube','youtube','from','of','for','video','play','Play','Video','For','Of']
			for word in video_keywords:
				if word.lower() in remv_keywords:
					pass
				else:
					final_key.append(word)
			query_string = urllib.parse.urlencode({"search_query" : final_key[0]})
			html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
			search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
			webbrowser.open_new_tab("http://www.youtube.com/watch?v=" + search_results[0])

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
