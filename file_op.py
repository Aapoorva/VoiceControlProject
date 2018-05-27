#!/usr/bin/python3

import os

# enter a text
text = input("Please give some input regarding file operation:\n")
list_text = text.strip().split()
print(list_text)
abs_file_path = ""
path = ""

# for opening file
def open_file(path):
	#open the desired file
	f=open(path,'r')
	if "read" in list_text:
		os.system("chmod -w "+path)
		os.system("gedit "+path)
	elif "write" in list_text:
		os.system("chmod +w "+path)
		os.system("gedit "+path)
	f.close()


#for copying file
def copy_file(source_file,dest_file):
	sf = open(source_file,'r')
	data = sf.read()
	sf.close()
	df = open(dest_file,'w')
	df.write(data)
	df.close()

# for deleting specific file
def delete_file(file_name):
	os.remove(file_name)	

# for deleting folder
def delete_folder(folder_name):
	os.rmdir(folder_name)



# for creating file:
def create_file(file_name):
	f=open(file_name,'w+')

#for getting file path
def file_path():
	try :
		if "file" in list_text:
			print("fileoperation possible")
			if "open" in list_text:
				#get index of file in text
				index = list_text.index("file")
				# fetch file name
				file_name = list_text[index+1]
						


				if file_name=="":
					os.system("echo please speak some file name|festival --tts")
			
				else:
					if "folder" in list_text:
						index_folder = list_text.index("folder")
						folder_name = list_text[index_folder+1]
					else:
						folder_name = "."

				# the final path of file is	
				script_dir = os.path.dirname(folder_name)
				rel_path = file_name
				abs_file_path = os.path.join(script_dir,rel_path)
				open_file(abs_file_path)
		
			
			elif "copy" in list_text:
					#get 1st file name
					index = list_text.index("file")
					file1 = list_text[index+1]
					list_text.remove("file")
					#get 2nd file name
					index = list_text.index("file")
					file2 = list_text[index+1]
					list_text.remove("file") 

					#check if input files are correct				
					if file1=="" or file2=="":
						os.system("echo please check file names something is missing|festival --tts")
					else:
						if "folder" in list_text:
							index = list_text.index("folder")
							folder1 = list_text[index+1]
							list_text.remove("folder")
						
						else:
							folder1 = "."
						if "folder" in list_text:
							index = list_text.index("folder")
							folder2 = list_file[index+1]
							list_text.remove("folder")
						else:
							folder2 = "."
			
					script_dir1 = os.path.dirname(folder1)
					rel_path1 = file1
					source_file = os.path.join(script_dir1,rel_path1)
					script_dir2 = os.path.dirname(folder2)
					rel_path2 = file2
					dest_file = os.path.join(script_dir2,rel_path2)
					copy_file(source_file,dest_file)
			
			elif "delete" in list_text:
				#get index of file in text
				index = list_text.index("file")
				# fetch file name
				file_name = list_text[index+1]
						


				if file_name=="":
					os.system("echo please speak some file name|festival --tts")
			
				else:
					if "folder" in list_text:
						index_folder = list_text.index("folder")
						folder_name = list_text[index_folder+1]
					else:
						folder_name = "."

				# the final path of file is	
				script_dir = os.path.dirname(folder_name)
				rel_path = file_name
				abs_file_path = os.path.join(script_dir,rel_path)
				delete_file(abs_file_path)
		
			elif "create" in list_text:
				#get index of file in text
				index = list_text.index("file")
				# fetch file name
				file_name = list_text[index+1]
						

				if file_name=="":
					os.system("echo please speak some file name|festival --tts")
			
				else:
					if "folder" in list_text:
						index_folder = list_text.index("folder")
						folder_name = list_text[index_folder+1]
					else:
						folder_name = "."

				# the final path of file is	
				script_dir = os.path.dirname(folder_name)
				rel_path = file_name
				abs_file_path = os.path.join(script_dir,rel_path)
				create_file(abs_file_path)
				



		elif "folder" in list_text:
			folder_name = list_text[list_text.index("folder")+1]
			delete_folder(folder_name)
	

		else:
			print("No operation regarding file can be done!! sorry check ur input text !!")


	except IOError:
		os.system("echo The file not found|festival --tts")


			
	


# call definition of file_path()
file_path()
	










'''
#!/usr/bin/python3

import os

script_dir = os.path.dirname("/home/bhavyaagrawal/backup_ubuntu/ML_Projects/") #<-- absolute dir the script is in
rel_path = "stt_demo.py"
abs_file_path = os.path.join(script_dir, rel_path)

print(type(abs_file_path))

f=open(abs_file_path,'r')
os.system("gedit "+abs_file_path)
f.close() '''


