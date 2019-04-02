from flask import Flask, render_template, flash, request, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, Form, TextField, TextAreaField, validators, SelectField, SelectMultipleField
from wtforms.fields.html5 import EmailField 
from wtforms.validators import DataRequired
from time import strftime
from werkzeug.utils import secure_filename
import os

path = 'C:/Users/okoro/OneDrive/Desktop/Web-BLCA/home_page'

DEBUG = True
app = Flask(__name__)
UPLOAD_FOLDER = path
ALLOWED_EXTENSIONS = set(['txt', 'fasta', 'FASTA'])
app.config.from_object(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
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
    submit = SubmitField('Submit')

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
   
@app.route('/', methods=['GET', 'POST'])
def index():
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
        write_to_disk(name,surname, email)
        open("seqfile.fasta", "w+").write(sequence + "\n" + database)
        form.name.data = ''
        form.email.data = ''
        form.sequence.data = ''
        form.surname.data = form.database.data = ''
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file',
                                    filename=filename))
    return render_template('home.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
