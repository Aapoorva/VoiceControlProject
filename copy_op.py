#!/usr/bin/python3

import os
import os.path
import subprocess as sp
import tts
import SpeechRego as sr


def take_in():
	text = input("enter the text\n")
	list_text = text.strip().split()
	call_copy(list_text)

# for copy operation
def copy_file(source,destination):
	f = open(source,'r')
	data = f.read()
	f.close()
	f2= open(destination,'w')
	f2.write(data)
	f2.close()



#for getting path
def path(files,folders):

	script_dir1 = os.path.dirname(folders[0])
	rel_path1 = files[0]
	source_path = os.path.join(script_dir1,rel_path1)

	#checking path validity
	if source_path == "/" :
		tts.convert_text_n_speak("Sorry but Path is invalid")

	#checking file path exists or not

	elif os.path.exists(source_path) :
		pass

	script_dir2 = os.path.dirname(folders[1])
	rel_path2 = files[0]
	dest_path = os.path.join(script_dir2,rel_path2)

	#checking path validity
	if dest_path == "/" :
		tts.convert_text_n_speak("Sorry but Path is invalid")

	#checking file path exists or not

	elif os.path.exists(dest_path) :
		pass
	
	# call copy function
	copy_file(source_path,dest_path)



# main trigger function
def call_copy(list_text):
	files = []
	folders = []
	source = []
	dest = []
	folder1 = ""
	folder2 =""
	current = 0
	entered_to = 0
	entered = 0
	try:
		for i in list_text:
			if i == "file":
				index = list_text.index("file")
				if list_text[-1]=="file":
					#file_name = input("enter file name\n")
				 	tts.convert_text_n_speak("what is the file name")
					file_name = sr.get_audio.to_text()
					files.append(file_name)
				else:
					files.append(list_text[list_text.index(i)+1])

				list_text.remove("file")

				if "from folder" not in list_text and "from directory" not in list_text and "to folder" not in list_text and "to directory" not in list_text:
					#source1 = input("enter source directory\n")
					tts.convert_text_n_speak("what is the source directory")
					source1 = sr.get_audio_to_text()
					source = source1.strip().split()
					#dest1 = input("enter destination directory\n")
					tts.convert_text_n_speak("what is the destination directory")
					dest1 = sr.get_audio_to_text()
					dest = dest1.strip().split()
					
									
				else:
					pass

			
			# dividing list in 2 parts
			elif i == "to" or "into":
				if entered_to == 1:
					pass
				else:
					index = list_text.index("to")


					for j in range(0,index):
						source.append(list_text[j])
					for j in range(index,len(list_text)):
						dest.append(list_text[j])
					del i
					entered_to =1
		
		# for source folder
		for i in source:
			if i == "folder" or i == "directory":
				index1 = source.index(i)
				if source[index1-1]=="home":
					entered = 1
					del i
				elif source[index1-1]=="current":
					current = 1
					del i
				elif source[index1-1]!="home" and source[index1-1]!="current" and i!=source[-1]:
					folder1 = source[index1+1]+"/"+folder1
					source.remove(i)			

		if current == 1:
			folder1="./"+folder1

		elif entered == 1:
			output=sp.run(['echo $USER'],shell=True,stdout=sp.PIPE)
			user=output.stdout.decode().replace('\n','')

			folder1 = "/home/" + user +"/" + folder1

		else:
			folder1="/"+folder1
		entered = 0
		current = 0

		folders.append(folder1)
	
		# for destination folder
		for i in dest:
			#if  i=="in" or i=="of" or i=="from":
			if i == "folder" or i == "directory":
				index1 = dest.index(i)
				if dest[index1-1]=="home":
					entered = 1
					del i
				elif dest[index1-1]=="current":
					current = 1
					del i
				elif dest[index1-1]!="home" and dest[index1-1]!="current" and i!=dest[-1]:
					folder2 = dest[index1+1]+"/"+folder2
					#dest.remove(i)
					del i			

			
		if current == 1:
			folder2="./"+folder2

		elif entered == 1:
			output=sp.run(['echo $USER'],shell=True,stdout=sp.PIPE)
			user=output.stdout.decode().replace('\n','')

			folder2 = "/home/" + user +"/" + folder2

		else:
			folder2="/"+folder2
		
		folders.append(folder2)	

		# get path of source and destination files
		path(files,folders)

		

	except IOError:
		tts.convert_text_n_speak("invalid input")

#take_in()






