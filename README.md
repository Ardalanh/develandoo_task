Develandoo Task
===============

Data Analysis
-------------
Analysis of the provided dataset is in Jupyter Notebook.

After droping rows where the 'scoring' column is null, no column had null values except 'ageRange' and 'gender' which they had perfect correllation on null values. 
I attempted to find a good ampute rule for this two columns, but despite finding some relations, it was not obviuous what the missing values were. I believe we can fill these null values by using training with the rest of the data and predicting these values.
But the accuracy of the models were satisfying when I droped all the null rows.

Because the data set is entirely categorical(I could make ageRange and OrganizationSize as a numeric value but I don't think it matters in this case), the dimension(parameters) are very high therefore I believe Linear models perform better on average.

Here is the comparision of ROC curves.

<img src="https://github.com/Ardalanh/develandoo_task/blob/master/LogReg_ROC.png" height=290><img src="https://github.com/Ardalanh/develandoo_task/blob/master/LDA_ROC.png" height=290>
<img src="https://github.com/Ardalanh/develandoo_task/blob/master/linSVM_ROC.png" height=290><img src="https://github.com/Ardalanh/develandoo_task/blob/master/SVM_ROC.png" height=290>
<img src="https://github.com/Ardalanh/develandoo_task/blob/master/KNN_ROC.png" height=290><img src="https://github.com/Ardalanh/develandoo_task/blob/master/TREE_ROC.png" height=290>

Django
----------

Very simplistic web site with two views, one is home view where you can upload '.csv' files and get prediction.

Home-page has two required field, name and file.
info page has the previous files and their results(if results where calculated).

<img src="https://github.com/Ardalanh/develandoo_task/blob/master/Django/Home.PNG" height=290><img src="https://github.com/Ardalanh/develandoo_task/blob/master/Django/Info.PNG" height=290>
