import cv2 as cv

img = cv.imread('Photos/cat_large.jpg')
cv.imshow('Cat',img)

def rescaleFrame(frame,scale= 0.4):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)

    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)
#img
resized_img = rescaleFrame(img)
cv.imshow('Resized_img ', resized_img)



#Video
capture = cv.VideoCapture('Videos/dog.mp4')
while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame)

    cv.imshow('cat',frame)
    cv.imshow('Cat_resized', frame_resized)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows
cv.waitKey(0)
"""Bir görüntüyü veya videoyu işlerken içinde barındırdığı bilgi çok fazla olduğu
 için ihtiyaç duyulan işlem miktarı da çok fazla oluyor.
   Bu işlem miktarını düşürmek için yeniden boyutlandırarak veya ölçeklendirerek
   bu kısımdan kurtulmaua çalışıyoruz."""