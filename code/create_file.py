#!/usr/bin/python

#to create a file in codesnippets folder
import pyperclip
import os
import re
import modules





str = pyperclip.paste()

str_lower=str.lower() #this is to ensure uniformity even if upper case or lower case or both are used


if (str_lower.find("add") != -1 and str_lower.find("code")!=-1 and
       str_lower.find("snippets") !=-1  and str_lower.find("-safe") !=-1 ):

    if re.search(r'\w+\.[a-z,A-Z]',str_lower)==None:
        modules.sendmessage("SPECIFY FILEEXTENSION (default file type is txt)")



    str1 = str.split('\n')

    str2 = str1[0].split(' ')
    length = len(str2)
    file_name = str2[length - 2]

    new_str = modules.cut(str, len(str1[0]))


    # until here we removed first line which contains " add this to code snippet filename"
    # print new_str

    # creating a file with the above name

    try:


        # code_snippets is the head folder

        if not os.path.exists('/home/nikhil/code_snippets'):
         os.makedirs('/home/nikhil/code_snippets')  # creating the directory if not exists


        extension = modules.get_extension(file_name)




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
        modules.sendmessage("successfully added to code snippets collection")


    except Exception:



        try:




             already_exists = open('/home/nikhil/code_snippets/' + extension.upper() + '/'
                + file_name, 'a+')

             #new_str = modules.cut(str, len(str1[0]))


             str_from_file = already_exists.read()
               #already_exists.seek(0) #http://stackoverflow.com/questions/6648493/open-file-for-both-reading-and-writing#answer-15976014



             already_exists.write('\n\n@@\n'+new_str)

             already_exists.truncate()

             already_exists.close()

             modules.sendmessage("successfully added to code snippets collection  (code has been appended to already existing file with same name)")



        except:
              print "oops some error in finding file to append content"
              modules.sendmessage("ERROR OCCURED")
