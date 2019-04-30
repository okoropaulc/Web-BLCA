# Web-BLCA
This project is the web implementation of the Bayesian Lowest Common Ancestor algorithm built by Gao et al., (2017). BMC Bioinformatics, 18(1):247. The actual BLCA algorithm, software, and paper are found at https://github.com/qunfengdong/BLCA 
The Team members of this project are: Paul Okoro, Benjamin Lorentz, and John Morris. 

# Aim
The aim for the web version of the BLCA is to enable non technical savvy users to have access to this wonderful algorithm by just following a simple web user interface.
#Prerequisities

    *Python 3
    *Linux
    *Biopython

#The following programs should be in your PATH:

    *BLAST binary (ftp://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/2.5.0/)
    *clustalo (http://www.clustal.org/omega/)
    *MUSCLE (http://www.drive5.com/muscle/downloads.htm)

# Manual
The web blca is completed and hosted at http://147.126.2.110/
To get a feel of how easy and fast the web app is, user can download the test_fasta.txt file in this repo, and upload it to the web blca website as well as fill in their email through which they will receive link to access the results.

# Note
The web blca has two major components (backend and front end) in this repo. The backend code is in the mainLoop folder, while the front code is in the FlaskApp folder. These two components were coded to align specifically with the LUC server. More precisely, all dependencies for BLCA software and apache2 were preinstalled in the server, and paths in the code were hardcoded with respect to the luc server.
The way the repo components is distributed in the server machine is; when this repo is cloned, the FlaskApp folder is moved/copied to /var/www/ and the FlaskApp.conf file is moved/copied to /etc/apache2/sites-available/ and then the conf file is enabled while the apache2 server is restarted.
The user which the program is installed and run under must be in the www-data group. To start the blca backend suggested use is to start a tmux session and invoke main.py with the command python3 main.py. BLCA may need to be cloned seperatly from github and placed inside of the Web-BLCA folder. 

#Future Development

* Validate Fasta
* Balance Server Resources
* More databases
* User generated databases
* Higher security 


