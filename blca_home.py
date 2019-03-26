from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
bootstrap = Bootstrap(app)

class NameForm(FlaskForm):
    name = StringField('First Name', validators=[DataRequired()])
    submit = SubmitField('Submit')

class emailForm(FlaskForm):
    email = StringField('Email Address', validators=[DataRequired()])
    submit = SubmitField('Submit')
    
@app.route('/', methods=['GET', 'POST'])
def index():
    name = None
    email = None
    nameform = NameForm()
    emailform = emailForm()
    if nameform.validate_on_submit():
        name = nameform.name.data
        nameform.name.data = ''
    if emailform.validate_on_submit():
        email = emailform.email.data
        emailform.email.data = ''
    return render_template('home.html', form=nameform, name=name, email=email)

if __name__ == '__main__':
    app.run(debug=True)

