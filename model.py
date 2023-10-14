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
corrmat = dataset.corr()
f, ax = plt.subplots(figsize=(12, 9))
sns.heatmap(corrmat, vmax=.8, square=True);
plt.show()
# Distribution and density by Age
plt.figure(figsize=(12,8))
sns.distplot(dataset["Age"], bins=24)
plt.title("Distribution and density by Age")
plt.xlabel("Age")
plt.figure(figsize=(12,8))
labels = labelDict['label_Faculty']
g = sns.countplot(x="Faculty", data=dataset)
g.set_xticklabels(labels)

plt.title('Total Distribution by Faculty')
plt.figure(figsize=(12,8))
labels = labelDict['label_Year of Study']
g = sns.countplot(x="Year of Study", data=dataset)
g.set_xticklabels(labels)

plt.title('Level')
#Nested bar plot to show the correlation between CGPA and YEAR OF STUDY
o = labelDict['label_CGPA']

g = sns.factorplot(x="CGPA", y="Overall how would you rate your mental health?", hue="Year of Study", data=dataset, kind="bar",  ci=None, size=5, aspect=2, legend_out = True)
g.set_xticklabels(o)

plt.title('Probability of mental health condition')
plt.ylabel('Probability x 100')
plt.xlabel('CGPA')
# replace legend labels

new_labels = labelDict['label_Year of Study']
for t, l in zip(g._legend.texts, new_labels): t.set_text(l)

# Positioning the legend
g.fig.subplots_adjust(top=0.9,right=0.8)

plt.show()
# Splitting dataset into dependent and independent variables
X = dataset.iloc[:, :-1]
y = dataset.iloc [:, 24]


# split X and y into training and testing sets

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, recall_score, plot_roc_curve, confusion_matrix, classification_report, precision_recall_curve, auc
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier, GradientBoostingClassifier
from xgboost.sklearn import XGBClassifier
import xgboost as xgb
from sklearn import metrics
key = ['LogisticRegression','KNeighborsClassifier','DecisionTreeClassifier','RandomForestClassifier','GradientBoostingClassifier','AdaBoostClassifier','XGBClassifier']
value = [LogisticRegression(), KNeighborsClassifier(n_neighbors = 2, weights ='uniform'), DecisionTreeClassifier(random_state=10), RandomForestClassifier(n_estimators=60, random_state=0), GradientBoostingClassifier(random_state=0), AdaBoostClassifier(), xgb.XGBClassifier(random_state=10,booster="gbtree")]
models = dict(zip(key,value))
models
predicted =[]
for name,algo in models.items():
    model=algo
    model.fit(X_train,y_train)
    predict = model.predict(X_test)
    acc = accuracy_score(y_test, predict)
    predicted.append(acc)
    print(name,acc)
    plt.figure(figsize = (10,5))
ax = sns.barplot(x = predicted, y = key, palette='Purples', order=predicted.sort())
plt.title("Plotting the Model Accuracies", fontsize=16, fontweight="bold")
xgb = XGBClassifier()
xgb.fit(X_train,y_train)
pred = xgb.predict(X_test)
cf_matrix = confusion_matrix(y_test, pred)
sns.heatmap(cf_matrix/np.sum(cf_matrix), annot=True, 
            fmt='.2%', cmap='Purples')
plt.title('Confusion Matrix of XGBoost', fontweight='bold', fontsize=16)
plt.xlabel('Predicted', fontweight='bold', fontsize=12)
plt.ylabel('Actual', fontweight='bold', fontsize=12)
fpr, tpr, thresholds = metrics.roc_curve(y_test, pred)
plt.figure(figsize=(8,8))
roc_auc = metrics.auc(fpr, tpr)
plt.plot(fpr, tpr, color='darkorange', label='ROC curve (area = %0.2f)' % roc_auc)
plt.plot([0, 1], [0, 1], color='navy', linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.0])
plt.rcParams['font.size'] = 12
plt.title('ROC Curve', fontweight = 'bold', fontsize=16)
plt.xlabel('False Positive Rate (1 - Specificity)', fontweight = 'bold', fontsize=14)
plt.ylabel('True Positive Rate (Sensitivity)', fontweight = 'bold', fontsize=14)
plt.legend(loc="lower right")
plt.show()
metrics.roc_curve(y_test, pred)
ypred = xgb.predict(X_test)
ypred
df = pd.DataFrame({'Actual':y_test,  'Predicted': ypred})
df

import pickle
pickle.dump(xgb,open("model.pkl", "wb"))