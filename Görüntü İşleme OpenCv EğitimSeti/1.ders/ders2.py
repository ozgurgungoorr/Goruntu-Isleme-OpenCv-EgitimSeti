import cv2
import numpy as np
img=cv2.imread("resimler\zeytin.png")


#karnel= np.ones((3,3),np.float32)/9
#blur=cv2.filter2D(img,-1,karnel)
#blur=cv2.blur(img,(10,10))
#karnel= np.array([-1,-1,-1],
                # [-1,9,-1],
                # [-1,-1,-1])
#keskinlestirme=cv2.filter2D(img, -1 karnel)
#gaus= cv2.GaussianBlur(img,(5,5),0)
#bilateral= cv2.bilateralFilter(img,9,75,75)
#median= cv2.medianBlur(img,11)


canny= cv2.Canny(img,10,200)


cv2.imshow("Zeytin Fotosu ",img)
cv2.imshow("Zeytin Fotosu Bulanik",canny)


cv2.waitKey(0)
cv2.destroyAllWindows()


