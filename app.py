from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, EmailField
from wtforms.validators import DataRequired, Length

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretstring'

bootstrap = Bootstrap(app)

class OverrideForm(FlaskForm):
    name = StringField(u'Full Name (Last Name, First Name)', validators=[DataRequired()])
    vid = StringField(u'V Number', validators=[DataRequired(), Length(min=9, max=9)])
    email = EmailField(u'Email Address', validators=[DataRequired()])
    year = SelectField(u'Year', choices=['', '2021', '2022', '2023'], validators=[DataRequired()])
    semester = SelectField(u'Semester', choices=['', 'Fall', 'Spring', 'Summer'], validators=[DataRequired()])
    crn = StringField(u'Course CRN', validators=[DataRequired()])
    reason = SelectField(u'Reason for Override', choices=['', 'Prerequisites not met', 'Class is full', 'Other'])
    submit = SubmitField('Submit')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

# @app.route('/test')  
# def confirm():
#     return render_template('confirm.html')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = OverrideForm()
    if form.validate_on_submit():
        return render_template('confirm.html', form=form)
    return render_template('index.html', form=form)
