A simple code snippet manager 

How it woks

1) Adding to Code Snippet repository


2)Retrieving from Code Snippet repository (folder on your system)

Dependencies:-

  i)Install pyperclip from pip
  pip install pyperclip
  
  ii)Install xclip
  sudo apt-get install xclip
  
<h4>How it works :</h4>  
  <b>adding to repo</b>:<br>
    add a single line above the code which you want to save to repository of code snippets as :
      add to code snippets filename.extension -safe 
      
  <b>retreiving from the code snippets repo:</b>
    add a single line at a place where you want the code to be used in your current code as:
       from code snippets filename.extension -safe -deep
  


