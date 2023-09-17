import cv2 as cv
import numpy as np
img = cv.imread('Photos/park.jpg')
cv.imshow('park',img)

blank = np.zeros(img.shape[:2], dtype = 'uint8')

b,g,r= cv.split(img)

cv.imshow('Blue',b)
cv.imshow('Green',g)
cv.imshow('Red',r)
"""Görüntüleri gösterdiğimizde tek kanallı oldukları için grayscale şeklinde olacaklardır.
Temsil edilen kanallar ise, orjinal görselde nerede yoğunlukları fazla ise ayrılan görselde beyaza dönüşürler.
Örneğin blue görselinde mavi renkli alanlar olan gökyüzünü beyaz olarak ortaya çıkarır.

"""

blue = cv.merge([b,blank,blank])
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])

cv.imshow('Blue',blue)
cv.imshow('Green',green)
cv.imshow('Red',red )


print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)
 
# Şimdi ayrılmış görselleri mergeleme işlemi ile birleştirelim
merged = cv.merge([b,g,r])
cv.imshow("merged", merged)

cv.waitKey(0)