import subprocess as SP
import sys

#args=sys.argv
#print(args)

SP.run(["sh","-c", "ls -l && pwd; ping -c2 www.google.com"])
#SP.run(["bash","-c", "ls -l"])

#SP.run(["bash","-c", "whoami"])
#SP.run(["bash","-c", "netstat"])
#for i in sys.argv[1:len(args)]:
#    print(i)
#    SP.run(["bash","-c", i])