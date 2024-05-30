import cv2

vid = cv2.VideoCapture(0)


while True:
    
    ret, frame = vid.read()
    
    cv2.imshow('frame' frame)
    
    kInp = cv2.waitKey(0)
    
    
    if kInp == ord('q'):
        break
    
    
    
vid.release()
cv2.destroyAllWindows()