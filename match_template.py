import cv2

# Read the images from the file
small_image = cv2.imread('part.png')
large_image = cv2.imread('main.png')

mask = cv2.imread('puzzle/p1_mask.jpg')


# Run the match template to get the minimums
method = cv2.TM_SQDIFF_NORMED
result = cv2.matchTemplate(small_image, large_image, method, mask)
min_value, _, min_location, _ = cv2.minMaxLoc(result)



# Get the location from the minimum
x_loc, y_loc = min_location

# Get the size of the template image
width, height = small_image.shape[:2]

# Draw the rectangle on the original image
color = (0,0,255)
thickness = 2
box_loc = x_loc, y_loc
box_size = x_loc + width, y_loc + height
cv2.rectangle(large_image, box_loc, box_size, color, thickness)

# Save the image
cv2.imwrite('output.png', large_image)
