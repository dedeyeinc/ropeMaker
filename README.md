# ropeMaker
A simple tool for quickly making ropes dynamic or ribbons in Maya. It can create the geo, joints, clusters, and follicles until we add more.


# SETUP INSTRUCTIONS #

1. Click on green button at the top right that says "Code" and then click on "Download ZIP".
2. Extract the ropeMaker-main folder wherever you want, but I recommend somewhere familiar, like 'C:/Users/{username}/Documents/maya/scripts/'.
3. Go to the Setup folder inside of ropeMaker-main and copy the userSetup.py file into your C:/Users/{username}/Documents/maya/scripts/ folder.
4. Make sure to change the code_directory inside the userSetup.py file to match your username or where-ever you're dumping it.

   Here is the setup file, for a better understanding:

```
#Setup

#1 Add the lines below to your Maya userSetup.py. It should be found in user/Documents/maya/scripts.  
#2 If it's not there, then add this file (userSetup.py) to that directory.

#3 code_directory must be set to the directory where you extracted the ropeMaker scripts. This can be anywhere you choose. The default path is set below.
code_directory = 'C:/Users/mathi/Documents/maya/scripts/ropeMaker-main/python' #<-- change only this path, make sure to include quotes. 


#Please don't change any of the following unless you know how it works.
import sys
import maya.utils

if code_directory not in syspath:  
    syspath.insert(0, code_directory)

def run_tools_ui(directory = None):
    ## You can take this code and maker it a button ##
    ## ↓↓↓↓↓↓ ↓↓↓↓↓↓ ↓↓↓↓↓↓ ↓↓↓↓↓↓ ##
    
    from ropeMaker import ropeMakerUI
    import imp
    imp.reload(ropeMakerUI)
    ropeMakerUI.ropeMakerUI()
    
    ## ↑↑↑↑↑↑ ↑↑↑↑↑↑ ↑↑↑↑↑↑ ↑↑↑↑↑↑ ##
    ## You can take this code and maker it a button ##
    
maya.utils.executeDeferred(run_tools_ui)```
