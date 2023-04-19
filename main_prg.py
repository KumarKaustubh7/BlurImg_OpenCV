

import cv2

img = cv2.imread('img.jpg')

# Averaging
avg = cv2.blur(img,(10,10))
   
cv2.imshow('Averaging',avg)
cv2.waitKey(0)
  
# Gaussian Blurring
gaus = cv2.GaussianBlur(img, (5,5),0) 
cv2.imshow('Gaussian Blurring', gaus)
cv2.waitKey(0)
  
# Median blurring
med = cv2.medianBlur(img,5)
cv2.imshow('Media Blurring', med)
cv2.waitKey(0)
  
# Bilateral Filtering
bFil = cv2.bilateralFilter(img,9,75,75)
cv2.imshow('Bilateral Filtering', bFil)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[ ]:




