"""

Muhammadsadeq Esmaeilian
August 21, 2018

Description:
    This python file will generate the type of data that you want
    but randomly!!!(With a little use of numpy random number generator.)
    You can also save your data on txt, xml, csv, json etc files.
    There are types of data like:
                                       1. Data Package (include 'sample' & 'features')
                                       2. Data Package Pro (include 'sample' & 'features' with Pro features)
                                       3. Sample Package (include 'sample')
                                       4. Features Package (include 'features')
                                       
    So for learning the data science and machine learning
    the first step is having the data to work with.
    For beginners this is the start.
     
"""

import numpy as np


def KMean_data_generator(samples, min, max, features):
    """
    :param samples: An INTEGER
    :param min:
    :param max:
    :param features:
    :return:
    """
    n_samples = np.random.randint(size=samples, low=min, high=max)
    i = 2
    n_features = []
    for i in range(samples):
        m_lst = []
        lst = 10 * (np.random.random_sample(size=features))
        for j in range(0, len(lst)):
            m_lst.append(lst[j])
            j += 1
        n_features.append(m_lst)
        i += 1

    data = n_samples, n_features
    return data


def KMean_feature_generator(features, samples):
    """
    :param features:
    :param samples:
    :return:
    """
    n_features = []
    for i in range(samples):
        m_lst = []
        lst = 10 * (np.random.random_sample(size=features))
        for j in range(0, len(lst)):
            m_lst.append(lst[j])
            j += 1
        n_features.append(m_lst)
        i += 1

    features = n_features
    return features

# x = input("Please select one of these packages :\n"
#           "Data Package \n"
#           "Data Package Pro \n"
#           "Sample Package \n"
#           "Feature Package \n"
#           "I choose :")
# y = input("I want to get my data on :\n"
#           "txt file \n"
#           "xml file \n"
#           "csv file \n"
#           "json file \n"
#           "I choose :")
