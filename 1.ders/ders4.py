import cv2
import numpy as np
from matplotlib import pyplot as plt


imgGri= cv2.imread("resimler\zeytin.png",0)
e,tresh1= cv2.threshold(imgGri, 80, 255, cv2.THRESH_BINARY)
e,tresh2= cv2.threshold(imgGri, 80, 255, cv2.THRESH_BINARY_INV)
e,tresh3= cv2.threshold(imgGri, 80, 255, cv2.THRESH_OTSU)
e,tresh4= cv2.threshold(imgGri, 80, 255, cv2.THRESH_TOZERO)
e,tresh5= cv2.threshold(imgGri, 80, 255, cv2.THRESH_TOZERO_INV)
e,tresh6= cv2.threshold(imgGri, 80, 255, cv2.THRESH_TRUNC)

titlelist=["BINARY","BINARY_INV","OTSU","TOZERO", "TOZERO_INV","TRUNC"]
imglist= [tresh1,tresh2,tresh3,tresh4,tresh5,tresh6]


for i in range(6):
    plt.subplot(2,3,i+1), plt.imshow(imglist[i],"gray",vmin=0,vmax=255)
    plt.title(titlelist[i])
    plt.xticks([]),plt.yticks([])
plt.show()


#cv2.imshow("BINARY",tresh1)


cv2.waitKey(0)
cv2.destroyAllWindows()