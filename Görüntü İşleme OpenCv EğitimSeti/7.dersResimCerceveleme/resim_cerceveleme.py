import cv2
import matplotlib.pyplot as plt
import os

# Görüntü dosyası yolu
img_path = '7.dersResimCerceveleme\\dene.png'

# Görüntüyü yükleme
img = cv2.imread(img_path)

# Görüntü başarılı bir şekilde yüklendi mi kontrol et
if img is None:
    print(f"Error: File {img_path} could not be loaded.")
else:
    # BGR'den RGB'ye dönüştürme
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    replicate = cv2.copyMakeBorder(img_rgb, 10, 10, 10, 10, cv2.BORDER_REPLICATE)
    reflect = cv2.copyMakeBorder(img_rgb, 10, 10, 10, 10, cv2.BORDER_REFLECT)
    reflect_101 = cv2.copyMakeBorder(img_rgb, 10, 10, 10, 10, cv2.BORDER_REFLECT_101)
    wrap = cv2.copyMakeBorder(img_rgb, 10, 10, 10, 10, cv2.BORDER_WRAP)
    greenColor = [0, 255, 0]
    constant = cv2.copyMakeBorder(img_rgb, 10, 10, 10, 10, cv2.BORDER_CONSTANT, value=greenColor)

    # Görüntüleri matplotlib ile gösterme
    plt.subplot(2, 3, 1), plt.imshow(img_rgb), plt.title('ORIGINAL')
    plt.subplot(2, 3, 2), plt.imshow(replicate), plt.title('REPLICATE')
    plt.subplot(2, 3, 3), plt.imshow(reflect), plt.title('REFLECT')
    plt.subplot(2, 3, 4), plt.imshow(reflect_101), plt.title('REFLECT_101')
    plt.subplot(2, 3, 5), plt.imshow(wrap), plt.title('WRAP')
    plt.subplot(2, 3, 6), plt.imshow(constant), plt.title('CONSTANT')

    plt.show()
