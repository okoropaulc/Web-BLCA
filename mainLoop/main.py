#!/usr/bin/python3import subprocessimport osimport loggingimport datetimeimport uuidimport smtpliblogging.basicConfig(level=logging.DEBUG, filename="web-blca.log")#object to make keeping track of users easier class User:    def __init__(self, name, email, data):        self.name = name        self.email = email        self.data = data #runs bash command but does not print outdef normal(cmd):    subprocess.run([cmd], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True, shell=True)    logging.info(cmd)#runs call and prints out to shell sessiondef normal_verbose(cmd):    call = subprocess.run([cmd], check=True, shell=True)    logging.info(cmd)#function checks to see if program is installed and in path somewhat of a formalitydef check_program(tool):    try:        if tool == "muscle":            subprocess.call([tool, '-version'],stdout=subprocess.PIPE)        else:            subprocess.call([tool, "--help"],stdout=subprocess.PIPE)    except OSError as e:        if e.errno == os.errno.ENOENT:            print(tool + " not found, installing")            if tool == "pip":                normal("sudo apt install -y python3-pip")                logging.info("pip not found")                logging.info("sudo apt install -y python3-pip")            elif tool == "blastn":                logging.info("blast not found")                normal("sudo apt install -y ncbi-blast+")                logging.info("sudo apt install -y ncbi-blast+")            else:                logging.info(tool + " not found")                normal("sudo apt install -y " + tool)                logging.info("sudo apt install -y " + tool)    logging.info(tool +" installed and working fine")#function to make sure all dependencies are installed and in path TODO setup BLCA universlly ie. first scriptdef setup():    cwd = os.getcwd()    list = []    with open("depend.txt", 'r') as dependencies:        all_line = dependencies.read()    for line in all_line.split():        list.append(line.strip())    print(list)    for program in list:        check_program(program)    #biopython needs to be installed through pip so this just checks it    logging.info("pip3 install biopython")    normal("pip3 install biopython")    logging.info("All dependencies installed")#method used to hold fasta file in memory in order to avoid directory helldef read_in_fasta(filename):    fasta_stuff = ""    with open(filename, "r") as myfile:        fasta_stuff = myfile.read()    return fasta_stuff#Handles creating the user directory and writing the user data to file and running BLCAdef blca(user):    cwd = os.getcwd()    fasta_seq = read_in_fasta(user.data)    if not (os.path.exists(user.email)):        logging.info("mkdir "+user.email)        normal("mkdir "+user.email)        os.chdir("..")        logging.info("cp -rf BLCA "+cwd+"/"+user.email)        normal("cp -rf BLCA "+cwd+"/"+user.email)        os.chdir(cwd +"/"+user.email+"/BLCA")    #checks if directory exists and makes a subdir if need be     else:        os.chdir(user.email)        id = str(uuid.uuid1())        normal("mkdir " +id)        logging.info(user.email + "exists, making subdirectory")        cwd2 = os.getcwd()        os.chdir("..")        os.chdir("..")        normal("cp -rf BLCA "+cwd2+"/"+id)        logging.info("Copying BLCA into new user directory")        os.chdir(cwd2+"/"+id+ "/" + "BLCA")    file = open("data.fasta", "w")    file.write(fasta_seq)    file.close()    #runs the blca commands    logging.info("python3 2.blca_main.py -i data.fasta")    normal("python3 2.blca_main.py -i data.fasta")    #sends email to user when finished TODO fix the link    sendemail(my_email, user_email=[user.email],subject="Your Job is finished", message=str("Your data can be found here: https://blca.cs.luc.edu"+cwd), login="webblcaluc@gmail.com",password="web@bio1_4fun")    logging.info("Sending email to " +user.email)    print("ok")#can change but will need to fix a bit of stuffmy_email = "webblcaluc@gmail.com"#sends email from gmaildef sendemail(my_email, user_email, subject, message, login, password, smtpserver='smtp.gmail.com:587'):    header ='From: %s \n' % my_email    header += 'To: %s \n' % ','.join(user_email)    header+='Subject: %s \n \n' % subject     message = header + message        server = smtplib.SMTP(smtpserver)    server.starttls()    server.login(login,password)    problems = server.sendmail(my_email, user_email, message)    server.quit()    return problems#Runs setup methodsetup()#Creates a queue and accepts input queue = []while 1 == 1:    cwd = os.getcwd()        name = input("Please enter a name> ")    email = input("Please enter an email> ")    data = input("Please enter the filename for your fasta data> ")    count = str(uuid.uuid1())    fasta_seq = read_in_fasta(data)    count = User(name, email, data)    queue.append(count)    while queue != []:        for item in queue:            print(item.name)        blca(queue[0])        del(queue[0])    os.chdir(cwd)print("all good boss")