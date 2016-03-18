#!/usr/bin/env python

#to create a file in codesnippets folder
import pyperclip
import os
import re
import subprocess


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


while True:
    str = pyperclip.paste()
    if (str==" "):
        continue

    str_low = str.lower()

    str_lower=str_low.split("\n")  #this is to ensure that only create a file if "add to code snippets" line is first line since if this line is present with other text which is not intended to be saved (i.e in btw that unwanted text
    #as we are using regular expression it checks a pattern in a given text so "add to code snippets " must be definitely first line

    if(str_lower[0]=="stop -safe"):
        sendmessage("Stopped the background process for code snippet management...byebye")

        os.exit()


    if (str_lower[0].find("add") != -1 and str_lower[0].find("code")!=-1 and
           str_lower[0].find("snippets") !=-1  and str_lower[0].find("-safe") !=-1 ):

        if re.search(r'\w+\.[a-z,A-Z]',str_lower[0])==None:
            sendmessage("SPECIFY FILEEXTENSION (default file type is txt)")



        str1 = str.split('\n')

        str2 = str1[0].split(' ')

        length = len(str2)
        file_name = str2[length - 2]

        new_str = cut(str, len(str1[0]))


        # until here we removed first line which contains " add this to code snippet filename"
        # print new_str

        # creating a file with the above name


        try:


            # code_snippets is the head folder

            if not os.path.exists('/home/nikhil/code_snippets'):
             os.makedirs('/home/nikhil/code_snippets')  # creating the directory if not exists


            extension = get_extension(file_name)




             # creating a folder with respective extenion names in uppercase

            if not os.path.exists('/home/nikhil/code_snippets/'
                              + extension.upper()):
             os.makedirs('/home/nikhil/code_snippets/' + extension.upper())
             print

        # creating a file in respective folder
            if not os.path.exists('/home/nikhil/code_snippets/' + extension.upper() + '/'
                    + file_name):
              name = open('/home/nikhil/code_snippets/' + extension.upper() + '/'
                    + file_name, 'w')

            name.write(new_str)
            name.truncate()
            name.close()
            sendmessage("successfully added to code snippets collection")
            pyperclip.copy(" ")


        except Exception:



            try:




                 already_exists = open('/home/nikhil/code_snippets/' + extension.upper() + '/'
                    + file_name, 'a+')

                 #new_str = cut(str, len(str1[0]))


                 str_from_file = already_exists.read()
                   #already_exists.seek(0) #http://stackoverflow.com/questions/6648493/open-file-for-both-reading-and-writing#answer-15976014



                 already_exists.write('\n\n@@\n'+new_str)

                 already_exists.truncate()

                 already_exists.close()

                 sendmessage("successfully added to code snippets collection  (code has been appended to already existing file with same name)")
                 str=pyperclip.copy(" ")


            except:
                  print "oops some error in finding file to append content"
                  sendmessage("ERROR OCCURED")
                  pyperclip.copy(" ")




os.system('python /home/nikhil/Desktop/haha.py')

