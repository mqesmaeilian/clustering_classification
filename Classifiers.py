from sample_divider import sample_divider_member, get_samples_csv
from sklearn.ensemble.weight_boosting import AdaBoostClassifier
import pandas as pd
import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt
import time

from sklearn.utils.testing import all_estimators
from sklearn.base import ClassifierMixin
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler, LabelEncoder

############ Classifiers

from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn import tree
from sklearn.neural_network import MLPClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.gaussian_process.kernels import RBF
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import AdaBoostClassifier
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
from sklearn.gaussian_process import GaussianProcess

dictionary_of_classifiers = {
    "Logistic Regression": LogisticRegression(),
    "Nearest Neighbors": KNeighborsClassifier(),
    "Linear SVM": SVC(),
    "Gradient Boosting Classifier": GradientBoostingClassifier(n_estimators=1000),
    "Decision Tree": tree.DecisionTreeClassifier(),
    "Random Forest": RandomForestClassifier(n_estimators=1000),
    "Neural Net": MLPClassifier(alpha=1),
    "Naive Bayes": GaussianNB(),
    # "AdaBoost": AdaBoostClassifier(),
    # "QDA": QuadraticDiscriminantAnalysis(),
    # "Gaussian Process": GaussianProcess(),
    # "RBF": RBF()
}


def classification_methods(x_train, y_train, x_test, y_test):
    dict_models = {}
    for classifier_name, classifier in list(dictionary_of_classifiers.items()):
        start_time = time.clock()
        classifier.fit(x_train, y_train)
        stop_time = time.clock()
        training_time = stop_time - start_time

        classifier_train_score = classifier.score(x_train, y_train)
        classifier_test_score = classifier.score(x_test, y_test)

        dict_models[classifier_name] = {
            'Name': classifier,
            'Train_score': classifier_train_score,
            'Test_score': classifier_test_score,
            'Train_time': training_time
        }
    return dict_models

sklearn_classifiers = [est for est in all_estimators() if issubclass(est[1], ClassifierMixin)]
classifiers_name = [item[0] for item in sklearn_classifiers]
classifiers_path = [item[1] for item in sklearn_classifiers]
# for items in classifiers_name:
#     print(items)
# print("All")
# print("")
# command = str(input("Please choose the methods that you want to evaluate : "))
# if command.lower() == "all":






