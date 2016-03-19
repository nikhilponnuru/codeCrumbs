A very simple code snippet manager to manage your code from any IDE

How it woks

this uility currently has two parts 1)adding to code snippet manager 2)fetching from that manager

<strong>Note</strong>:-- use the command , here means copy that command to clipboard using <strong>ctrl+c </strong> and to get the      results use <strong>ctrl+v</strong>

<h4>1) Adding to Code Snippet repository</h4>


whichever lines of code you want to store or manage, above those lines of code mention a single as command 

 
    command:-- add to code snippets filename.extension -safe 

 
copy the block of code along with the above command (first line must be command) to the clipboard (i.e ctrl+c )and that does everything 

<strong>or</strong>

you can even add other logic to the same filename (i.e append other logic to existing file)
  to differentiate between different logics existing in same file, "@@" symbols are used to seperate them inside the file
 


the above command will add the code into the respective folders (e.g:-if "sample.py" is filename then it saves the code in code_snippets > PY >sample.py

![alt tag](https://github.com/nikhilponnuru/codeCrumbs/blob/master/screenshots/add.gif)




<h4>2)Retrieving from code_snippet repository (folder on your system)</h4>

to retrieve any logic or code you have stored all you need to do is use the below command and copy that to clipboard

    command:- from code snippets filename.py -safe


<strong>or</strong>

if you can't remember the filename, you can mention any of the comment or word in that file

    command:-from code snippets 'comment or any word' -safe -deep

![alt tag](https://github.com/nikhilponnuru/codeCrumbs/blob/master/screenshots/fetch.gif)




at any time you can stop the python script running back by copying the below command to clipboard


     command:-stop -safe





<strong>Dependencies:-</strong>
 
  i)Install <a href="https://pypi.python.org/pypi/pyperclip"> pyperclip</a> from pip
  
      pip install pyperclip
  
  ii)Install xclip
  
      sudo apt-get install xclip
  
after installing the above 

if you want to fetch the code or logic that was already stored

     go to -- codeCrumbs/code/ 
     then chmod +x codedisplay.sh and then ./codedisplay.sh 


or
if you want to store or add logic or code to code_Snippet manager then 
   
     chmod +x create_file.sh and
      then ./create_file.sh

Note:-you can <strong>force</strong> close your terminal after executing the above commands,then the script starts running in background and you can stop the above background running process at any time by copying command:-- <strong>stop -safe </strong>


<h3>TODO:--</h3>
1)Combine fetch and display parts of above utility to one so that only one script can be made to run and that does the above 2 features in a single execution (since now both scripts must be individually executed and that is tieresome)





