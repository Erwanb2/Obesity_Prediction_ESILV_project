The subject of this study is about predicting obesity based on a dataset called :
	"Dataset for estimation of obesity levels based on eating habits and physical condition ​
	 in individuals from Colombia, Peru and Mexico"

In this Git Repository you will find :

 - Data_visualisations.ipynb  jupyter notebook file containing the exploratory work we did on data
 - Flask API                  directory containing the app 
 - obesity_prediction.pdf     PDF of the PPT explaining our work
 - obesity_notebook.ipynb     jupyter notebook file containing the pre-processing and predictions code

To launch our app you need to : 
-open The Folder with VisualStudioCode
-In the terminal:
$env:FLASK_APP="app"
pip install -r requirements.txt

and LAUNCH THE APP ! (-python app.py)

If you have any problem, switch your Python Interpreter (ctrl+shift+p) to python from conda. (because we use scikitlearn from conda)

In conclusion of this study, we finally manage to get a 79% of accuracry while predicting the target and 93% of accuracy while predicting if a person is obese or not.​
We maybe could even better results if the mistakes/problems in the inital dataset were fixed. ​
We enjoyed working on these data because it's a concrete use case of data science and about a subject on which everyone has knowledge.