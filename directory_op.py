#!/usr/bin/env python3

import tts
# import SpeechRego as sr
import textInput as sr
import subprocess as sp
import os.path
from time import sleep

def dir_path(filtered_query) :
	start_index=-1
	last_index=
	path=""

	#removing folder or directory word in query
	for word in filtered_query :
		if word == "folder" or word == "directory" :
			filtered_query.remove(word)

	#checking directory path given or not
	if "in" in filtered_query :
		start_index = filtered_query.index("in")
	elif "of" in filtered_query :
		start_index = filtered_query.index("of")
	elif "under" in filtered_query :	
		start_index = filtered_query.index("under")
	#directory path not given
	else :
		tts.convert_text_n_speak("Please tell directory location")
		user_input = sr.get_audio_to_text()
		if user_input != None :
			user_input_split = user_input.lower().strip().split()
			#calling function to create path
			path = dir_path(user_input_split)

	#creating path by parsing list from start_index i.e. index of in/of/under
	if start_index != -1 :
		i = start_index+1
		while i < len(filtered_query) :
			dir_name = filtered_query[i]
			path=dir_name + "/" + path
			#skipping splitter word i.e. in/of/under
			i=i+2

	return path

#to refine path for home, current dir and checking validity
def refine_path(path) :
	path = "/" + path

	if path.find('home') != -1 :
		#getting user name to get home directory path
		out = sp.run(['echo $USER'],shell=True,stdout=sp.PIPE,stderr=sp.PIPE)
		user = out.stdout.decode().replace("\n","")
		path = path.replace("home","home/"+user)

	elif path.find('current',0) != -1 :
		#getting current directory path
		out = sp.run(['pwd'],shell=True,stdout=sp.PIPE,stderr=sp.PIPE)
		curr_dir = out.stdout.decode().replace("\n","")
		path = path.replace("/current",curr_dir)

	#checking dir location exixts or not
	if not os.path.isdir(path) :
		print(path)
		tts.convert_text_n_speak("Sorry Location is invalid please check and try again")
		return

	print(path)

	return path

def get_dir_name(filtered_query) :

	print("query : ",filtered_query)

	if len(filtered_query) == 1 :
		dir_name = filtered_query[0]

	else :
		split_words=['in','of','under']

		dir_name = ""
		name_index = -1

		if "name" in filtered_query :
			name_index = filtered_query.index("name")
		elif "named" in filtered_query :
			name_index = filtered_query.index("named")
		elif "directory" in filtered_query :
			name_index = filtered_query.index("directory")
		elif "folder" in filtered_query :
			name_index = filtered_query.index("folder")
		
		#storing dir name
		if name_index+1 < len(filtered_query) :
			dir_name = filtered_query[name_index+1]

		#dir name not given
		if dir_name in split_words or name_index == -1 :
			tts.convert_text_n_speak("Please tell directory name")
			user_input = sr.get_audio_to_text()
			if user_input != None :
				user_input_split = user_input.lower().strip().split()
				#calling function to create path
				dir_name = get_dir_name(user_input_split)

	return dir_name

def  get_dir_path(filtered_query):

	path = dir_path(filtered_query)
	refined_path = refine_path(path)
	if refined_path == None or refined_path == "" :
		return

	#reading directory name
	new_dir_name = get_dir_name(filtered_query)

	#creating absolute path
	abs_path = refined_path + new_dir_name

	return abs_path

# to create dir
def create_dir(filtered_query) :
	
	abs_path = get_dir_path(filtered_query)	

	#checking directory already exists or not
	if os.path.isdir(abs_path) :
		tts.convert_text_n_speak("Directory Already Exists. Check before creating")
		return
	#creating command
	create_dir_cmd = 'mkdir ' + abs_path
	#creating dir
	out = sp.run([create_dir_cmd],shell=True,stdout=sp.PIPE,stderr=sp.PIPE)
	if out.returncode == 0 :
		tts.convert_text_n_speak("Directory created")
	else :
		tts.convert_text_n_speak("Unable to Create directory. Please try again later")
	sleep(5)

def remove_dir(filtered_query) :

	abs_path = get_dir_path(filtered_query)
	
	#checking directory exists or not
	if not os.path.isdir(abs_path) :
		tts.convert_text_n_speak("Please Check Directory Does Not Exists")
		return
	tts.convert_text_n_speak("Are you sure? You want to remove directory ?")
	user_input = sr.get_audio_to_text()
	user_input = user_input.lower().strip().split()

	if "yes" in user_input :	

		#creating command
		create_dir_cmd = 'rm -r ' + abs_path
		#creating dir
		out = sp.run([create_dir_cmd],shell=True,stdout=sp.PIPE,stderr=sp.PIPE)
		if out.returncode == 0 :
			tts.convert_text_n_speak("Directory Successfully Removed")
		else :
			tts.convert_text_n_speak("Unable to Remove directory. Please try again later")
		sleep(5)
	else :
		tts.convert_text_n_speak("Aage se dhayan rakhna")


def execute_directory_query(filtered_query) :

	if len(filtered_query) < 2 :
		tts.convert_text_n_speak("Sorry your query is incomplete please check")
		return
	#create a directory
	elif "create" in filtered_query  or "make" in filtered_query :
		create_dir(filtered_query)

	#create a directory
	elif "remove" in filtered_query or "delete" in filtered_query :
		remove_dir(filtered_query)
		
	else :
		tts.convert_text_n_speak("Sorry your query is incomplete please check")
		return

query = input("Directory query : ")
filtered_query = query.lower().strip().split()
execute_directory_query(filtered_query)