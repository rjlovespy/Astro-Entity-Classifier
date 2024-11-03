from sklearn.ensemble import IsolationForest
import numpy as np

def remove_outliers_with_isolation_forest(F):
    isolation_forest = IsolationForest(contamination=0.01, random_state=42)   
    is_inlier = isolation_forest.fit_predict(F) == 1                          
    if len(is_inlier) == 99999:
        np.save("inlier_index.npy", np.where(is_inlier==True)[0])              
    return F[is_inlier] 
