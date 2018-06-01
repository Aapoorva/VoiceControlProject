
#!/usr/bin/env python3

#this is main file to start project

import SpeechRego as sr
import tts
import subprocess as sp
import youtube_play as yp
import installModule as im
import file_operations as fo
import execute_commands as ec
#import directory_op as do
import google_search as gs
import service as se

# program exit keywords
exit_keyword = ['quit','exit','cancel','close']

#intro message
tts.convert_text_n_speak("welcome")

tts.convert_text_n_speak("ask")

def process_user_query() :

	while True:
		user_query = sr.get_audio_to_text()

		#checking query is empty or not
		if user_query != None :

			user_query = user_query.lower()

			# if query has exit keywords, close the application
			if exit_keyword[0] in user_query or exit_keyword[1] in user_query or exit_keyword[3] in user_query:
				tts.speak("exit")
				break;
			# else execute the command
			else :
				filter_query_trigger(user_query)
				#asking for next query
				tts.speak("askNext")

# to filter query and call related function
def filter_query_trigger(user_query) :
	#tokenizing user query
	filtered_query = user_query.strip().split()

	#calling function for respective query
	if "file" in filtered_query :
		fo.call_file(filtered_query)

	elif "directory" in filtered_query or "folder" in filtered_query:
		#do.execute_directory_query(filtered_query)
		pass

	elif "install" in filtered_query :
		im.execute_install_query(filtered_query)

	elif "service" in filtered_query :
		se.Service(filtered_query)

	elif "youtube" in filtered_query or "play" in filtered_query or "video" in filtered_query:
		yp.play_youtube(filtered_query)
	# search the words on google
	elif "search" in filtered_query or "google" in filtered_query:
		gs.search_google(filtered_query)

	# elif "command" in filtered_query or "directory" in filtered_query or "file" in filtered_query :
	# 	ec.execute_commands(filtered_query)

	else :
		#executing a command like date, cal, check internet
		ec.execute_commands(filtered_query)

#calling function to start code
tts.convert_text_n_speak("What else sir")
process_user_query()
