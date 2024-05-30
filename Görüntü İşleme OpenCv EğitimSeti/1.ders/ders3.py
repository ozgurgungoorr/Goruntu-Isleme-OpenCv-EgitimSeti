import cv2 
img=cv2.imread(r"resimler/zeytin.png",0)
cv2.line(img,(0,0),(350,400),(200,0,100),10)
cv2.rectangle(img,(100,100),(300,200),(255,100,0),-1)
cv2.circle(img,(300,300),50,(100,200,200),150)
cv2.ellipse(img,(300,300),(100,200),45,0,180,(0,100,255),5)


cv2.putText(img,'OPENCV',(100,0),cv2.FONT_HERSHEY_COMPLEX,5,(100,100,100),3,cv2.LINE_AA,True)


cv2.imwrite("zeytingri.png",img)
cv2.imshow("Zeytin Fotosu",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
