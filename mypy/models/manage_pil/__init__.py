"""
图像处理
使用PIL库各种图像处理操作
图像校正、去噪、调整亮度和对比度
"""
from PIL import Image, ImageEnhance, ImageFilter
import os

# 图像校正
def straighten_image(image):
    # 使用PIL的旋转函数寻找最佳角度进行图像校正
    image = image.rotate(45)  # angle为需要旋转的角度
    return image

# 去噪
def denoise_image(image):
    # 使用PIL的滤波函数进行图像去噪
    image = image.filter(ImageFilter.SMOOTH)
    return image

# 调整亮度和对比度
def adjust_brightness_contrast(image, brightness_factor, contrast_factor):
    # 使用PIL的增强函数调整图像亮度和对比度
    enhancer = ImageEnhance.Brightness(image)
    image = enhancer.enhance(brightness_factor)

    enhancer = ImageEnhance.Contrast(image)
    image = enhancer.enhance(contrast_factor)

    return image

# 获取待处理的图像文件列表
directory = 'models/loadimg/dataset'  # 图像文件所在的目录
output_directory = 'models/expansion/data'  # 处理后图像保存的目录

image_files = [f for f in os.listdir(directory) if f.endswith('.jpg') or f.endswith('.png')]

# 遍历每个图像文件进行批处理
for image_file in image_files:
    # 打开原始图像
    image_path = os.path.join(directory, image_file)
    image = Image.open(image_path)

    # 图像校正
    image = straighten_image(image)

    # 去噪
    image = denoise_image(image)

    # 调整亮度和对比度
    brightness_factor = 1.2  # 调整亮度的系数（大于1增加亮度，小于1降低亮度）
    contrast_factor = 1.2  # 调整对比度的系数（大于1增加对比度，小于1降低对比度）

    image = adjust_brightness_contrast(image, brightness_factor, contrast_factor)

    # 保存处理后的图像
    output_image_path = os.path.join(output_directory, image_file)
    
    image.save(output_image_path)
