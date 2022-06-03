__author__ = 'tafaz'
import pandas as pd
import json



class Calculation:
    def __init__(self):
        self.base = ''
        self.calc_list = []

    def connect(self,user):
        self.user = user
        print(self.user)

    def calbmi(self,json_data):
        new_json = []
        for data in json_data:
            data['BMI'] = data['WeightKg'] / ((data['HeightCm'] / 100) ** 2)
            if data['BMI'] <= 18.4:
                data['BMI Category'] = 'Underweight'
                data['Health risk'] = 'Malnutrition risk'
            elif data['BMI'] <= 24.5 and data['BMI'] >= 18.5:
                data['BMI Category'] = 'Normal weight'
                data['Health risk'] = 'Low risk'
            elif data['BMI'] <= 29.9 and data['BMI'] >= 25:
                data['BMI Category'] = 'Overweight'
                data['Health risk'] = 'Enhanced risk'
            elif data['BMI'] <= 34.9 and data['BMI'] >= 30:
                data['BMI Category'] = 'Moderately obese'
                data['Health risk'] = 'Medium risk'
            elif data['BMI'] <= 39.9 and data['BMI'] >= 35:
                data['BMI Category'] = 'Severely obese'
                data['Health risk'] = 'High risk'
            elif data['BMI'] >= 40:
                data['BMI Category'] = 'Very severely obese'
                data['Health risk'] = 'Very high risk'
            new_json.append(data)
            df = pd.json_normalize(new_json)
            number_of_BMI_Category_overweight = sum(df['BMI Category'] == 'Overweight')

        return number_of_BMI_Category_overweight
