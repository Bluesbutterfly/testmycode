# 特征提取
import cv2

# 创建SIFT或ORB对象
feature_detector = cv2.xfeatures2d.SIFT_create()  # 或者 cv2.ORB_create()

# 批量处理图片
image_files = ['models/expansion/data/southeast.jpg']  # 图片文件列表
keypoints_list = []  # 存储特征点列表
descriptors_list = []  # 存储特征描述符列表

for file in image_files:
    # 读取图像
    image = cv2.imread(file, cv2.IMREAD_GRAYSCALE)

    # 检测特征点和计算描述符
    keypoints, descriptors = feature_detector.detectAndCompute(image, None)

    # 添加到列表
    keypoints_list.append(keypoints)
    descriptors_list.append(descriptors)

    # 可以在这里进行进一步的处理或保存特征点和描述符

# 打印每张图片提取的特征点数量
for i, keypoints in enumerate(keypoints_list):
    print("图像{}中提取的特征点数量: {}".format(i+1, len(keypoints)))