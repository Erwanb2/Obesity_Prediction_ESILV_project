from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DecimalField, BooleanField, RadioField
from wtforms.validators import DataRequired,Length,NumberRange

class QuizzForm(FlaskForm):
    sex = RadioField('What is your gender ?', choices=[('Male','Male'),('Female','Female')], validators=[DataRequired()])
    age=DecimalField("What is your age ? ", validators=[DataRequired(), NumberRange(min=0, max=120)])
    height=DecimalField("What is your height (meters, example : 1.80) ?", validators=[DataRequired(), NumberRange(min=0, max=2.5)])
    weight=DecimalField("What is your weight (kg) ?", validators=[DataRequired(), NumberRange(min=0, max=250)])
    family_member = RadioField('Has a family member suffered or suffers from overweight ?', choices=[('no','No'),('yes','Yes')], validators=[DataRequired()]) 
    high_caloric_food = RadioField(' Do you eat high caloric food frequently ?', choices=[('no','no'),('yes','yes')], validators=[DataRequired()]) 
    vegetables = RadioField('Do you usually eat vegetables in your meals ?', choices=[('1','Never'),('2','Sometimes'),('3', 'Always')], validators=[DataRequired()]) 
    main_meals_per_day = RadioField('How many main meals do you have daily ?', choices=[('1','Between 1 y 2'),('2','Three'),('3', 'More than three')], validators=[DataRequired()]) 
    food_between_meals = RadioField('Do you eat any food between meals ?', choices=[('no','No'),('Sometimes','Sometimes'),('Frequently', 'Frequently'),('Always', 'Always')], validators=[DataRequired()]) 
    smoke = RadioField('Do you smoke ?', choices=[('no','No'),('yes','Yes')], validators=[DataRequired()]) 
    water = RadioField('How much water do you drink daily ?', choices=[('1','Less than a liter'),('2','Between 1 and 2 L'),('3', 'More than 2 L')], validators=[DataRequired()])
    monitor  = RadioField('Do you monitor the calories you eat daily ?', choices=[('no','No'),('yes','Yes')], validators=[DataRequired()])
    physical_acitivity  = RadioField('How often do you have physical activity?', choices=[('0','I do not have'),('1','1 or 2 days'),('2', '2 or 4 days'),('3', '4 or 5 days')], validators=[DataRequired()])
    videogames = RadioField('How much time do you use technological devices such as cell phone, videogames, television, computer and others ? ', choices=[('0','0–2 hours'),('1','3–5 hours'),('2', 'More than 5 hours')], validators=[DataRequired()])  
    alcohol = RadioField('How often do you drink alcohol ?', choices=[('no','I do not drink'),('Sometimes','Sometimes'),('Frequently', 'Frequently'), ('Always', 'Always')], validators=[DataRequired()]) 
    transportation = RadioField('Which transportation do you usually use ?', choices=[('Automobile','Automobile'),('Motorbike','Motorbike'),('Bike', 'Bike'), ('Public_Transportation', 'Public Transportation'), ('Walking', 'Walking')], validators=[DataRequired()]) 
    submit = SubmitField("Submit")