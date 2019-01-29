### a simple script show how to change a methods parameter




import pandas as pd
import numpy as np
from sklearn.ensemble import gradient_boosting

parameters = {
    'n_estimators': [100, 500, 1000],
    'learniong_rate': [0.5, 0.1, 0.01, 0.001],
    'citerion': ['friedman_mse', 'mse', 'mae']
}

# gradiant_boosting(sample, parameters)
