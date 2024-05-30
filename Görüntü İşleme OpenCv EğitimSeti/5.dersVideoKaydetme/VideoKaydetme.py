import cv2

vid = cv2.VideoCapture(0)

w = int(vid.get(3))
h = int(vid.get(4))


size = (w, h)

result = cv2.VideoWriter('record.avi', cv2.VideoWriter_fourcc(*'XVID'), 24, size)

while True:
    ret, frame = vid.read()
    
    if ret == True:
        result.write(frame)
        
        
        cv2.imshow('frame', frame)
        
        kInp = cv2.waitKey(1)
        if kInp == ord('s'):
            break
        else:
            break
        
vid.release()
result.release()
cv2.destroyAllWindows()


print('Ekranın video kaydı başarılı bir şekilde alındı.')