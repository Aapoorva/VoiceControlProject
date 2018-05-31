#!/usr/bin/env python3

#this module is to execute commands

import subprocess as sp

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