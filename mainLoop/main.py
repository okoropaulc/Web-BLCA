#!/usr/bin/python3import subprocessimport osdef bash_command(cmd):    subprocess.run([cmd],check=True,shell=True)def normal(cmd):    subprocess.run([cmd], stdout=subprocess.PIPE, sterr=subprocess.PIPE, check=True)def check_program(tool):    try:        out =        subprocess.call([tool, "--help"],stdout=subprocess.PIPE)    except OSError as e:        if e.errno == os.errno.ENOENT:            print(tool + " not found, installing")        else:            print("other error finding " + tool)            raisebash_command('ls')cwd = bash_command("pwd")check_program("clustalo")check_program("git")print(cwd)