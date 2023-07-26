import pandas as pd
import numpy as np
from sklearn import linear_model

# file_path="C:\Users\shubh\OneDrive\Desktop\webapp\venv\depressiondetector\mldataset.csv"
file_path='C:/Users/shubh/OneDrive/Desktop/webapp/venv/depressiondetector/mldataset.csv'
df = pd.read_csv(file_path)
def grading(prediction_data):
    
    reg = linear_model.LinearRegression()
    reg.fit(df[['Seasonal changes','Harmonal changes', 'Score', 'Score2']], df.Grade)
    
    prediction = reg.predict(prediction_data)
    return prediction


