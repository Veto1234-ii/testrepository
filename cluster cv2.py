import numpy as np
import cv2
import imageio

img=imageio.imread('C:/Users/User/Desktop/repo/depositphotos_122778520-stock-illustration-seamless-background-colored-dots.jpg')
Z = img.reshape((-1,3))

# convert to np.float32
Z = np.float32(Z)

# define criteria, number of clusters(K) and apply kmeans()
criteria = (5, 10, 1.0)
K = 8
ret,label,center=cv2.cv2.kmeans(Z,K,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)

# Now convert back into uint8, and make original image
center = np.uint8(center)
res = center[label.flatten()]
res2 = res.reshape((img.shape))


cv2.imshow('res',img)
cv2.imshow('res2',res2)
cv2.waitKey(0)
cv2.destroyAllWindows()
