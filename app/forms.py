from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from flask_wtf.validators import DataRequired

class RegionForm(FlaskForm):
    region = StringField('Region or Country', validators=[DataRequired()])
    submit = SubmitField('Get Weather')