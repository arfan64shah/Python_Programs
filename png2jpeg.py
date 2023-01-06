
# import matplotlib.pyplot as plt
# import cv2

# # Loading .png image
# png_img = cv2.imread('C:/Users/arfan.shah/Desktop/Mydocs/arfan.png')

# # converting to jpg file
# #saving the jpg file

# plt.imshow(png_img)

# cv2.imwrite('C:/Users/arfan.shah/Desktop/Mydocs/arfan.jpeg', png_img, [int(cv2.IMWRITE_JPEG_QUALITY), 100])

# Import the library OpenCV
import cv2

# Import the image
file_name = "C:/Users/arfan.shah/Desktop/Mydocs/arfan.jpeg"

# Read the image
src = cv2.imread(file_name, 1)

# Convert image to image gray
tmp = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

# Applying thresholding technique
_, alpha = cv2.threshold(tmp, 0, 255, cv2.THRESH_BINARY)

# Using cv2.split() to split channels
# of coloured image
b, g, r = cv2.split(src)

# Making list of Red, Green, Blue
# Channels and alpha
rgba = [b, g, r, alpha]

# Using cv2.merge() to merge rgba
# into a coloured/multi-channeled image
dst = cv2.merge(rgba, 4)

# Writing and saving to a new image
cv2.imwrite("C:/Users/arfan.shah/Desktop/Mydocs/arfanshah.jpeg", dst)

