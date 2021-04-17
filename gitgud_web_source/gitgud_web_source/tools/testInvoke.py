import invokeBashProcess as inv
import sys
command="ping -c4 -q www.google.com"
dst = "www.google.com"
#argTool("ping","-c","4","-q", "www.google.com")
#runTool()
#argTool(command)
#print()
#argTool(sys.argv)
print(inv.runTool("ping","-c4 -q www.google.com"))

print(inv.runTool("dig","www.google.com"))
