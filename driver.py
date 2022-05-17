# IMPORT:
# ------------------------------------------------------------
from re import X
import datainterface
import pandas as pd
# ------------------------------------------------------------

# init datainterface object
di = datainterface.DataInterface()

# sets 'AMLdata.scv' as the dataset for DataInterface object
di.setdata(pd.read_csv("AMLdata.csv"))

# split data into features and labels by preset split function
# specific to THIS DATASET'S CYTOMETRY DATA
features, labels = di.split_by_cyto()

# performs gaussian naive bayes function on features and labels with seed of 51,
# stores result
z = di.gauss_naive_bayes(features, labels, randomstate=51)

# prints gaussian navie bayes
print(z)

# performs forest random tree function on features and labels with seed of 51,
# stores results
y = di.forest_random_tree(features, labels, randomstate=51)

# prints forest random tree
print(y)

# performs decision tree algo on features and labels, stores PNG in folder,
# doesn't show result in window
x = di.decision_tree(features, labels, False)
