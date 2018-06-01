#!/usr/bin/python3
import os
import os.path
import SpeechRego as sr
#import pyaudio
#from gtts import gTTS
import tts  
import copy_op
import subprocess as sp 

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
	
	#checking path validity
	if abs_file_path == "/" :
		tts.convert_text_n_speak("Sorry but Path is invalid")

	#checking file path exists or not

	elif os.path.exists(abs_file_path) :
		if operation==1:
			open_file(abs_file_path)
		elif operation == 3:
			delete_file(abs_file_path)
		elif operation==4:
			rename_file(script_dir,file_names[0],file_names[1])
		elif operation == 6:
			list_files(script_dir)	

	else:
		if operation == 2:
			create_file(abs_file_path)
		else:
			tts.convert_text_n_speak("Sorry file not found")

# taking input
#def call(list_text):
def call():
	new_list = 0
	file_names = []
	valid_file_op = []
	text = input("Enter the text\n")
	list_text = text.strip().split()
	call_file(list_text,new_list,file_names,valid_file_op)	

#open file
def open_file(path):
	print("open entered")
	os.system("gedit "+path)
	tts.convert_text_n_speak("file opened")

#create file
def create_file(path):
	f=open(path,'a')
	os.system("gedit "+path)
	tts.convert_text_n_speak("file created")

#delete file
def delete_file(path):
	
	tts.convert_text_n_speak("are u sure to delete file")
	input_text = sr.get_audio_to_text()
	if input_text.find("yes")!=-1:
		os.remove(path)
		tts.convert_text_n_speak("Ok fine!!file deleted ,check it once")
	else:
		tts.convert_text_n_speak("aage se dhyan rakhna")

# renaming file
def rename_file(folder,file1,file2):
	path1 = os.path.join(folder,file1)
	f1 = open(path1,'r')
	data = f1.read()
	path2 = os.path.join(folder,file2)
	f2 = open(path2,'w')
	f2.write(data)
	os.remove(path1)
	tts.convert_text_n_speak("file is renamed check it once")

#for listing files of a folder
def list_files(folder_name):
	tts.convert_text_n_speak("see the list of files below")
	os.system("cd "+folder_name+";ls -l")




#main trigger function
def call_file(list_text,new_list,file_names,valid_file_op):
	folder=""
	count=0
	index = 0
	index1=0
	length = len(list_text)
	entered = 0
	value = 0
	current = 0
	c = 0
	list_text1 = ""

	try:
		if new_list == 1:
			new_list = 0
	
		for i in list_text:

			count+=1
			if i=="open"  or i=="create" or i=="close" or i=="delete" or i=="rename" or i=="list":
				index = list_text.index(i)
				if i in valid_file_op:
					pass
				else:
					valid_file_op.append(i)
				del i				

			elif i=="copy":
				list_text.remove("copy")
				copy_op.call_copy(list_text)

			elif i=="file":
			
				index1 = list_text.index(i)
				if list_text[-1]=="file":
					tts.convert_text_n_speak("please give the file name sir!!")
					file_name = sr.get_audio_to_text()
					#file_name = input("enter file")
					file_names.append(file_name)
				else:
					file_name = list_text[list_text.index("file")+1]
					file_names.append(file_name)
					list_text.remove("file")						

				#to check whether folder name is given or not
				if "folder" not in list_text and "directory" not in list_text:
					tts.convert_text_n_speak("what is the desired location of the file!!")
					list_text1  = sr.get_audio_to_text()
					#list_text1 = input("enter location")
					list_text = list_text1.strip().split()
					length = len(list_text)
					new_list = 1
					count = 0
					call_file(list_text,new_list,file_names,valid_file_op)
					
				else:
					pass
 
 
			elif  i=="folder" or i=="directory":

				index1 = list_text.index(i)
							 
				if list_text[index1-1]=="home":
					entered = 1
					del i
					#list_text.remove(i)

				elif list_text[index1-1]=="current":
					current = 1
					del i
					#list_text.remove(i)	

				elif list_text[index1-1]!="home" and list_text[index1-1]!="current" and i!=list_text[-1]:
					folder = list_text[index1+1]+"/"+folder
					#del i
					list_text.remove(i)			
			
			else:
				#pass
				c=0

			if count == length:
				break

			else:
				#continue
				c=0				

		# out of for loop
		if current == 1:
			folder="./"+folder

		elif entered == 1:
			#to fetch user name			
			output=sp.run(['echo $USER'],shell=True,stdout=sp.PIPE)
			user=output.stdout.decode().replace('\n','')

			folder = "/home/" + user +"/" + folder
				
		else:	
			folder="/"+folder

		for i in valid_file_op:
			
			if i == "open":
				path(1,file_names,folder)
				
			elif i == "create":
				path(2,file_names,folder)
				
			elif i == "delete":
				path(3,file_names,folder)
				
			elif i == "rename":
				if len(file_names) == 1:
					tts.convert_text_n_speak("what do u want to be the new name of ur file")
					file_name = sr.get_audio_to_text()
					file_names.append(file_name)
				else:
					pass
				path(4,file_names,folder)
	
			elif i == "copy":
				path(5,file_names,folders)
			elif i=="list":
				path(6,[],folder)

		

	except IOError:
		tts.convert_text_n_speak("something might be missing or maybe you don't have appropriate permissions please check your input once")

call()
