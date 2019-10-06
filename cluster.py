import matplotlib.pyplot as plt
import numpy as np
from scipy import ndimage
import imageio
from sklearn import cluster
import cv2
image = imageio.imread('C:/Users/User/Desktop/repo/main_slider_066027fe9b.png')
plt.figure(figsize = (15,8))
#plt.imshow(image)
#Для кластеризации изображения  нужно преобразовать его в двумерный массив
x, y, z = image.shape
image_2d = image.reshape(x*y, z)
print(image_2d.shape)

kmeans_cluster = cluster.KMeans(n_clusters=10)# алгоритм
kmeans_cluster.fit(image_2d)# находит средства 
cluster_centers = kmeans_cluster.cluster_centers_
cluster_labels = kmeans_cluster.labels_# метки
print(cluster_labels)
plt.figure(figsize = (15,8))
c= np.array(cluster_centers[cluster_labels]).reshape(x*y, z)
plt.imshow(с)
plt.show()


