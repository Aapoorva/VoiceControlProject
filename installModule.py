#!/usr/bin/env python3

#this module is to install python library or a package

import tts
import cmdExecute as ce

#to install a service or python library related query
def execute_install_query(filtered_query) :

	#filtering python library query
	if "python" in filtered_query :
		indx = filtered_query.index('library')
		library_name = filtered_query[indx + 1]
		#install library
		cmd_output = ce.execute_cmd('pip3 install '+library_name)
		if cmd_output.returncode != 0 :
			tts.convert_text_n_speak("Sorry Library Not Found")
		else :
			tts.convert_text_n_speak("Installed " + library_name + " Library")
	
	#installing ubuntu packages
	else :
		indx = filtered_query.index('install')
		pckg_name = filtered_query[indx + 1]
		#install library
		cmd_output = ce.execute_cmd('apt install '+pckg_name)
		if cmd_output.returncode != 0 :
			tts.convert_text_n_speak("Unable to install service")
		else :
			tts.convert_text_n_speak("Installed " + pckg_name + " Library")