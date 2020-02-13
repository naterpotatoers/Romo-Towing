from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, IntegerField, DateField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Length, Optional
from app.models import Vehicle

class VehicleForm(FlaskForm):
    year = StringField('Year', validators=[DataRequired()])
    make = StringField('Make', validators=[DataRequired()])
    model = StringField('Model', validators=[DataRequired()])
    milage = StringField('Milage', validators=[DataRequired()])
    info = TextAreaField('Info', validators=[DataRequired()])
    submit = SubmitField('Submit')

class PriceEstimatorForm(FlaskForm):
    chpTow = BooleanField('Is this a CHP Tow?', validators=[Optional()])
    fpdTow = BooleanField('Is this a FPD Tow?', validators=[Optional()])
    onLot = BooleanField("Towed to our Tow Yard?(Ignore if CHP or FPD tow)", validators=[Optional()])
    towHours = IntegerField('Number of Hours Towed', validators=[DataRequired()]) #ASK RAUL IF THIS IS APPLICABLE FOR CHP & FPD TOWS
    submit = SubmitField('Submit')
