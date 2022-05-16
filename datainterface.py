# IMPORTS:
# ------------------------------------------------------------
from pyexpat import features
import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score
# ------------------------------------------------------------

class DataInterface:
    '''
    Class that handles splitting data and contains all algorithm actions
    '''
    def __init__(self):
        '''
        Initialises empty data, empty features, empty labels
        '''
        self._data = ""
        self._features = ""
        self._labels = ""

    def getdata(self):
        '''
        gets dataset
        '''
        print(self._data)
        return self._data
    
    def setdata(self, data):
        '''
        sets dataset
        '''
        self._data = data

    def getfeatures(self):
        print(self._features)
        return self._features

    def setfeatures(self, features):
        self._features = features

    def getlabels(self):
        print(self._labels)
        return self._labels
    
    def split_by_cyto(self):
        '''
        Splits data into preset features and labels from cytometry. Returns features, labels.
        '''
        self._features = pd.DataFrame(self._data, columns=['Events | Median (HLA DR-FITC)',
       'Events | Median (CD117-PE)', 'Events | Median (CD45-ECD)',
       'Events | Median (CD34-PC5)', 'Events | Median (CD38-PC7)',
       'Events | Median (FS Lin)', 'Events | Median (SS Log)'])

        self._labels = pd.DataFrame(self._data, columns=['AML?'])

        return self._features, self._labels

    def gauss_naive_bayes(self, features, labels, testsize=0.25, randomstate=53):
        '''
        Performs Gaussian Naive Bayes algorithm with inputed training and testing sets. Returns f1_score, cross validation score

        PARAMETERS:
        split_by_cyto: the return values of split_by_cyto \n
        test_size: float or int, default = 0.25 \n
        random_state: int, default 53
        '''

        X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=testsize, random_state=randomstate)
        
        gnb = GaussianNB()
        gnb.fit(X_train, y_train.values.ravel())
        y_pred = gnb.predict(X_test)

        print(y_test)
        print(y_pred)
        return f1_score(y_test, y_pred), gnb.score(X_test, y_test)

