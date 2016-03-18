#!/usr/bin/env python
#want to display file contents
#testing display code


import pyperclip
import re
import subprocess

import os,sys,time

counter=1

already_checked=''

def get_extension(file_name):
    if file_name.find('.')!=-1:

        ext = file_name.split('.')

        return (ext[1])
    else:

        return 'txt'


def cut(str, len1):
    return str[len1 + 1:]  #to remove first line which is meant for reading from which file



#for displaying contents
def find(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)



#ubuntu notification (message sending)
def sendmessage(message):
    subprocess.Popen(['notify-send', message])
    return






while(True):
 str = pyperclip.paste() #for bring the content of clipboard to str variable

 str_low= str.lower()
 str_lower =str_low.split("\n")

 if(str_lower[0]=="stop -safe"):
        sendmessage("Stopped the background process for code snippet management...byebye")

        os.exit()




 if (str_lower[0].find("from")!=-1 and str_lower[0].find("code") !=-1 and
       str_lower[0].find("snippet") !=-1 and str_lower[0].find("-safe") !=-1):









    if (re.search(r'\w+\.[a-z,A-Z,0-9]',str_lower[0])!=None and str_lower[0].find("-deep")==-1): #filename is given


            str1=str.split(' ') #split() returns a list [ ]

            file_str=str1[(len(str1)-2)]  #in  the first line take the last seconde element of list

            file_str=file_str.replace(".txt"," ") #if filename.txt is given remove txt and search --for all other we need extension
            if(file_str==already_checked):
                continue



            str2= find(file_str,"/home/nikhil/code_snippets") #finding the directory of the file from where code to be copied


            try:
              file1= open(str2,"r")

            except:
              print "ohhh mann"
              sendmessage("file not found in codesnippets sorry")
              already_checked=file_str
              continue


            pyperclip.copy(file1.read())
            sendmessage("Fetched press ctrl+v")


    elif (str_lower[0].find("-deep")!=-1 and re.search("\'[a-z,A-Z,0-9, ]+\'",str_lower[0])!=None):#text is given and need to grep it

          search_string= re.search("\'[a-z,A-Z,0-9, ]+\'",str_lower[0])

          if search_string!=None:
              entered_string = search_string.group()
              final_search_string=entered_string[1:len(entered_string)-1]



              try:
                  hosts = subprocess.check_output("grep '%s' /home/nikhil/code_snippets -r" % (final_search_string), shell=True) #http://stackoverflow.com/questions/12809467/how-to-get-output-of-grep-command-python

                  lists=re.findall(r"/[a-z,A-Z,0-9]+\.[a-z]+",hosts)


              #befor using below line e.g:- /ooh.py
                  s=lists[0][1:]

            #after using above line e.g:-ooh.py
                  extension=get_extension(s)
                  print extension

                  file_obj=open('/home/nikhil/code_snippets/'+extension.upper()+'/'+s,'r')

                  pyperclip.copy(file_obj.read())
                  sendmessage("Success..Fetched!")

              except:
                  sendmessage("unable to find")



          else:
              sendmessage("You Entered Non Existing Search String..")












os.system('python /home/nikhil/Desktop/haha.py')


#todo file not found exception is being raised --unlimited times
#same comment in multiple files means it is showing only first file with that comment --handle this
