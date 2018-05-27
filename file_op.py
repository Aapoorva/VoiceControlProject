#!/usr/bin/python3

import os

# enter a text
text = input("Please give some input regarding file operation:\n")
list_text = text.strip().split()
print(list_text)
abs_file_path = ""
path = ""

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
			''''path = str(folder_name+"/"+file_name)
			print(path)
			open_file()'''
			script_dir = os.path.dirname(folder_name)
			rel_path = file_name
			abs_file_path = os.path.join(script_dir,rel_path)
			open_file(abs_file_path)
		

	
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


