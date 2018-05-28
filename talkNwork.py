#!/usr/bin/env python3

#this is main file to start project

import SpeechRego as sr
import tts 
import subprocess as sp
import installModule as im

# program exit keywords
exit_keyword = ['quit','exit','cancel','close']

#intro message
tts.speak("welcome")
tts.speak("ask")

def process_user_query() :

	while True:
		user_query = sr.get_audio_to_text()
		
		#checking query is empty or not
		if user_query != None :

			user_query = user_query.lower()
			
			# if query has exit keywords, close the application
			if user_query in exit_keyword :
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
		pass
		# execute_file_query(filtered_query)

	if "directory" in filtered_query :
		pass
		# execute_directory_query(filtered_query)

	elif "install" in filtered_query :
		im.execute_install_query(filtered_query)

	elif "service" in filtered_query :
		pass
		# execute_system_query(filtered_query)
	else :
		pass
		# execute_basic_cmd(filtered_query)

#calling function to start code
process_user_query()