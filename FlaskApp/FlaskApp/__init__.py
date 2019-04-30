from flask import Flask, render_template, flash, request, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, Form, TextField, TextAreaField, validators, SelectField, SelectMultipleField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired
from time import strftime
from werkzeug.utils import secure_filename
from flask_wtf.file import FileField, FileRequired, FileAllowed
import os
#from ../Web-BLCA/mainLoop/main import start_blca_backend
#from app import app


DEBUG = True
app = Flask(__name__, static_url_path='', static_folder="/var/www/Web-BLCA/mainLoop")
app.config.from_object(__name__)
app.config['SECRET_KEY'] = 'hard to guess string ok?!'
#app.config['MAX_CONTENT_LENGTH'] = 20 * 1024 * 1024 #Set maximum file upload size to 20mb
bootstrap = Bootstrap(app)
cwd = os.getcwd()
os.chdir("/var/www/html/Web-BLCA/mainLoop/")
os.system("sudo python3 main.py")
os.chdir(cwd)

def get_time():
    time = strftime("%Y-%m-%dT%H:%M")
    return time

def write_to_disk(name, surname, email):
    userdata = open('file.log', 'w+')
    timestamp = get_time()
    userdata.write('DateStamp={}, Name={}, Surname={}, Email={} \n'.format(timestamp, name, surname, email))
    userdata.close()

#create forms
class Form(FlaskForm):
    name = TextField('First Name', validators=[DataRequired()])
    surname = TextField('Last Name', validators=[DataRequired()])
    email = EmailField('Email Address', [validators.DataRequired(), validators.Email()])
    #sequence = TextAreaField('Paste 16sRNA query sequence')
    database = SelectField('Microbial DataBase to Query', choices = [('N','NCBI'), ('G','GreenGenes'), ('S','Silva')])
    file = FileField('Upload 16s rRNA Sequence File', validators=[FileRequired(), FileAllowed(['txt', 'fasta', 'FASTA'], 'upload FASTA files only!')])
    submit = SubmitField('Submit')

#homepage
@app.route('/', methods=['GET', 'POST'])
def index():
    cwd1 = os.getcwd()
    cwd2 = cwd1[0:-9]
    name = None
    email = None
    #sequence = None
    form = Form()
    if form.validate_on_submit():
        name = form.name.data
        surname = form.surname.data
        email = form.email.data
        #sequence = form.sequence.data
        database = form.database.data
        #write_to_disk(name,surname, email)
        filename = secure_filename(form.file.data.filename)
        form.file.data.save("/var/www/html/Web-BLCA/mainLoop/" + filename)


        open("/var/www/html/Web-BLCA/mainLoop/seqfile.fasta", "w+").write(database+"\n")
        open("/var/www/html/Web-BLCA/mainLoop/preq.txt", "a").write(name + "\n" + email + "\n" + filename + "\n" + database+"\n")
        form.name.data = ''
        form.email.data = ''
        #form.sequence.data = ''
        form.surname.data = form.database.data = ''
        flash("Thank you! Your Job has been submitted!", "success")
    return render_template('home.html', form=form)

#Tutorial Page
@app.route('/tutorial')

def tutorial():
    return render_template('tutorial.html')

#About Page
@app.route('/about')

def about():
    return render_template('about.html')

#Contact Page
@app.route('/contact')

def contact():
    return render_template('contact.html')

if __name__ == '__main__':
   app.run(debug=False)
