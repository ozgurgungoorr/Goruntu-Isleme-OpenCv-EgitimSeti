import cv2
import numpy as np
img=cv2.imread("resimler\zeytin.png")
imgGri= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("Zeytin Fotosu",img)
cv2.imshow("Zeytin Fotosu Gri", imgGri)


size_y=img.shape[0]    # yükseklik
size_x=img.shape[1]    # genişlik
#kanal= img.shape[2]    # 



print("Yükseklik :",size_y, "Genişlik",size_x,)


print(img[(100,100)])
print(imgGri[(100,100)])

cv2.waitKey(0)
cv2.destroyAllWindows()
