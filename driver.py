# IMPORT:
# ------------------------------------------------------------
import datainterface
import pandas as pd
# ------------------------------------------------------------

# init datainterface object
di = datainterface.DataInterface()

# sets 'AMLdata.scv' as the dataset for DataInterface object
di.setdata(pd.read_csv("AMLdata.csv"))

# split data into features and labels by preset split function
# specific to THIS DATASET'S CYTOMETRY DATA
features, labels = di.split_by_cyto() # stores features and labels

# performs gaussian naive bayes function on features and labels with seed of 51,
# stores result
z = di.gauss_naive_bayes(features, labels, randomstate=51)

# prints gaussian navie bayes
print(z)