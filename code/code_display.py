#want to display file contents
#testing display code
import pyperclip
import re
import subprocess
import modules




str = pyperclip.paste() #for bring the content of clipboard to str variable

str_lower = str.lower()


if (str_lower.find("code") !=-1 and
       str_lower.find("snippet") !=-1 and str_lower.find("-safe") !=-1):





    if (re.search(r'\w+\.[a-z,A-Z,0-9]',str_lower)!=None and str_lower.find("-deep")==-1): #filename is given


            str1=str.split(' ') #split() returns a list [ ]

            file_str=str1[(len(str1)-2)]  #in  the first line take the last seconde element of list

            file_str=file_str.replace(".txt"," ") #if filename.txt is given remove txt and search --for all other we need extension


            str2= modules.find(file_str,"/home/nikhil/code_snippets") #finding the directory of the file from where code to be copied



            file1= open(str2,"r")

            pyperclip.copy(file1.read())


    elif (str_lower.find("-deep")!=-1 and re.search("\'[a-z,A-Z,0-9, ]+\'",str_lower)!=None):#text is given and need to grep it

          search_string= re.search("\'[a-z,A-Z,0-9, ]+\'",str_lower)

          if search_string!=None:
              entered_string = search_string.group()
              final_search_string=entered_string[1:len(entered_string)-1]



              try:
                  hosts = subprocess.check_output("grep '%s' /home/nikhil/code_snippets -r" % (final_search_string), shell=True) #http://stackoverflow.com/questions/12809467/how-to-get-output-of-grep-command-python

                  lists=re.findall(r"/[a-z,A-Z,0-9]+\.[a-z]+",hosts)


              #befor using below line e.g:- /ooh.py
                  s=lists[0][1:]

            #after using above line e.g:-ooh.py
                  extension=modules.get_extension(s)
                  print extension

                  file_obj=open('/home/nikhil/code_snippets/'+extension.upper()+'/'+s,'r')

                  pyperclip.copy(file_obj.read())
                  modules.sendmessage("Success..Fetched!")

              except:
                  modules.sendmessage("unable to find")



          else:
              modules.sendmessage("You Entered Non Existing Search String..")
