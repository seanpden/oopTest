# IMPORTS:
# ------------------------------------------------------------
from pyexpat import features
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score
import matplotlib.pyplot as plt
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

    def gauss_naive_bayes(self, _features, _labels, testsize=0.25, randomstate=53):
        '''
        Performs Gaussian Naive Bayes algorithm with inputed training and testing sets. 
        Returns f1_score, cross validation score

        PARAMETERS:
        features: the feature return value of split_by_cyto \n
        labels: the label return value of split_by_cyto \n
        test_size: float or int, default = 0.25 \n
        If float, should be between 0.0 and 1.0 and represent the proportion of the dataset to include in the test split. \n
        If int, represents the absolute number of test samples.
        random_state: int, default 53
        '''

        X_train, X_test, y_train, y_test = train_test_split(_features, _labels, test_size=testsize, random_state=randomstate)
        
        gnb = GaussianNB()
        gnb.fit(X_train, y_train.values.ravel())
        y_pred = gnb.predict(X_test)

        # print(y_test)
        # print(y_pred)
        return f1_score(y_test, y_pred), gnb.score(X_test, y_test)

    def forest_random_tree(self, _features, _labels, testsize=0.25, randomstate=53):
        '''
        Performs the RandomForest algorithm with the training and testing sets,
        Returns the f1_score, cross validation score.

        PARAMETERS:
        features: the feature return value of split_by_cyto \n
        labels: the label return value of split_by_cyto \n
        test_size: float or int, default = 0.25 \n
        If float, should be between 0.0 and 1.0 and represent the proportion of the dataset to include in the test split. \n
        If int, represents the absolute number of test samples.
        random_state: int, default 53
        '''

        X_train, X_test, y_train, y_test = train_test_split(_features, _labels, test_size=testsize, random_state=randomstate)

        clf = RandomForestClassifier(n_estimators=100)
        clf.fit(X_train, y_train.values.ravel())
        y_pred = clf.predict(X_test)

        # print(y_test)
        # print(y_pred)
        return f1_score(y_test, y_pred), clf.score(X_test, y_test)

    def decision_tree(self, _features, _labels, show=False):
        '''
        Calculates and outputs a PNG of a decision tree classifying algorithm

        PARAMETERS:
        _features: the feature return value of split_by_cyto \n
        _labels: the label return value of split_by_cyto \n
        show: boolean, show plot on screen
        '''

        plt.figure(dpi=200)
        clf = tree.DecisionTreeClassifier().fit(_features, _labels)
        tree.plot_tree(clf, filled=True)
        plt.title("Decision tree with all features")
        plt.savefig("decision_tree_output")

        if show == True:
            plt.show()