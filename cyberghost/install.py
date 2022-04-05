import subprocess

print("cmd exec.")

cmd = "./cmd/cyberghost.cmd"
subprocess.Popen(cmd.split())


print("pip exec.")

cmd = "pip install -r ./requirements.txt"
subprocess.Popen(cmd.split())