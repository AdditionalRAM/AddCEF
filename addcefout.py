from cefpython3 import cefpython as cef
import sys
import os
import subprocess



def main():
    host_webserver()
    sys.excepthook = cef.ExceptHook  # To shutdown all CEF processes on error
    cef.Initialize()
    cef.CreateBrowserSync(url="localhost:" + str(port),
                          window_title=windowname)
    cef.MessageLoop()
    cef.Shutdown()

def host_webserver():
    cmd = os.getcwd()+"\\" + miniwebname
    global process
    process = subprocess.Popen([cmd, "-p", str(port)], stdout=subprocess.PIPE, creationflags=0x08000000)

main()
process.kill()