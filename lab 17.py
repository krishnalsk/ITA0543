import cv2
import numpy as np

# Read original image
original = cv2.imread("C:/Users/mbala/OneDrive/Pictures/Screenshots 1/Screenshots/Screenshot 2026-03-03 143552.png")

# Read watermark image
watermark = cv2.imread("C:/Users/mbala/OneDrive/Pictures/Screenshots 1/Screenshots/Screenshot 2026-03-03 143601.png")

# Resize watermark to match original image size
watermark = cv2.resize(watermark, (original.shape[1], original.shape[0]))

# Set transparency level
alpha = 0.7   # original image weight
beta = 0.3    # watermark weight

# Blend images
watermarked_image = cv2.addWeighted(original, alpha, watermark, beta, 0)

# Display images
cv2.imshow("Original Image", original)
cv2.imshow("Watermarked Image", watermarked_image)

# Save output image
cv2.imwrite("watermarked_output.jpg", watermarked_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
