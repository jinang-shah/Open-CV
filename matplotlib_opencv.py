import cv2 as cv
import matplotlib.pyplot as plt

img=cv.imread('football.jpg')    # read img in -> RBG form
cv.imshow('IMAGE',img)

img=cv.cvtColor(img, cv.COLOR_BGR2RGB)

plt.imshow(img)     # read img in -> BGR form
plt.show()

cv.waitKey(0)
cv.destroyAllWindows()