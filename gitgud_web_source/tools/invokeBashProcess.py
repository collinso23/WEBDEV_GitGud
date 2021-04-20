import subprocess as sp
from subprocess import PIPE
import sys
 
"""
This is a very generic function. It will work with any of the bash tools not just the network tools for this project 
currently has complex usage. It allows for full bash like functions with the param arg
as the arguments are not properly caputre you can use stdin, pipe, newline, ect to escape the program.
Returns a formated string with the output from the subprocess.
#runTool(tool,params)
"""
def runTool(toolName,parameters):
    output=sp.run(["bash","-c", f"{toolName} {parameters}"], stdout=PIPE, stderr=PIPE, universal_newlines=True)
    return f"Return Code:\n{output.returncode}\nStdout:\n{output.stdout}\nSterror:\n{output.stderr}"





#### TESTING ZONE ####
"""
Testing tool only
Takes a destination as IP or url, spawns a subprocess.
The below tool works from the cli
python3 sh_with_py.py mtr -rz -c10 8.8.8.8
"""
def argTool(*args):
    parameters=' '.join(args[1:])
    print(f"{parameters}")
    sp.run(["bash", "-c", f"{parameters}"])   

params=sys.argv
#Take all arguments except 0 <- which is the python command being run
print(f"{params}")
#argTool(params)