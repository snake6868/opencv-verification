# encoding:utf-8
import cv2 as cv
import numpy as np


def get_pos(image):
    # get pos ####################################################################################################
    print("start")
    cv.imshow('cropped_image', image)
    blurred = cv.GaussianBlur(image, (9, 9), 0)
    canny = cv.Canny(blurred, 50, 100)
    contours, hierarchy = cv.findContours(canny, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    for i, contour in enumerate(contours):
        print('mid')
        M = cv.moments(contour)
        if M['m00'] == 0:
            cx = cy = 0
            print("11111111111111")
        else:
            cx, cy = M['m10'] / M['m00'], M['m01'] / M['m00']
            print("22222222222222")
        print("33333333333333")
        if cx < 200:
            continue
        x, y, w, h = cv.boundingRect(contour)  # 外接矩形
        print(w, h)
        if 100 < w < 400 and h > 100:
            cv.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv.imshow('result_image', image)
            print("end")
            print("边框的横坐标位置为：" + str(x))
            print("边框的宽度为：" + str(w))
            return x
    return 0


def crop_image(image):
    # 定义裁剪区域的坐标
    x = 70  # 起始横坐标
    y = 500  # 起始纵坐标
    width = 400  # 裁剪宽度
    height = 300  # 裁剪高度

    # 裁剪图像
    cropped_image = image[y:y + height, x:x + width]

    # # 显示原始图像和裁剪后的图像
    cv.imshow("Original Image", image)
    # cv.imshow("Cropped Image", cropped_image)

    # 保存裁剪后的图像
    cv.imwrite("result_cropped.jpg", cropped_image)

    # cv.waitKey(0)
    # cv.destroyAllWindows()


def resize_image(image, scale_percent):
    width = int(image.shape[1] * scale_percent / 100)
    height = int(image.shape[0] * scale_percent / 100)
    dim = (width, height)
    resized = cv.resize(image, dim, interpolation=cv.INTER_AREA)
    return resized


if __name__ == '__main__':
    # img0 = cv.imread('android_screenshot.jpg')
    # crop_image(img0)
    img1 = cv.imread('./img/test_2.png')
    # scaled_image = resize_image(img1, 45)
    # img1 = cv.imread('./result_cropped.jpg')
    get_pos(img1)
    cv.waitKey(0)
    cv.destroyAllWindows()
