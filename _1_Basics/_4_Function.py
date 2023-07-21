import cv2 as cv
img = cv.imread('Photos/cats.jpg')
cv.imshow('img',img)

#Converting to grayscale
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)


#Blur
blur = cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)
cv.imshow('blur',blur)
"""
Görüntüyü Blurlama, bir nevi gürültünün bir kısmını ortadan kaldırmasını sağlar.

"""

#Edge Cascode
canny = cv.Canny(img,125,175)
cv.imshow('Canny Edge', canny)


# Dilating the image
dilated = cv.dilate(canny,(3,3),iterations=3)
cv.imshow('Dilated',dilated)

#Eroded
eroded = cv.erode(dilated,(7,7),iterations=3)
cv.imshow('Eroded',eroded)


cv.waitKey(0)