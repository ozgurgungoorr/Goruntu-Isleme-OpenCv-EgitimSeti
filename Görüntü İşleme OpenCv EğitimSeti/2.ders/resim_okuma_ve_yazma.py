import cv2

# img = cv2.imread('frame.png')




#img = cv2.imread('frame.png', cv2.IMREAD_GRAYSCALE)
#İKİSİDE AYNI GÖREVİ GÖRÜYOR
#img = cv2.imread('frame.png', 0)


#cv2.imshow('Profil', img)

#cv2.waitKey(0)
#kInp = cv2.waitKey(0)
#print(kInp)


#if kInp == 97:
#    print('a tuşuna basıldı')
#else:
#    print('başka bir tuşa basıldı')    
#cv2.destroyAllWindows()






#if kInp == ord('a'):
#    print('a tuşuna basıldı')
#else:
#    print('başka bir tuşa basıldı')    
#cv2.destroyAllWindows()



#img = cv2.imread('frame.png')

img = cv2.imread('frame.png', 0)

cv2.imwrite('me2.png', img)