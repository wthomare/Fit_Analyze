# -*- coding: utf-8 -*-
import os

execPath = os.getcwd()
userPath = os.getcwd()

def main():
    import os, sys
    global execPath, userPath

    # Path
    try:
        sys.path.append(execPath)
        os.chdir(execPath)
    except OSError as msg:
        OSError("Error while setting path: ", msg)


    from FitUIApp import FitUIApp
    app = FitUIApp(0)
    app.MainLoop()
    app = None
    
if __name__ == "__main__":
    execPath = os.getcwd()
    main()