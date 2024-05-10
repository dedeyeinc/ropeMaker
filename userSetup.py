
#Setup

#1 Add the lines below to your Maya userSetup.py. It should be found in user/Documents/maya/scripts.  
#2 If it's not there, then add this file (userSetup.py) to that directory.

#3 code_directory must be set to the directory where you extracted the ropeMaker scripts. This can be anywhere you choose. The default path is set below.
code_directory = 'C:/Users/{username}/Documents/maya/scripts/python' #<-- change only this path, make sure to include quotes. 


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
    
maya.utils.executeDeferred(run_tools_ui)