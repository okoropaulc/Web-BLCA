#!/usr/bin/python3.6
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/Web-BLCA/")

from Web-BLCA import app as application
application.secret_key = 'Add your secret key'
