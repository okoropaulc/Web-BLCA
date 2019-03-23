#!/usr/bin/python3import subprocessimport osimport logginglogging.basicConfig(level=logging.DEBUG, filename="web-blca.log")#runs bash command but does not print outdef normal(cmd):    subprocess.run([cmd], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True, shell=True)    logging.info(cmd)#runs call and prints out to shell sessiondef normal_verbose(cmd):    call = subprocess.run([cmd], check=True, shell=True)    logging.info(cmd)#function checks to see if program is installed and in path somewhat of a formalitydef check_program(tool):    try:        subprocess.call([tool, "--help"],stdout=subprocess.PIPE)        logging.info(tool)    except OSError as e:        if e.errno == os.errno.ENOENT:            print(tool + " not found, installing")            if tool == "pip":                normal("sudo apt install -y python-pip")                logging.info("pip not found")                logging.info("sudo apt install -y python-pip")            elif tool == "blastn":                logging.info("blast not found")                normal("sudo apt install -y ncbi-blast+")                logging.info("sudo apt install -y ncbi-blast+")            else:                logging.info(tool + " not found")                normal("sudo apt install -y " + tool)                logging.info("sudo apt install -y " + tool)    logging.info(tool +" installed and working fine")#function to make sure all dependencies are installed and in path TODO setup BLCA universlly ie. first scriptdef setup():    cwd = os.getcwd()    list = []    with open("depend.txt", 'r') as dependencies:        list.append(dependencies.readline().strip())    for program in list:        check_program(program)    logging.info("pip install biopython")    normal("pip install biopython")    logging.info("All dependencies installed")setup()print("all good boss")