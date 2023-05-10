import cv2
image = cv2.imread('path/to/bugsbunny.jpg')

blue, green, red = cv2.split(image)

cv2.imshow('Blue Channel', blue)
cv2.imshow('Green Channel', green)
cv2.imshow('Red Channel', red)

cv2.waitKey(0)

green[:] = 0
image = cv2.merge((blue, green, red))

cv2.imshow('Edited Image', image)
cv2.waitKey(0)
