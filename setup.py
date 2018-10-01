import cx_Freeze
import sys
import os
import matplotlib
os.environ['TCL_LIBRARY']="C://LOCAL_TO_PYTHON\\Python35-32\\tcl\\tcl8.6"
os.environ['TK_LIBRARY']="C://LOCAL_TO_PYTHON\\Python35-32\\tcl\\tk8.6"
base=None
if sys.platform=='win32':
    base='Win32GUI'
executables = [cx_Freeze.Executable('ftoneanalyser.py',base=None)]
cx_Freeze.setup(
     name="Helpwiththemood",
	 options={"build_exe":{"packages":["urllib.request","urllib.parse","re","webbrowser","json","tweepy","datetime","collections","sys","twitter","emoji","regex","watson_developer_cloud","tkinter"]}},
	 version="0.01",
	 description="Find the mood on the basis of the tweets by the user, need to provide the screen naame only",
	 executables=executables
	 )
