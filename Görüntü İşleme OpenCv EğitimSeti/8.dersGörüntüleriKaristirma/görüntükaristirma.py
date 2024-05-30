import cv2

img1 = cv2.imread('')   #deger girilecek
img2 = cv2.imread('')
print('img1:', img1.shape)
print('img2:', img2.shape)





totalImg = cv2.add(img1, img2)

print(img1[0, 0])
print(img2[0, 0])
print('totalImg', totalImg[0, 0])


# bu kodu eksik yaptım tamamlanması gerek