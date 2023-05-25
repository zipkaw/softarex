from typing import Any, Optional
from django.apps import AppConfig
import pathlib
from model.revenue_predictor import *
import pandas as pd
import joblib
import os

class WebRevenueConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'web_revenue'
    
    ml_models = {
    'KNeighbors':Model1KNN(),
    'RandomForest':Model1RF(), 
    'LightGBM': Model1lgb(),
    'Linear':Model2Linear(),
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.trainval_filename = '/home/plantator/revenue_predict/data/train.csv.zip'
        df_trainval, y_trainval = prepare_train_data(self.trainval_filename)
        lin_reg_predictor = fitting_models(self.ml_models, df_trainval, y_trainval)
        joblib.dump(lin_reg_predictor, 'model2.pkl')
        joblib.dump(self.ml_models['KNeighbors'], 'model1knn.pkl')
        joblib.dump(self.ml_models['RandomForest'], 'model1rf.pkl')
        joblib.dump(self.ml_models['LightGBM'], 'model1lgb.pkl')

    def prediction(self, data_to_predict):
        data = prepare_test_data(data_to_predict)
        return predict_revenue(self.lin_reg_predictor, self.models, data)
    
    def to_csv(self, filepath, data):
        save_to_csv(data, filename=filepath)

