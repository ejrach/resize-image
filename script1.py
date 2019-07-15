import cv2

# import the image, specified with options to 0=grayscale intensity values
img = cv2.imread("galaxy.jpg",0)

# import the image, specified with options to 1=RGB
#img = cv2.imread("galaxy.jpg",1)


# Python stores the image as a numpy array
print(type(img))

# Prints the matrix of the numpy array, like [14 18 14 ... 20 15 16]
# where the numbers represent the intensity from lightest (0) to darkest (100)
print(img)

# prints the # of rows and columns (number of pixels across, by the number of pixels down)
print(img.shape)

# prints the number of dimensions
print(img.ndim)

# show a window of the image which displays on your screen
resized_image = cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2)))
cv2.imshow("Galaxy",resized_image)
cv2.imwrite("Galaxy_resized.jpg",resized_image)

# 0 specifies that a button press will close the window
# something like 2000 specifies that in 2000 ms, the window will close automatically
cv2.waitKey(0)
cv2.destroyAllWindows()