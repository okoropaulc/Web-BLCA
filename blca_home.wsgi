#!/usr/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/blca.cs.luc.edu/public_html/Web-BLCA/home_page")
from blca_home import app as application
application.secret_key = 'helloworld'
