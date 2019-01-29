### Example 1 of classification with one of the sklearn random data generator (make_blobs)



from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

X, y = make_blobs(n_samples=800, n_features=3, centers=4)



# def create_file():
#     f = open('data.txt', 'w')
#     f.write(str(data))
#     f.close()
# create_file()
fig = plt.figure()
ax = Axes3D(fig)
ax.scatter(X[:, 0], X[:, 1], X[:, 2])
# #
kmeans = KMeans(n_clusters=4)
kmeans.fit(X)
labels = kmeans.predict(X)
fig = plt.figure()
ax = Axes3D(fig)
ax.scatter(X[:, 0], X[:, 1], X[:, 2], c=y)
C = kmeans.cluster_centers_
#print (">>>>>",C,"<<<<<")


#
# ax.scatter(X[labels ==0,0], X[labels == 0,1], s=50, c='red')
# ax.scatter(X[labels ==1,0], X[labels == 1,1], s=50, c='black')
# ax.scatter(X[labels ==2,0], X[labels == 2,1], s=50, c='blue')
# # ax.scatter(X[labels ==3,0], X[labels == 3,1], s=50, c='cyan')

for angle in range(70, 360, 80):
    ax.view_init(elev=20., azim=angle)
    plt.draw()
    plt.pause(1)
