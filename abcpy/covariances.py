import sklearn.covariance
import numpy as np

def cov_sklearn(x):
    return(sklearn.covariance.MinCovDet().fit(np.array(x)).covariance_)
