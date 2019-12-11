import os
import subprocess
while True:
    
    cmd = input(os.getcwd() + "--> ")
    if cmd.startswith("cd"):
        cmd = cmd.replace("cd ","")
        cmd = cmd.replace("'","")
        cmd = cmd.replace("\"","")
        print(cmd)
        os.chdir(cmd)
    elif cmd == "exit":
        break
    elif cmd == "clear":
        os.system("clear")
    else:
        output = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE,encoding='utf-8')
        hi = output.stdout.read()
        print(hi)