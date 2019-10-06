import random
import numpy as np
import matplotlib.pyplot as plt
import cv2
img=cv2.imread('C:/Users/User/Desktop/repo/depositphotos_122778520-stock-illustration-seamless-background-colored-dots.jpg')
image=np.array(img)
size= np.shape(image)
N=size[0]*size[1]

k=3
n= float(N)/k# среднее, все точки делить на кол-во кластеров, среднее кол-во точек для одного кластера
X=[]
for i in range(k):
    c = (random.uniform(image[0,0,0], image[1023,1023,2]), random.uniform(image[0,0,0], image[1023,1023,2]))# uniform принимает от скольки до скольки(интервал) и размер. Это кортеж
    s=random.uniform(1,4) # значение
    x=[]
    while len(x)<n:
        a=np.random.normal(c[0], s)# normal принимает центр распределения, ширина отклонения
        b=np.random.normal(c[1], s)# normal принимает центр распределения, ширина отклонения
#        a, b = np.array([np.random.normal(c[0], s), np.random.normal(c[1], s)])
        #Продолжаем рисовать точки из распределения в диапазоне [-1,1]
        if abs(a)<3 and abs(b)<3:# возвращает модуль числа
            x.append([a,b])
    X.extend(x)# удлиняет список, добавлят элементы, конкретно a и b, а не [a,b]
    
z=np.zeros( ( 1024,1024 ) ) 

X = np.array(X)[:N][:4]
print(type(X))
#X=np.array(X).reshape( ( 1024,1024 ) ) 
#print(np.shape(X))
#for i in range(10):
#    for j in range(10):
#        k=X[i,j]
#        z[i,j]=k
#
##plt.imshow(z,cmap=plt.cm.bone)
##cv2.imshow('bilateralFilter',z)
##
##
##
##cv2.waitKey(0)
##cv2.destroyAllWindows()
###        
#    
#    
#
#
#
#
#    
#
#
#
#
#
