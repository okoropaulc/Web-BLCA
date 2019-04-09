from flask import Flask
#import os

#os.chdir(r"c:\Users\okoro\OneDrive\Desktop\Web-BLCA\app")

app = Flask(__name__)
app.config.from_object('config')

from app import views
from app import routes
