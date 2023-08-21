import cv2 as cv
import numpy as np

img = cv.imread('Photos/cats.jpg')
cv.imshow('img',img)

#2.contour bulma şekli

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

ret,thresh = cv.threshold(gray, 125,255,cv.THRESH_BINARY)
cv.imshow('Thresh',thresh)

contours, hierarchies = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE )
print(f'{len(contours)}: counters found!')
# 
# 125 eşik değeri. geçtiyse beyaz, geçmediyse siyah yani 0 olarak temsil edilir.
# 255 maksimum  pixel değeri
"""
cv.THRESH_BINARY: Eşikleme türü olarak kullanılan bir sabit. 
Bu tür, piksel değeri eşik değerini geçiyorsa, piksel değerini belirtilen maksimum değere (burada 255) ayarlar. 
Geçmiyorsa, piksel değerini 0 olarak ayarlar
"""

#renklendirme yapalım
blank = np.zeros(img.shape,dtype = 'uint8')
cv.imshow('blank',blank)
cv.drawContours(blank, contours,-1, (0,0,255),2)
#-1 parametresi: tüm konturları çizmesini belirtir. 0 olsayı ilk kontur 1 olsaydı ikinci konturları 
# 2 paramtresi kalınlık için.
cv.imshow('contours Drawn', blank)
cv.waitKey(0)