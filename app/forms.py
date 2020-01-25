from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, DateTimeField, IntegerField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Length, Optional
from app.models import Vehicle

class VehicleForm(FlaskForm):
    year = StringField('Year', validators=[DataRequired()])
    make = StringField('Make', validators=[DataRequired()])
    model = StringField('Model', validators=[DataRequired()])
    vin = StringField('VIN', validators=[DataRequired()])
    arrivalTime = DateTimeField('Arrival Date', validators=[DataRequired()])
    submit = SubmitField('Submit')

class PriceEstimatorForm(FlaskForm):
    # print('Please Select Only One Box.')
    chpTow = BooleanField('Is this a CHP Tow?', validators=[Optional()])
    fpdTow = BooleanField('Is this a FPD Tow?', validators=[Optional()])
    onLot = BooleanField("Towed to our Tow Yard?(Ignore if CHP or FPD tow)", validators=[Optional()])
    towHours = IntegerField('Number of Hours Towed(ASK RAUL IF THIS IS APPLICABLE FOR CHP & FPD TOWS)', validators=[DataRequired()])
    submit = SubmitField('Submit')
