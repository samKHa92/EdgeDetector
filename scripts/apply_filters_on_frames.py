import cv2
import numpy as np


def sobel_filter_frame(image_path, index):
    image = cv2.imread(image_path, 0)
    sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0)
    sobel_x_abs = np.uint8(np.absolute(sobel_x))
    sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1)
    sobel_y_abs = np.uint8(np.absolute(sobel_y))
    sobel_xy_combined = cv2.bitwise_or(sobel_y_abs, sobel_x_abs)

    cv2.imwrite('resources/filtered_resources/frames/sobel/horizontal/filtered_frame' + str(index) + '.jpeg',sobel_x_abs)
    cv2.imwrite('resources/filtered_resources/frames/sobel/vertical/filtered_frame' + str(index) + '.jpeg',  sobel_y_abs)
    cv2.imwrite('resources/filtered_resources/frames/sobel/combined/filtered_frame' + str(index) + '.jpeg',sobel_xy_combined)

    return image, sobel_x_abs, sobel_y_abs, sobel_xy_combined


def scharr_filter_frame(image_path, index):
    image = cv2.imread(image_path, 0)
    scharr_x = cv2.Scharr(image, cv2.CV_64F, 1, 0)
    scharr_x_abs = np.uint8(np.absolute(scharr_x))
    scharr_y = cv2.Scharr(image, cv2.CV_64F, 0, 1)
    scharr_y_abs = np.uint8(np.absolute(scharr_y))
    scharr_xy_combined = cv2.bitwise_or(scharr_y_abs, scharr_x_abs)

    cv2.imwrite('resources/filtered_resources/frames/scharr/horizontal/filtered_frame' + str(index) + '.jpeg',scharr_x_abs)
    cv2.imwrite('resources/filtered_resources/frames/scharr/vertical/filtered_frame' + str(index) + '.jpeg', scharr_y_abs)
    cv2.imwrite('resources/filtered_resources/frames/scharr/combined/filtered_frame' + str(index) + '.jpeg',scharr_xy_combined)

    return image, scharr_x_abs, scharr_y_abs, scharr_xy_combined
