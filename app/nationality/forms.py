from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class NameForm(FlaskForm):
    name = StringField('民族名称', validators=[DataRequired()])
    submit = SubmitField('确定')