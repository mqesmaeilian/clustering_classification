### Example 3 of classification with sklearn 
### September 16, 2018



from KMeans_Data import KMean_data_generator
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

sample = int(input("How many samples do you want to generate?"))
min = int(input("Please insert the minimum of the samples :"))
max = int(input("Please insert the maximum of the samples :"))
features = int(input("How many features do you want to generate?"))
y, X =  KMean_data_generator(samples=sample,min=min,max=max,features=features)
x, Y =  KMean_data_generator(samples=sample,min=min,max=max,features=features)

f0 = [X[int(i/2)][0] for i in range(len(X))]
f1 = [X[int(i/2)][1] for i in range(len(X))]
f2 = [X[int(i/2)][2] for i in range(len(X))]
s0 = [Y[int(i/2+1)][0] for i in range(len(Y))]
s1 = [Y[int(i/2+1)][1] for i in range(len(Y))]
s2 = [Y[int(i/2+1)][2] for i in range(len(Y))]

fig = plt.figure()
ax = Axes3D(fig)
ax.scatter(f0, f1, f2)
ax.scatter(s0, s1, s2,color="r")

for angle in range(70, 360, 80):
    ax.view_init(elev=20., azim=angle)
    plt.draw()
    plt.pause(1)


# # #
# kmeans = KMeans(n_clusters=2)
# kmeans.fit(X)
# labels = kmeans.predict(X)
# fig = plt.figure()
# ax = Axes3D(fig)
# ax.scatter(f0,f1,f2,c=y)
# C = kmeans.cluster_centers_
# print (">>>>>",C,"<<<<<")
#
#
# #
# # ax.scatter(X[labels ==0,0], X[labels == 0,1], s=50, c='red')
# # ax.scatter(X[labels ==1,0], X[labels == 1,1], s=50, c='black')
# # ax.scatter(X[labels ==2,0], X[labels == 2,1], s=50, c='blue')
# # # ax.scatter(X[labels ==3,0], X[labels == 3,1], s=50, c='cyan')
#
# for angle in range(70, 360, 80):
#     ax.view_init(elev=20., azim=angle)
#     plt.draw()
#     plt.pause(1)

