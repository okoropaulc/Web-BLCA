import subprocess

def bash_command(cmd):
    subprocess.Popen(['/bin/bash', '-c', cmd])

bash_commmand('ls')