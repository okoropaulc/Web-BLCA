from flask import Flask
#import os

#os.chdir(r"c:\Users\okoro\OneDrive\Desktop\Web-BLCA\app")

app = Flask(__name__)

from app import routes
