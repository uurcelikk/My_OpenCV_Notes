import cv2 as cv
import numpy as np  

img = cv.imread('Photos/lady.jpg')

cv.imshow('Lady', img)

# Translation
""" Translation temelde bir görüntüyü x boyunca kaydırıyor.

"""

# görüntüyü fonksiyon içine alıyoruz.
# x ve y temel olarak kaydırmak istediğiniz piksel sayısını ifade eder.

def translate(img, x, y):
    transMat = np.float32([[1,0,x], [0,1,y]])
    dimensions = (img.shape[1],img.shape[0])
    # 1 genişlik 0 yükseklik
    return cv.warpAffine(img,transMat,dimensions)

#- x --> left
# -y --> up
# x --> right
# y --> Down

translated =translate(img, -100,100)
cv.imshow('translated', translated)

# Rotation

def rotate(img, angle, rotPoint = None):
    (height, widht) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (widht // 2, height // 2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0) # 3.parametre ölçeklendirme
    dimensions = (widht, height)

    return cv.warpAffine(img,rotMat,dimensions)
rotated = rotate(img, -45)
cv.imshow('Rotated', rotated)


# Resizing
resized = cv.resize(img,(500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized',resized)

# Flip
flip = cv.flip(img, 0)
cv.imshow('Flip',flip)
cv.waitKey(0)