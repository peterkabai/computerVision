import cv2

# Read the images from the file
image = cv2.imread('puzzle/p1.png')

fgbg = cv2.createBackgroundSubtractorMOG2()
image1 = fgbg.apply(image)
#image = cv2.equalizeHist(image)
#image = cv2.bitwise_not(image)

cv2.imwrite('p1_mask2.png', image1)

