### dividing data to 2 group's of 'Test_data' and 'Train_data' (randomly to reduce error function)


import numpy as np
import pandas as pd


def sample_divider_member(sample, rate):
    data = pd.read_csv(sample)
    lst = []
    for i in range(1, len(data) + 1):
        while True:
            n = np.random.randint(1, len(data) + 1)
            if n in lst:
                continue
            else:
                lst.append(n)
                break
    Number_of_train_samples = int(round((rate / 100) * len(data)))
    train_lst = lst[:Number_of_train_samples]
    test_lst = lst[Number_of_train_samples:]
    return train_lst, test_lst


def get_samples(sample, train_members, test_members):
    data = pd.read_csv(sample)
    train_data = []
    test_data = []
    for i in train_members:
        trn_data = data[i:i + 1]
        train_data.append(trn_data)
    for j in test_members:
        tst_data = data[j:j + 1]
        test_data.append(tst_data)
    return train_data, test_data


def get_samples_csv(sample, train_members, test_members):
    data = pd.read_csv(sample)
    train_data = pd.DataFrame([], columns=[x for x in data.columns])
    test_data = pd.DataFrame([], columns=[x for x in data.columns])
    for i in train_members:
        trn_data = data[i:i + 1]
        train_data = train_data.append(trn_data)
    for j in test_members:
        tst_data = data[j:j + 1]
        test_data = test_data.append(tst_data)
    train_data.to_csv("Train_Data.csv", float_format='%.5f')
    test_data.to_csv("Test_Data.csv", float_format='%.5f')


def xy_divider(sample, y_dimensions):
    data = pd.read_csv(sample)
    x_dimensions = list(data.columns.values)
    x_dimensions.remove(y_dimensions)
    y_dimensions = y_dimensions
    X = data[x_dimensions].values
    Y = data[y_dimensions].values
    return X, Y





