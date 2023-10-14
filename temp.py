import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import seaborn as sns

from scipy import stats
from scipy.stats import randint

# prep
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.datasets import make_classification
from sklearn.preprocessing import binarize, LabelEncoder, MinMaxScaler

dataset = pd.read_csv("Mental_Health.csv")
dataset.info()
dataset.shape
dataset.describe
dataset.head()
#missing data
total = dataset.isnull().sum().sort_values(ascending=False)
percent = (dataset.isnull().sum()/dataset.isnull().count()).sort_values(ascending=False)
missing_data = pd.concat([total, percent], axis=1, keys=['Total', 'Percent'])
missing_data.head(20)
print(missing_data)

#dealing with missing data
dataset.drop(['Do you want to share any other information? (e.g something that affects your mental health in school)'], axis= 1, inplace=True)


dataset.isnull().sum().max() #just checking that there's no missing data missing...
dataset.head(5)

#Making Target Variable into two groups Good or Poor
dataset['Overall how would you rate your mental health?']= dataset['Overall how would you rate your mental health?'].replace(['Excellent','Very good','Good'], 'Good')
dataset['Overall how would you rate your mental health?']= dataset['Overall how would you rate your mental health?'].replace(['Poor','Fair','Not Sure'], 'Poor')
dataset.head(5)

    
#Encoding data
labelDict = {}
for feature in dataset:
    le = preprocessing.LabelEncoder()
    le.fit(dataset[feature])
    le_name_mapping = dict(zip(le.classes_, le.transform(le.classes_)))
    dataset[feature] = le.transform(dataset[feature])
    # Get labels
    labelKey = 'label_' + feature
    labelValue = [*le_name_mapping]
    labelDict[labelKey] =labelValue

#Testing that there's no missing data
#missing data
total = dataset.isnull().sum().sort_values(ascending=False)
percent = (dataset.isnull().sum()/dataset.isnull().count()).sort_values(ascending=False)
missing_data = pd.concat([total, percent], axis=1, keys=['Total', 'Percent'])
missing_data.head(20)
print(missing_data)
    
#correlation matrix

# Splitting dataset into dependent and independent variables
X = dataset.iloc[:, :-1]
y = dataset.iloc [:, 24]


# split X and y into training and testing sets

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
from sklearn.ensemble import RandomForestClassifier
Classifier = RandomForestClassifier(criterion= 'entropy', n_estimators=60, random_state=0)
Classifier.fit(X_train, y_train)

ypred = Classifier.predict(X_test)
import pickle
pickle.dump(Classifier,open("model.pkl", "wb"))
