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
        self.data = ""
        self.features = ""
        self.labels = ""

    def getdata(self):
        '''
        gets dataset
        '''
        print(self.data)
        return self.data
    
    def setdata(self, data):
        '''
        sets dataset
        '''
        self.data = data

    def getfeatures(self):
        print(self.features)
        return self.features

    def setfeatures(self, features):
        self.features = features

    def getlabels(self):
        print(self.labels)
        return self.labels
    
    def split_by_cyto(self):
        '''
        Splits data into preset features and labels from cytometry. Returns features, labels.
        '''
        self.features = pd.DataFrame(self.data, columns=['Events | Median (HLA DR-FITC)',
       'Events | Median (CD117-PE)', 'Events | Median (CD45-ECD)',
       'Events | Median (CD34-PC5)', 'Events | Median (CD38-PC7)',
       'Events | Median (FS Lin)', 'Events | Median (SS Log)'])

        self.labels = pd.DataFrame(self.data, columns=['AML?'])

        return self.features, self.labels

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

