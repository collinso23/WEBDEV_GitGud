import subprocess as sp
import sys

import subprocess as sp
import sys
"""
This is a very generic function. It will work with any of the bash tools not just the network tools for this project 
currently has complex usage. It allows for full bash like functions with the param arg
as the arguments are not properly caputre you can use stdin, pipe, newline, ect to escape the program.
example usage: python3 sh_with_py.sh
enter a tool to test: whois
enter a destination: AS6079

"""
def runTool(toolName, parameters):
    print(f"{toolName} {parameters}")
    sp.run(["bash","-c", f"{toolName} {parameters}"])

#tool = input ("enter a tool to test: ")
#params = input ("enter parameters: ")
#runTool(tool,params)

"""
The below tool works from the cli
python3 sh_with_py.py mtr -rz -c10 8.8.8.8
"""
def argTool(parameters):
    print(f"{' '.join(parameters)}")
    sp.run(["bash", "-c", f"{' '.join(parameters)}"])   

params=sys.argv[1:] #Take all arguments except 0 <- which is the python command being run
print(f"{params}")
argTool(params)