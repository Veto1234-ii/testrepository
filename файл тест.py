from spectral import *
import spectral.io.envi as envi
import numpy as np 
import matplotlib.pyplot as plt 
import cv2

lib = envi.open(r'C:\Users\IT\Documents\Image spectral\f090729t01p00r09\f090729t01p00r09rdn_b\f090729t01p00r09rdn_b_ort_igm.hdr', r'C:\Users\IT\Documents\Image spectral\f090729t01p00r09\f090729t01p00r09rdn_b\f090729t01p00r09rdn_b_ort_igm')

print(lib.shape )
print(lib[50,100])
print(lib[50,100].shape)
gt  = envi.open(r'C:\Users\IT\Documents\Image spectral\f090729t01p00r09\f090729t01p00r09rdn_b\f090729t01p00r09rdn_b_ort_igm.hdr', r'C:\Users\IT\Documents\Image spectral\f090729t01p00r09\f090729t01p00r09rdn_b\f090729t01p00r09rdn_b_ort_igm') . read_band ( 1 ) 
print(lib)
print(type(gt))

view  =  imshow (lib ,  ( 2 ,  2 ,  2 ), classes = gt )

view.class_alpha = 0.5


#pc = principal_components(lib)
#v = imshow(pc.cov)





( m ,  c )  =  kmeans ( lib ,  2 ,  2 ) 


   


#save_rgb ( 'rgb.jpg' ,  lib ,  [ -1 ,  -1 ,  -1 ],colors = spy_colors)
#data= envi.open(r'C:\Users\User\Desktop\Спектральные изображения\f080709t01p00r15\f080709t01p00r15rdn_c_ort_igm.hdr', r'C:\Users\User\Desktop\Спектральные изображения\f080709t01p00r15\f080709t01p00r15rdn_c_ort_igm').load()
#pc = principal_components(data)
#print(type(pc))
#xdata = pc.transform(data)
#
#w = view_nd(xdata[:,:,:10], classes=gt)

