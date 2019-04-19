from flask import Flask, render_template, flash, request, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, Form, TextField, TextAreaField, validators, SelectField, SelectMultipleField
from wtforms.fields.html5 import EmailField 
from wtforms.validators import DataRequired
from time import strftime
from werkzeug.utils import secure_filename
from flask_wtf.file import FileField, FileRequired
import os


DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = 'hard to guess string ok?!'
bootstrap = Bootstrap(app)

def get_time():
    time = strftime("%Y-%m-%dT%H:%M")
    return time

def write_to_disk(name, surname, email):
    userdata = open('file.log', 'w+')
    timestamp = get_time()
    userdata.write('DateStamp={}, Name={}, Surname={}, Email={} \n'.format(timestamp, name, surname, email))
    userdata.close()
    
    
class Form(FlaskForm):
    name = TextField('First Name', validators=[DataRequired()])
    surname = TextField('Last Name', validators=[DataRequired()])
    email = EmailField('Email Address', [validators.DataRequired(), validators.Email()])
    sequence = TextAreaField('Paste 16sRNA query sequence')
    database = SelectField('Microbial DataBase to Query', choices = [('N','NCBI'), ('G','GreenGenes'), ('S','Silva')])
    file = FileField()
    submit = SubmitField('Submit')

   
@app.route('/', methods=['GET', 'POST'])
def index():
    cwd1 = os.getcwd()
    cwd2 = cwd1[0:-9]
    name = None
    email = None
    sequence = None
    form = Form()
    if form.validate_on_submit():
        name = form.name.data
        surname = form.surname.data
        email = form.email.data
        sequence = form.sequence.data
        database = form.database.data
        #write_to_disk(name,surname, email)
        filename = secure_filename(form.file.data.filename)
        form.file.data.save(cwd2 + "mainLoop/" + filename)
        open(cwd2 + "mainLoop/seqfile.fasta", "w+").write(sequence + "\n" + database)
        open(cwd2 + "mainLoop/preq.txt", "a").write(name + "\n" + email + "\n" + filename + "\n" + database)
        form.name.data = ''
        form.email.data = ''
        form.sequence.data = ''
        form.surname.data = form.database.data = ''
    return render_template('home.html', form=form)

if __name__ == '__main__':
   app.run(debug=False)
