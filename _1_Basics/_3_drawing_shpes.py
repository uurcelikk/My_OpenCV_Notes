import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3),dtype = 'uint8')
cv.imshow('Blank',blank)

blank[200:300,300:400] = 0,0,255 #siyah ekran içinde belirli pikselleri kırmızya döndürür
#blank[:] = 0,255,0 yeşil ekran
cv.imshow('red',blank)

# Draw a rectangle

# cv.rectangle(blank,(0,0), (250,250),(0,255,0),thickness=cv.FILLED)
# cv.imshow('Rectangle',blank)
cv.rectangle(blank,(0,0), (blank.shape[1] // 2, blank.shape[0] // 2),
             (0,255,0),
             thickness=4)
cv.imshow('Rectangle',blank)



# Draw a Circle
cv.circle(blank,(blank.shape[1] // 2, blank.shape[0] // 2),
          40,(0,0,255),thickness = -1)
cv.imshow('Circle',blank)



#Draw a Line
cv.line(blank, (100,250),(300,400),(255,255,255),
        thickness=4)
cv.imshow('line',blank)



# Write text
cv.putText(blank,'Hello',(255,255),cv.FONT_HERSHEY_TRIPLEX,1.0,(0,255,0),2)
cv.imshow('Text',blank)
cv.waitKey(0)



"""
Bir resim üzerinde çizimler yapmak için sahte bir görsel hazirlanir.

"""