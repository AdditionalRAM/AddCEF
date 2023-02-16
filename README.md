# AddCEF
Wrap any web project for use on windows computers using Nuitka, CEF and miniweb

# How it works
-Downloads miniweb from https://github.com/avih/miniweb/releases/  
-Creates python script to first launch miniweb and then CEF to load the webpage  
-Uses Nuitka to build the python script into Windows executable  

# How to use
-Download and install Python 3.9 (newer versions don't work)  
-Download ADDCEF.py and addcefout.py and copy them into your scripts folder (default is C:\Users\user\AppData\Local\Programs\Python\Python39\Scripts)  
-Edit the variables at the start of ADDCEF.py for your personal project (lines 18-21)  
-Run ADDCEF.py  
-Move web project into AddcefOut/htdocs (index.html should be at AddcefOut/htdocs/index.html)  
-Enjoy!
