"""Görüntüdeki detayları azaltmak veya gürültüyü azaltmak gibi birçok farklı amaca hizmet eden çeşitli teknikler vardır. Bulanıklaştırma (blurring),
 bu tekniklerden biridir ve genellikle aşağıdaki amaçlarla kullanılır:"""

import cv2 as cv

img = cv.imread('Photos/cats.jpg')
cv.imshow('img',img)

#Averaging
"""
Bulanıklaştırma gerçekleştirirken öncelikle bir pencere  tanımlamalıyız.
Çekirdek penceresindeki merkez piksel çevresindeki piksel yoğunluğunun ortalamasını alacak.
Bu işlem bitince pencere sağa ve aşağıya kayarak işlemi tekrar eder.

"""

average = cv.blur(img, (8,8)) # Çekirdek boyutu arttıkca blurlama artar
cv.imshow('Average Blur',average)

# Gaussian Blur
gauss = cv.GaussianBlur(img, (7, 7), 0)# 0 filtrenin standart sapması
cv.imshow('gauss', gauss)

# Median Blur
median = cv.medianBlur(img, 3)# 3 çekirdeğin boyutu
cv.imshow('median', median)

# Bilateral
bilateral = cv.bilateralFilter(img,5,5,15)
cv.imshow('bilateral',bilateral)
cv.waitKey(0)
"""Bilateral filtreleme, bir görüntü üzerinde gürültüyü azaltmak 
ve aynı zamanda görüntünün kenarlarını korumak için etkili bir yöntemdir.

filtered_image = cv.bilateralFilter(src, d, sigma_color, sigma_space)
src: Bilateral filtrelemenin uygulanacağı giriş görüntüsüdür.
d: Filtreleme işlemindeki piksel komşuluklarına dahil edilen bir çap (diameter) parametresidir. 
Daha büyük bir d değeri, daha geniş bir çevre içindeki piksellerin dikkate alınmasını sağlar.

sigma_color: Renk benzerliği (color similarity) için bir standart sapma değeridir. 
Daha büyük bir sigma_color, renk benzerliğinin daha fazla uzak renkler için de geçerli olmasını sağlar.

sigma_space: Uzamsal benzerlik (spatial similarity) için bir standart sapma değeridir.
 Daha büyük bir sigma_space, uzamsal benzerliğin daha fazla uzak pikseller için de geçerli olmasını sağlar.

Bilateral filtreleme, gürültüyü azaltırken kenarları korurken, diğer basit bulanıklaştırma yöntemlerinden daha karmaşıktır. 
Bu nedenle daha yavaş çalışabilir, ancak daha iyi sonuçlar elde etmenizi sağlar.


"""