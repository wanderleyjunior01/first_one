from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, FloatField, SubmitField
from wtforms.validators import DataRequired


class StudentForm(FlaskForm):
    name = StringField("Student Name", validators=[DataRequired()])
    subject = SelectField("Student Subject", choices=[(" "), ("Psycology"), ("Mechanical"), ("Arts"), ("Physics")], validators=[DataRequired()])
    student_fee = FloatField("Student Fee", validators=[DataRequired()])
    submit = SubmitField("Add New Record")