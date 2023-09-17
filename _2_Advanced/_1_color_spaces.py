import cv2 as cv
import matplotlib.pyplot as plt
img = cv.imread('Photos/cat.jpg')
cv.imshow('Boston',img)

#BGR to Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)
# Gri tonlamalı görüntüler genellikle piksel dağılımını gösterir bize."


#BGR to HSV
hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow('hsv',hsv)

#BGR to LAB
lab = cv.cvtColor(img,cv.COLOR_BGR2LAB)
cv.imshow('lab',lab)

# BGR to RGB
rgb = cv.cvtColor(img,cv.COLOR_BGR2RGB)
cv.imshow('rgb',rgb)
cv.waitKey(0)