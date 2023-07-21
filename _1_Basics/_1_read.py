import cv2 as cv

img = cv.imread('Photos/cat.jpg')

cv.imshow('Cat',img)


#cv.waitKey() işlevi, programın belirli bir süre boyunca beklemesini sağlar
# ve klavyeden bir tuşa basıldığında tuşun ASCII değerini döndürür

#cv.waitKey(0) ise, programın klavyeden bir tuşa basılana kadar sürekli beklemesini sağlar.
#  Yani, sıfır olarak belirtilen parametre beklemeyi sonsuz bir süre olarak ayarlar. 

# Reading Videos
capture = cv.VideoCapture('Videos/dog.mp4')

while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break
capture.relase()#video yakalayıcısını serbest bırakır ve video kaynağını kapatır
cv.destroyAllWindows()# tüm açık pencereleri kapatır
cv.waitKey(0)