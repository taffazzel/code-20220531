__author__ = 'tafaz'
import unittest
from bmi_cal import Calculation
import boto3
import json
import pandas as pd

class CalculationTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        user = 'taffazzel'
        cls.lib = Calculation()
        cls.lib.connect(user)

    '''def test_calbmi(self):
        print("I am in test_plus")
        with open("XXX/input/input.json") as f:
            json_data = json.load(f)
        self.number_of_BMI_Category_overweight = self.lib.calbmi(json_data)
        self.assertEqual(self.number_of_BMI_Category_overweight,1)'''

    def test_calbmi(self):
        s3 = boto3.client('s3')
        bucket = 'XXX'
        key = 'test-pipeline/input.json'
        response = s3.get_object(Bucket=bucket, Key=key)
        content = response['Body']
        json_data = json.loads(content.read())
        self.number_of_BMI_Category_overweight = self.lib.calbmi(json_data)
        self.assertEqual(self.number_of_BMI_Category_overweight, 1)


if __name__ == '__main__':
    print("I am in main")
    unittest.main()
