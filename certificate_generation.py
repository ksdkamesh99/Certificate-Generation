# -*- coding: utf-8 -*-
"""Certificate_generation.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Nf0gltkoASW6EDmTIrFop_GdQh5j0m1_
"""

#cd /content/drive/My Drive/Certificate Generation

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cv2

dataset=pd.read_csv('dataset.csv')

#dataset

img=cv2.imread('template_final.png')
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
img=cv2.resize(img,(1450,1000))

#plt.imshow(img)

name=dataset['Name']
event=dataset['Event']
serial=dataset['Serial No']


font = [cv2.FONT_HERSHEY_TRIPLEX,
cv2.FONT_HERSHEY_COMPLEX_SMALL,
cv2.FONT_HERSHEY_SCRIPT_COMPLEX,
cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,
cv2.FONT_HERSHEY_SIMPLEX,
cv2.FONT_HERSHEY_PLAIN,
cv2.FONT_HERSHEY_DUPLEX,
cv2.FONT_HERSHEY_COMPLEX]

print('1.FONT_HERSHEY_TRIPLEX  2.FONT_HERSHEY_COMPLEX_SMALL  3.FONT_HERSHEY_SCRIPT_COMPLEX  4.FONT_HERSHEY_SCRIPT_SIMPLEX  5.cv2.FONT_HERSHEY_SIMPLEX  6.FONT_HERSHEY_PLAIN  7.cv2.FONT_HERSHEY_DUPLEX  8.cv2.FONT_HERSHEY_COMPLEX')
x = int(input("Enter an Integer between 1 to 8 ")) - 1
for i in range(len(name)):
  image=np.array(img)
  cv2.putText(image,name[i],(550,450),font[x],1,(0,0,0),cv2.LINE_4)
  cv2.putText(image,event[i],(550,590),font[x],1,(0,0,0),cv2.LINE_4)
  cv2.putText(image,"Serial No:-"+serial[i],(1100,230),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,0,0),1)
  no=serial[i].replace('TCF/NITP/','')
  print(no)
  #plt.imshow(image)
  plt.imsave("Certificates/"+no+".png",image)
  #plt.show()
  del(image)

