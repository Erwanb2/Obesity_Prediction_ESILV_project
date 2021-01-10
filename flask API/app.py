import os
from flask import Flask, redirect, url_for, render_template, Response, request, flash
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import io
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from forms import QuizzForm
from preprocessing import preprocess
import pickle
#import pyreadr

app = Flask(__name__)
app.config["SECRET_KEY"]="MettezNous20svp?"

@app.route('/')
def Accueil():          
    return render_template('Accueil.html')

@app.route('/Data_Vizs')
def Dashboard():
    return render_template('index.html')

@app.route('/quizz', methods=['GET','POST'])
def quizz():
	form = QuizzForm()
	preprocesser = preprocess()
	if form.validate_on_submit():
		data_preprocessed= preprocess.transform(preprocesser, sex=form.sex.data, age=form.age.data, family_member=form.family_member.data, high_caloric_food=form.high_caloric_food.data, vegetables=form.vegetables.data, main_meals_per_day=form.main_meals_per_day.data, food_between_meals=form.food_between_meals.data, smoke=form.smoke.data, water=form.water.data, monitor=form.monitor.data, physical_acitivity=form.physical_acitivity.data, videogames=form.videogames.data, alcohol=form.alcohol.data, transportation=form.transportation.data)
		model = pickle.load(open("clf_RF.p", "rb"))
		prediction= model.predict(data_preprocessed)
		height=form.height.data
		weight=form.weight.data
		Mass_body_index = weight/(height*height)
		Mass_body_index=round(Mass_body_index)
		print("Mass_body_index",Mass_body_index)
		if Mass_body_index < 18.5:
			theoric_level="Insufficient_Weight"
		elif Mass_body_index < 24.9:
			theoric_level="Normal_Weight"
		elif Mass_body_index < 27.9:
			theoric_level="Overweigt_Weight I"
		elif Mass_body_index < 29.9:
			theoric_level="Overweight_Weight II"
		elif Mass_body_index < 34.9:
			theoric_level="Obesity_Level_I"
		elif Mass_body_index < 39.9:
			theoric_level="Obesity_Level_II"
		else:
			theoric_level="Obesity_Level_III"

		return render_template("prediction.html", prediction=prediction, theoric_level=theoric_level, Mass_body_index=Mass_body_index)
	return render_template('quizz.html', title='Quizz', form=form)          


	
## Errors

@app.errorhandler(404)
def not_found_error(error):
    return render_template('page-404.html'), 404

if __name__ == "__main__":
	app.run(debug=True)
  