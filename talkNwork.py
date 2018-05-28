#!/usr/bin/env python3
import SpeechRego as sr
import tts 
import subprocess as sp

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

def filter_query_trigger(user_query) :
	#tokenizing user query
	filtered_query = user_query.strip().split()

	#calling function for respective query
	if "file" in filtered_query :
		pass
		# execute_file_query(filtered_query)

	elif "install" in filtered_query :
		execute_install_query(filtered_query)

	elif "service" in filtered_query :
		pass
		# execute_system_query(filtered_query)
	else :
		pass
		# execute_basic_cmd(filtered_query)


#to install a service or python library related query
def execute_install_query(filtered_query) :

	#filtering python library query
	if "python" in filtered_query :
		indx = filtered_query.index('library')
		library_name = filtered_query[indx + 1]
		#install library
		cmd_output = execute_cmd('pip3 install '+library_name)
		if cmd_output.returncode != 0 :
			tts.convert_text_n_speak("Sorry Library Not Found")
		else :
			tts.convert_text_n_speak("Installed " + library_name + " Library")
	
	#installing ubuntu packages
	else :
		indx = filtered_query.index('install')
		pckg_name = filtered_query[indx + 1]
		#install library
		cmd_output = execute_cmd('apt install '+pckg_name)
		if cmd_output.returncode != 0 :
			tts.convert_text_n_speak("Unable to install service")
		else :
			tts.convert_text_n_speak("Installed " + pckg_name + " Library")

#to execute a command
def execute_cmd(cmd) :
	cmd_output = ""
	try :
		#executing command
		cmd_output = sp.run([cmd],shell=True,stdout=sp.PIPE,stderr=sp.PIPE)
	except sp.CalledProcessError :
		print(cmd,"Command Not Found")
		exit()

	return cmd_output

process_user_query()