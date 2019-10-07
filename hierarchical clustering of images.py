import random
import numpy as np
from sklearn.cluster import AgglomerativeClustering
import matplotlib.pyplot as plt



N=800
k=5
X1 = np.array([(random.uniform(-1,1), random.uniform(-1,1)) for i in range(N)])




plt.figure(figsize=(10, 7))
plt.subplots_adjust(bottom=0.0)

plt.scatter(X1[:,0],X1[:,1], label='True Position')

#for label, x, y in zip( X1[:, 0], X1[:, 1]):
#    plt.annotate(
#        label,
#        xy=(x, y), xytext=(-3, 3),
#        textcoords='offset points', ha='right', va='bottom')
plt.show()
#
#
#
#
#
#        
cluster = AgglomerativeClustering(n_clusters=k, affinity='euclidean', linkage='ward')
#  affinity='euclidean' - расстояние между точками данных
# linkage='ward' - минимуму варианта между кластерами.
cluster.fit_predict(X1)#возвращает имена кластеров, которым принадлежит каждая точка данных, метки
#цифры являются просто метками, назначенными кластерам, и не имеют математического значения.

plt.scatter(X1[:,0],X1[:,1], c=cluster.labels_, cmap='rainbow')






