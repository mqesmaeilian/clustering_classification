from sample_divider import sample_divider_member,get_samples_csv, xy_divider
from Classifiers import classification_methods



filename = 'glass.csv'
train_list_members, test_list_members = sample_divider_member(filename, 70)
get_samples_csv(filename, train_list_members, test_list_members)
X_Train, Y_Train = xy_divider('Train_Data.csv', 'Type')
X_Test, Y_Test = xy_divider('Test_Data.csv', 'Type')
results = classification_methods(X_Train,Y_Train, X_Test,Y_Test)
print(results)



