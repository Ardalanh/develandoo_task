import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
#from sklearn.neighbors import KNeighborsClassifier
#from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis, LinearDiscriminantAnalysis
#from sklearn.metrics import classification_report, confusion_matrix
from scikitplot.metrics import plot_roc_curve

from ..models import Document
from django.core.files import File

import os

class DataAnalayzer:
    def __init__(self):
        self.file_path = ''
        self.train_data_path = 'training.csv'
        self.logmodel = LogisticRegression()
        #self.lda = LinearDiscriminantAnalysis()
        #self.qda = QuadraticDiscriminantAnalysis()
        #self.knn = KNeighborsClassifier()

        #self.models = [self.logmodel, self.lda, self.qda, self.knn]
        self.models = [self.logmodel]
        self.predictions = []

    def set_file_path(self, pk=1):
        try:
            self.file_path = Document.objects.get(pk=pk).user_file.path
        except:
            print('No file found')

    def train(self):
        data = pd.read_csv('myai/machine_learning/training.csv', index_col=0)
        X = pd.get_dummies(data.drop('scoring', axis=1), drop_first=True)
        y = pd.get_dummies(data['scoring'], drop_first=True)['Win']
        for model in self.models:
            model.fit(X, y)

    def make_predictions(self, pk):
        if not self.file_path:
            self.set_file_path(pk)
        self.train()
        self.predictions = []

        excel_files = pd.read_excel(self.file_path, sheet_name=None)
        for v,k in excel_files.items():
            if {'id','industry','countryCode','organizationTypeCode','organizationSizeCode','ageRange','gender'}.issubset(k.columns):
                dataset = k
                break
        dataset.set_index('id', inplace=True)
        dummy = dataset[['industry','countryCode','organizationTypeCode','organizationSizeCode','ageRange','gender']].copy()
        #dummy.set_index('id', inplace=True)
        dummy.dropna(inplace=True)
        dummy = pd.get_dummies(dummy, drop_first=True)
        for model in self.models:
            result = pd.DataFrame(model.predict(dummy), index=dummy.index,columns=['prediction'])
            result = result['prediction'].map({0:'Loss',1:'Win'})
            result.to_csv("myai/machine_learning/x.csv")
            reopen = open("myai/machine_learning/x.csv", "rb")
            django_file = File(reopen)
            doc = Document.objects.get(pk=pk)
            doc.logreg_result.save(f'{pk}.csv',django_file,save=True)
            doc.save()
            reopen.close()
            os.remove("myai/machine_learning/x.csv")
            self.predictions.append(result)
