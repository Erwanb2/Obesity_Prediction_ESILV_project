import pandas as pd
import pickle
from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler


class preprocess():
    def __init__(self):
        self.df_columns=['Age','Gender', 'family_history_with_overweight',
        'FAVC', 'FCVC', 'NCP', 'CAEC', 'SMOKE', 'CH2O', 'SCC', 'FAF', 'TUE',
        'CALC', 'MTRANS']
        self.ctg_dict={
            'Gender': ['Female', 'Male'],
            'family_history_with_overweight': ['yes', 'no'],
            'FAVC': ['no', 'yes'],
            'FCVC': [2, 3, 1],
            'NCP': [3, 1, 2],
            'CAEC': ['Sometimes', 'Frequently', 'Always', 'no'],
            'SMOKE': ['no', 'yes'],
            'CH2O': [2, 3, 1],
            'SCC': ['no', 'yes'],
            'FAF': [0, 3, 2, 1],
            'TUE': [1, 0, 2],
            'CALC': ['no', 'Sometimes', 'Frequently', 'Always'],
            'MTRANS': ['Public_Transportation',
            'Walking',
            'Automobile',
            'Motorbike',
            'Bike']
        }
    def one_encode_data(self, df,ctg_dict):
        # Work on a copy
        df_ = df.copy()
    
        # Encode categorical variable
        #scroll the ctg dict and get all categorical columns and thier possible values
        for k in ctg_dict:
            
            df_[k] = pd.Categorical(df_[k],
                                # Pandas categorical data type
                                # List possible values
                                categories=list(ctg_dict[k]))
        # Encode categorical variables
        return pd.get_dummies(df_)
    def transform(self, sex, age, family_member, high_caloric_food, vegetables, main_meals_per_day, food_between_meals, smoke, water, monitor, physical_acitivity, videogames, alcohol, transportation):
        #Create a panda DataFrame of 1 lign with data
        age=int(age)

        reponse=[age, sex, family_member, high_caloric_food, vegetables, main_meals_per_day, food_between_meals, smoke, water, monitor, physical_acitivity, videogames, alcohol, transportation]
        print("reponse",reponse)
        reponse_dict=dict(zip(self.df_columns, reponse))
        df_to_predict=pd.DataFrame(reponse_dict,[0])
        #Encode Data
        df_to_predict_encoded=self.one_encode_data(df_to_predict,self.ctg_dict)
        #Open scaler
        scaler = pickle.load(open("scaler.p", "rb"))
        dataset_predict=df_to_predict_encoded.values
        dataset_predict_scaled=scaler.transform(dataset_predict)
        print("dataset_predict_scaled",dataset_predict_scaled)
        return dataset_predict_scaled
        # GB.predict(dataset_predict_scaled)