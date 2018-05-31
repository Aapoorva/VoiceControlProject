#!/usr/bin/env python3

#this is module for admin purpose to create static
#audio files to be used to reduce execution speed 

from tts import convert_txt_n_store

#get input from user
usr_input = input("Text : ")
file_name = input("File Name : ")
#calling method in tts module to convert text and store
convert_txt_n_store(usr_input,file_name)