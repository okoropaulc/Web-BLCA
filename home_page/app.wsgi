#!/usr/bin/python3.6
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/Web-BLCA/home_page/")

from app import app as application
application.secret_key = 'Add your secret key'
