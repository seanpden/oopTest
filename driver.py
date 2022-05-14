# IMPORT:
# ------------------------------------------------------------
import datainterface
import pandas as pd
# ------------------------------------------------------------

di = datainterface.DataInterface() # init object
di.setdata(pd.read_csv("AMLdata.csv")) # sets data
features, labels = di.split_by_cyto() # stores features and labels
z = di.gauss_naive_bayes(features, labels, randomstate=51) # perform gauss naive bayes algo with a randomstate seed of 51
print(z)