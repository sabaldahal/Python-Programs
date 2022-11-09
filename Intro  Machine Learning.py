
"""
Using 10 estimators: Accuracy is: 86.89%

Using 12 estimators: Accuracy is: 73.77%

Using 14 estimators: Accuracy is: 83.61%

Using 16 estimators: Accuracy is: 86.89%

Using 18 estimators: Accuracy is: 85.25%

Using 20 estimators: Accuracy is: 81.97%

Using 22 estimators: Accuracy is: 85.25%

Using 24 estimators: Accuracy is: 80.33%

Using 26 estimators: Accuracy is: 81.97%

Using 28 estimators: Accuracy is: 81.97%

Using 30 estimators: Accuracy is: 86.89%

Using 32 estimators: Accuracy is: 83.61%

Using 34 estimators: Accuracy is: 83.61%

Using 36 estimators: Accuracy is: 85.25%

Using 38 estimators: Accuracy is: 86.89%

Using 40 estimators: Accuracy is: 83.61%

Using 42 estimators: Accuracy is: 85.25%

Using 44 estimators: Accuracy is: 81.97%

Using 46 estimators: Accuracy is: 85.25%

Using 48 estimators: Accuracy is: 85.25%

Using 50 estimators: Accuracy is: 85.25%

Using 52 estimators: Accuracy is: 86.89%

Using 54 estimators: Accuracy is: 83.61%

Using 56 estimators: Accuracy is: 86.89%

Using 58 estimators: Accuracy is: 83.61%

Using 60 estimators: Accuracy is: 85.25%

Using 62 estimators: Accuracy is: 85.25%

Using 64 estimators: Accuracy is: 85.25%

Using 66 estimators: Accuracy is: 86.89%

Using 68 estimators: Accuracy is: 86.89%

Using 70 estimators: Accuracy is: 85.25%

Using 72 estimators: Accuracy is: 81.97%

Using 74 estimators: Accuracy is: 81.97%

Using 76 estimators: Accuracy is: 86.89%

Using 78 estimators: Accuracy is: 86.89%

Using 80 estimators: Accuracy is: 88.52%

Using 82 estimators: Accuracy is: 85.25%

Using 84 estimators: Accuracy is: 85.25%

Using 86 estimators: Accuracy is: 81.97%

Using 88 estimators: Accuracy is: 83.61%

Using 90 estimators: Accuracy is: 81.97%

Using 92 estimators: Accuracy is: 85.25%

Using 94 estimators: Accuracy is: 86.89%

Using 96 estimators: Accuracy is: 86.89%

Using 98 estimators: Accuracy is: 86.89%

80 estimators produced the best accuracy which is 88.5246
"""

import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score


# import the data
file = 'heart.csv'
heart = pd.read_csv(file)

# create features matrix
X = heart.drop('target', axis=1)
# create labels
Y = heart['target']

# choosing the model and hyperparameters
clf = RandomForestClassifier(n_estimators=100)

# generate training and test data
# fit the model to the training data
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)
clf.fit(X_train, Y_train)
# making prediction
y_preds = clf.predict(X_test)
# evaluating the model on the training data
trainSet_score = clf.score(X_train, Y_train)
print(trainSet_score)
# evaluating the model on the test data
testSet_score = clf.score(X_test, Y_test)
print(testSet_score)


# setting a seed so that the result can be reproduced
np.random.seed(42)
# store the highest accuracy
max_acc = 0
# store the n_estimators for which highest accuracy was obtained
estr = 0
# Trying different amount of n_estimators
for i in range(10, 100, 2):
    print(f'Using {i} estimators', end=': ')
    clf = RandomForestClassifier(n_estimators=i)
    clf.fit(X_train, Y_train)
    result = clf.score(X_test, Y_test)
    print(f'Accuracy is: {result * 100:.2f}%')
    print()

    # calculating max value
    if((result * 100) > max_acc):
        max_acc = result * 100
        estr = i

print(f'{estr} estimators produced the best accuracy which is {max_acc:.4f}')
