import cv2 as cv
"""
Matematiksel açıdan kontürler ve kenarlar farklı şeylerdir.
Konturlar, şekil analizine ve nesne algılamaya başladığınızda kullanışlı araçlardır.

"""
img = cv.imread('Photos/cats.jpg')

cv.imshow('Cats',img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

#bulanıklaştırarak contours sayısını bulmaya çalışalım
blur = cv.GaussianBlur(gray,(5,5), cv.BORDER_DEFAULT)
cv.imshow('blur',blur)

canny = cv.Canny(img,125,175) # burda eşik değerlerini vererek gerçekleştiriyoruz.
cv.imshow('Canny Edges',canny)

contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)}: counters found!')
#cv.RETR_EXTERNAL kontur alma yöntemi, yalnızca en dışdaki (en büyük) konturları bulmanızı sağlar.
"""cv.CHAIN_APPROX_NONE: Kontur noktalarının depolanma yöntemi olarak kullanılan bir sabit. Bu değer, konturun tüm noktalarını saklamak için kullanılır,
 yani konturun her noktası ayrı ayrı listelenir.
"""
#######
"""
cv.RETR_LIST: Kontur alma yöntemi olarak kullanılan bir sabit. Bu yöntem, görüntüdeki tüm konturları elde eder, ancak hiyerarşi bilgisi sağlamaz. Bu demektir ki,
iç içe geçmiş konturları tespit edebilirsiniz ancak hangi konturun hangi konturun altında olduğu bilgisine sahip olmazsınız.
"""

"""
Eğer cv.RETR_TREE yöntemi ile cv.findContours() fonksiyonunu çağırsaydınız, her bir konturun ana konturu (ebeveyn), 
alt konturları (çocuklar) ve kardeş konturları (aynı düzeydeki diğer konturlar) hakkında bilgi sağlayan bir hiyerarşik yapı elde edersiniz
"""
# cv.CHAIN_APPROX_SIMPLE: Bu yöntem, konturun şeklini yaklaşık olarak tanımlamak için gereken minimum noktaları saklar. Bu da daha az bellek kullanımı anlamına gelir. 

canny2 = cv.Canny(blur,125,175) # blurlu deneme
cv.imshow('Canny Edges',canny2)

contours2, hierarchies2 = cv.findContours(canny2, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours2)}: counters found!')
cv.waitKey(0)