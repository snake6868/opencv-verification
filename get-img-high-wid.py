from PIL import Image
import cv2 as cv


def resize_image(image, scale_percent):
    width = int(image.shape[1] * scale_percent / 100)
    height = int(image.shape[0] * scale_percent / 100)
    dim = (width, height)
    resized = cv.resize(image, dim, interpolation=cv.INTER_AREA)
    return resized


if __name__ == '__main__':
    # 打开图像文件
    # image = Image.open("./ios_block_ori2.png")
    # image = Image.open("./result_cropped.jpg")
    # 获取图像的宽度和高度
    img1 = cv.imread('./img/test_0.png')
    scaled_image = resize_image(img1, 100)
    # 获取缩放后图像的宽度和高度
    scaled_width = scaled_image.shape[1]
    scaled_height = scaled_image.shape[0]

    print("缩放后图像的宽度：", scaled_width)
    print("缩放后图像的高度：", scaled_height)

    # # 打印图像的像素尺寸
    # print("图像宽度:", width)
    # print("图像高度:", height)
