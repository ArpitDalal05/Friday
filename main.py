import os
import eel

eel.init("FrontEnd")
os.system('start msedge.exe --app="http://localhost:8000/index.html"')
eel.start('index.html',mode=None,host='localhost',block=True)