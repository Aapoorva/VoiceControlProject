#!/usr/bin/python3
import os
import os.path
import tts
import SpeechRego as sr

global operation
operation = 0

#to get path
def path(operation,file_names,folder):
	
	script_dir = os.path.dirname(folder)
	if file_names == []:
		rel_path=""
	else:
		rel_path = file_names[0]
	abs_file_path = os.path.join(script_dir,rel_path)

	if operation==1:
		open_file(abs_file_path)
	elif operation == 2:
		create_file(abs_file_path)
	elif operation == 3:
		delete_file(abs_file_path)
	elif operation==4:
		rename_file(script_dir,file_names[0],file_names[1])
	elif operation == 6:
		list_files(script_dir)

#open file
def open_file(path):
	os.system("gedit "+path)
	tts.convert_text_n_speak("File opened")

#create file
def create_file(path):
	f=open(path,'a')
	os.system("gedit "+path)
	tts.convert_text_n_speak("File Created")

#delete file
def delete_file(path):
	tts.convert_text_n_speak("Are you sure ? ")
	user_input = sr.get_audio_to_text()
	if user_input.find("yes") != -1 :
		os.remove(path)
	else :
		tts.convert_text_n_speak("Aage se dhyan rakhna")

# renaming file
def rename_file(folder,file1,file2):
	path1 = os.path.join(folder,file1)
	f1 = open(path1,'r')
	data = f1.read()
	path2 = os.path.join(folder,file2)
	f2 = open(path2,'w')
	f2.write(data)
	os.remove(path1)

#for listing files of a folder
def list_files(folder_name):
	os.system("cd "+folder_name+";ls -l")

#main trigger function
def call_file(list_text):
	folder=""
	count=0
	index = 0
	index1=0
	length = len(list_text)
	valid_file_op = []
	file_names = []
	data = ""
	entered = 0
	value = 0
	
	for i in list_text:
		print(i)
		if i=="open" or i=="copy" or i=="create" or i=="close" or i=="delete" or i=="rename" or i=="list":
			valid_file_op.append(i)
			#list_text.remove(i)
			del i

		elif i=="file":
			
			index = list_text.index("file")
			file_name = list_text[index+1]
			file_names.append(file_name)
			print(file_names)
			list_text.remove(i)

		elif  i=="in" or i=="of" or i=="from":
			if "current" in list_text:
				folder = "."	
			else:	
				index1 = list_text.index(i)
				folder = list_text[index1+2]+"/"+folder
				list_text.remove(i)	

			if "home" in list_text:
				entered = 1
				index = list_text.index("home")
				list_text.remove(list_text[index-1])
				list_text.remove("home")
			
		elif i=="to":
			folders.append(folder)

		else:
			pass

		count+=1

		if(count==length):
			break

		else:
			continue
	# out of for loop
	if folder == ".":
		folder="./"

	else:
		if entered == 1:
			folder = "/home/bhavyaagrawal/"+folder
		else:
			folder="/"+folder
			
	
# call specific function regarding file path
	for i in valid_file_op:
		
		if i == "open":
			path(1,file_names,folder)
			
		elif i =="create":
			path(2,file_names,folder)
			
		elif i == "delete":
			path(3,file_names,folder)
			
		elif i == "rename":
			path(4,file_names,folder)
	
		elif i == "copy":
			path(5,file_names,folders)
		elif i=="list":
			path(6,[],folder)