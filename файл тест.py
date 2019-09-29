from spectral import *
import spectral.io.envi as envi
import numpy as np 
import matplotlib.pyplot as plt 
import cv2

lib = envi.open(r'C:\Users\User\Desktop\Спектральные изображения\f080709t01p00r15\f080709t01p00r15rdn_c_ort_igm.hdr', r'C:\Users\User\Desktop\Спектральные изображения\f080709t01p00r15\f080709t01p00r15rdn_c_ort_igm')

print(lib.shape )
print(lib[50,100])
print(lib[50,100].shape)
gt  = envi.open(r'C:\Users\User\Desktop\Спектральные изображения\f080709t01p00r15\f080709t01p00r15rdn_c_ort_igm.hdr', r'C:\Users\User\Desktop\Спектральные изображения\f080709t01p00r15\f080709t01p00r15rdn_c_ort_igm') . read_band ( 0 ) 
print(lib)
print(type(gt))

view  =  imshow (lib ,  ( 0 ,  1 ,  0 ), classes = gt )

view.class_alpha = 0.5


pc = principal_components(lib)
v = imshow(pc.cov)




#( m ,  c )  =  kmeans ( lib ,  20 ,  30 ) 


   


#view_cube ( lib ,  band = [ 0 ,  1 ,  2 ])

#save_rgb ( 'rgb.jpg' ,  lib ,  [ -1 ,  -1 ,  -1 ],colors = spy_colors)
#data= envi.open(r'C:\Users\User\Desktop\Спектральные изображения\f080709t01p00r15\f080709t01p00r15rdn_c_ort_igm.hdr', r'C:\Users\User\Desktop\Спектральные изображения\f080709t01p00r15\f080709t01p00r15rdn_c_ort_igm').load()
#pc = principal_components(data)
#print(type(pc))
#xdata = pc.transform(data)
#
#w = view_nd(xdata[:,:,:10], classes=gt)

