#!/usr/bin/python3import subprocessimport osdef bash_command(cmd):    subprocess.run([cmd],check=True,shell=True)def normal(cmd):    subprocess.run([cmd], stdout=subprocess.PIPE, sterr=subprocess.PIPE, check=True)def check_dependencies():    if not (bash_command("command -v git")):        print("git is not installed")    else:        print("git is installed")    if not(bash_command("command -v clustalo")):        print("clustalo is not installed")    else:        print("clustalo is installed")bash_command('ls')cwd = bash_command("pwd")check_dependencies()print(normal(stout))print(cwd)