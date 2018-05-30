#!/usr/bin/python3

import os
import os.path


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

	script_dir2 = os.path.dirname(folders[1])
	rel_path2 = files[1]
	dest_path = os.path.join(script_dir2,rel_path2)

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
	entered = 0
	entered_to = 0
	entered = 0
	try:
		for i in list_text:
			if i == "file":
				files.append(list_text[list_text.index(i)+1])
				list_text.remove("file")
				print(list_text)
			
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
			if  i=="in" or i=="of" or i=="from":
				index1 = source.index(i)
				if source[index1+1]=="home":
					entered = 1
					del i
				elif source[index1+1]=="current":
					current = 1
					del i
				else :
					folder1 = source[index1+2]+"/"+folder1
					source.remove(i)			

		if current == 1:
			folder1="./"+folder1

		else:
			if entered == 1:
				folder1 = "/home/bhavyaagrawal/"+folder1
			else:
				folder1="/"+folder1
		entered = 0
		current = 0
		folders.append(folder1)
		
	
		# for destination folder
		for i in dest:
			if  i=="in" or i=="of" or i=="from":
				index1 = dest.index(i)
				if dest[index1+1]=="home":
					entered = 1
					del i
				elif dest[index1+1]=="current":
					current = 1
					del i
				else :
					folder2 = dest[index1+2]+"/"+folder2
					dest.remove(i)			

			
		if current == 1:
			folder2="./"+folder2

		else:
			if entered == 1:
				folder2 = "/home/bhavyaagrawal/"+folder2
			else:
				folder2="/"+folder2
		
		folders.append(folder2)
		print(files)
		print(folders)
		path(files,folders)

		

	except IOError:
		print("invalid input")

take_in()






