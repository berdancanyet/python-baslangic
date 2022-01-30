import cv2
import numpy as np
resim=cv2.imread('C:\\resim\\test.jpg')
y=resim.shape[0]
x=resim.shape[1]
k=resim.shape[2]
print('Resmin x uzunlugu:',x,',y uzunlugu:',y,' ,kanal sayisi:',k,'') #Örnek çıktı: Resmin x uzunlugu: 720 ,y uzunlugu: 383  ,kanal sayisi: 3 
cv2.imshow('Resmimiz', resim)
cv2.waitKey()
cv2.destroyAllWindows()
