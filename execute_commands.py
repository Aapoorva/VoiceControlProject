import os
# import pymysql.cursors
import mysql.connector as mariadb
import json
import subprocess
import time
import tts

# #Input from user via mic
# user_input=input("Enter your command:")
def execute_commands(filtered_query) :
    insplit=[]
    #Invalid words which will be removed
    invalid_words=['a','an','the','is','am','are','this','that','do','please','would','you','of','me','could','show','present','my','what','who','me','my','tell','hey','all','in','under','then','will','would','for','there','command','to','find','my','run','execute','tell','year']
    connectionObject=mariadb.connect(host='127.0.0.1',user='root',password='root',database='testdb',charset='utf8mb4')

    try:
        #creating a cursor object
        cursorObject=connectionObject.cursor()

        #creating list after removing inappropriate words
        for my_val in filtered_query:
            if my_val not in invalid_words:
                insplit.append(my_val)

        #converting list to string
        insplit_str=' '.join(insplit)
        #to check whether user has given the command for creating a directory or file
        if(insplit_str.startswith('make') | insplit_str.startswith('create')):
            pass
            # if('directory' in insplit_str):
            #     path=insplit_str.split()
            #     #print(path)
            #     pathvar=path[2:]
            #     str='/'.join(pathvar)
            #     command="mkdir /"+str
            #     #print(command)
            #     proc = subprocess.Popen([command], stdout=subprocess.PIPE, shell=True)
            #     (out, err) = proc.communicate()
            #     print(out.decode())

            # elif('file' in insplit_str):
            #     path=insplit_str.split()
            #     pathvar=path[2:]
            #     str='/'.join(pathvar)
            #     command ="touch /"+str
            #     #print(command)
            #     proc = subprocess.Popen([command], stdout=subprocess.PIPE, shell=True)
            #     (out, err) = proc.communicate()
            #     print(out.decode())

        # elif(insplit_str.startswith('remove') | insplit_str.startswith('delete')):
            # if('directory' in insplit_str):
            #     path=insplit_str.split()
            #     pathvar=path[2:]
            #     str='/'.join(pathvar)
            #     command="rm -rvf /"+str
            #     #print(command)
            #     proc = subprocess.Popen([command], stdout=subprocess.PIPE, shell=True)
            #     (out, err) = proc.communicate()
            #     print(out.decode())

        #     elif('file' in insplit_str):
        #         path=insplit_str.split()
        #         pathvar=path[2:]
        #         str='/'.join(pathvar)
        #         command="rm -rvf /"+str
        #         #print(command)
        #         proc = subprocess.Popen([command], stdout=subprocess.PIPE, shell=True)
        #         (out, err) = proc.communicate()
        #         print(out.decode())

        #for calendar command
        elif(insplit_str.startswith('calendar')):

            #calendar command with year
            cal_query = insplit_str.strip().split()
            attri = "cal"
            for i in range(1,len(cal_query)) :
                attri=attri+" "+cal_query[i]
            
            os.system(attri)
            time.sleep(5)

        else:
            #SQL Query
            var='"'+insplit_str+'"'
            sqlQuery="select command from commands1 where user_input="+var
            #print(sqlQuery)

            #executing sql query
            cursorObject.execute(sqlQuery)

            #fetching data from sql - returning list
            rows=cursorObject.fetchall()
            # checking query fetched or not
            if len(rows) != 0 :
                #fetching command
                print("fetching commands")
                inp=rows[0][0]
                #os.system(inp)
                # s=''.join(val)
                proc = subprocess.Popen([inp], stdout=subprocess.PIPE, shell=True)
                (out, err) = proc.communicate()
                print(out.decode())
                time.sleep(5)
                #print(var12)
            else :
                tts.convert_text_n_speak("Sorry your query is incomplete PLEASE CHECK")
                time.sleep(5)
                return

    except Exception as e:
        #Exception Caught
        print("Exception Occured ",e)

    finally:
        #CLosing the connection
        connectionObject.close()
        return