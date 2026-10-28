import cv2

img = cv2.imread("input.jpg")

# Check whether the image is loaded
if img is None:
    print("Image not found!")
else:
    # Convert color image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Display original and grayscale images
    cv2.imshow("Original Image", img)
    cv2.imshow("Grayscale Image", gray)

    # Save the grayscale image
    cv2.imwrite("output.jpg", gray)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

