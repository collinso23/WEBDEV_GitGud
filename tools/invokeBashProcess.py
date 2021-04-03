import subprocess as sp
from subprocess import PIPE
import sys
 
"""
This is a very generic function. It will work with any of the bash tools not just the network tools for this project 
currently has complex usage. It allows for full bash like functions with the param arg
as the arguments are not properly caputre you can use stdin, pipe, newline, ect to escape the program.
example usage: python3 sh_with_py.sh
enter a tool to test: whois
enter a destination: AS6079


#runTool(tool,params)
"""
def runTool():
    toolName = input ("enter a tool to test: ")
    params = input ("enter parameters: ")
    print(f"{toolName} {params}")
    sp.run(["bash","-c", f"{toolName} {params}"])

"""
Takes a destination as IP or url, spawns a subprocess.
Pings the destingation twice, and then returns a string with exit code, output, and any error messages
"""
def pingTool(destination):
    output = sp.run(["bash","-c", f"ping -c2 {destination}"], stdout=PIPE, stderr=PIPE, universal_newlines=True)
    return f"Return Code:\n{output.returncode}\nStdout:\n{output.stdout}\nSterror:\n{output.stderr}"

"""
The below tool works from the cli
python3 sh_with_py.py mtr -rz -c10 8.8.8.8
"""

def argTool(*args):
    parameters=' '.join(kwargs[1:])
    print(f"{parameters}")
    sp.run(["bash", "-c", f"{parameters}"])   

#params=sys.argv
#Take all arguments except 0 <- which is the python command being run
#print(f"{params}")
#argTool(params)