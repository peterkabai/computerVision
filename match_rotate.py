import cv2
import numpy as np

# Read the images from the file
small_image = cv2.imread('part_rotated.png')
large_image = cv2.imread('main.png')

# Run the match template to get the minimums
#method = cv2.TM_SQDIFF_NORMED
method = cv2.TM_CCOEFF_NORMED

rows, cols = small_image.shape[:2]

for degree in range(0,360,45):
    print(degree)
    matrix = cv2.getRotationMatrix2D((cols/2,rows/2),degree,1)
    rotated_image = cv2.warpAffine(small_image, matrix, (cols,rows))
    result = cv2.matchTemplate(rotated_image, large_image, method)
    min_value, _, min_location, _ = cv2.minMaxLoc(result)
    x_loc, y_loc = min_location
    width, height = rotated_image.shape[:2]
    
    top_ten = np.sort(np.ndarray.flatten(result))[::-1][0:10]
    print(top_ten)
    
    color = (0,0,255)
    thickness = 2
    box_loc = x_loc, y_loc
    box_size = x_loc + height, y_loc + width
    cv2.rectangle(large_image, box_loc, box_size, color, thickness)
    
cv2.imwrite('output_rotated.png', large_image)
