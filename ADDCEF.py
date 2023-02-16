#Written by AdditionalRAM
#AddCEF Project
#Converts any web project to standalone windows application
#using miniweb and Chromium Embedded Framework

#Prerequisites: Install Python 3.9 (no newer) and
#move this script to your Scripts folder

#You need an internet connection on the first run
#After first run all required files are downloaded and
#you can run it without an internet connection too

#Your end users will NOT need an internet connection to run the app

#change the variables below in order to personalize
#NOTE : Script name determines the name of the .exe file of the build!

miniwebname = "addcefout_sub.exe" #changed name of miniweb.exe
scriptname = "addcef_out.py" #name of generated script and EXE file
windowname = "test window" #name of CEF window
port = 42069 #port miniweb runs on

import os
import time
import urllib.request
import zipfile
import subprocess

try:
    import cefpython3
except ImportError as e:
    print ("cefpython3 not found. Attempting install...")
    os.system("pip install cefpython3")
    import cefpython3
    pass

try:
    import nuitka
except ImportError as e:
    print ("nuitka not found. Attempting install...")
    os.system("pip install nuitka")
    import nuitka
    pass

print ("All required modules installed, proceeding")
if not os.path.exists("AddcefOut"):
    os.mkdir("AddcefOut")
    print ("Directory AddcefOut created")
if not os.path.exists("AddcefOut\\htdocs"):
    os.mkdir("AddcefOut\\htdocs")
    print ("Directory htdocs created in AddcefOut")

else:
    print ("Directory AddcefOut already exists, proceeding")
print ("Downloading miniweb")
urllib.request.urlretrieve("https://github.com/avih/miniweb/releases/download/snapshot-2017-09-17/miniweb-2017-09-17.zip", "miniweb.zip")
print ("Downloaded miniweb, unzipping")
with zipfile.ZipFile(os.getcwd()+"\\miniweb.zip", 'r') as zip_ref:
    zip_ref.extractall(os.getcwd()+"\\AddcefOut")
os.system("ren AddcefOut\\miniweb.exe " + miniwebname)
print ("unzipped, running")
cmd = os.getcwd()+"\\AddcefOut\\" + miniwebname
process = subprocess.Popen([cmd, "-p", str(port)], stdout=subprocess.PIPE, creationflags=0x08000000)
time.sleep(3)
process.kill()
print("run complete")
##download addcefout.py
print("copying python script")
os.system("copy addcefout.py addcefout\\" + scriptname)
with open(os.getcwd() + "\\addcefout\\" + scriptname, "r+") as f:
    f.seek(84)
    old = f.read()
    f.seek(84)
    f.write("windowname = \"" + windowname +"\"\nport = "+str(port)+"\nminiwebname = \""+miniwebname+"\"\n" + old)
print("copied and modified python script successfully")
print("starting nuitka build, good luck!")
os.system("nuitka addcefout\\"+scriptname+" --standalone --windows-disable-console")
print("nuitka build complete. moving files")
os.system("xcopy " + scriptname[:-3] + ".dist addcefout /h /i /c /k /e /r /y")
os.system("del /s /q " + scriptname[:-3] + ".dist")
os.system("del /s /q " + scriptname[:-3] + ".build")
os.system("del /q AddcefOut\\" + scriptname)
print("build complete. move files into htdocs before running!")
print ("Thank you for using AddCEF by AdditionalRAM")
