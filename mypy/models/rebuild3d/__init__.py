# 三维重建
# 首先，使用cv2.stereoCalibrate函数对相机进行标定，获取相机的内部参数（相机矩阵、畸变系数）以及外部参数（旋转矩阵、平移向量）
# 其次，使用cv2.triangulatePoints函数对双目图像进行三角化
# 最后，使用cv2.reprojectImageTo3D函数将投影的深度图转换为空间点云
import cv2
import numpy as np
# 读取图片
imageSize = (640, 480)
objectPoints = np.zeros((6 * 7, 3), np.float32)
objectPoints[:, :2] = np.mgrid[0:7, 0:6].T.reshape(-1, 2)
imagePoints1 = np.random.randint(0, 480, (6, 7, 2), np.float32
                                 )
imagePoints2 = np.random.randint(0, 480, (6, 7, 2), np.float3
                                 )
# 相机参数
cameraMatrix1 = np.random.randint(0, 100, (3, 3), np.float32)
cameraMatrix2 = np.random.randint(0, 100, (3, 3), np.float32)
distCoeffs1 = np.random.randint(0, 100, (5, 1), np.float32
                                )
distCoeffs2 = np.random.randint(0, 100, (5, 1), np.float32
                                )
# 计算相机参数
R = np.random.randint(0, 100, (3, 3), np.float32)
T = np.random.randint(0, 100, (3, 1), np.float32)
# 计算相机参数
R1, R2, P1, P2, Q, roi1, roi2 = cv2.stereoCalibrate(
    objectPoints, imagePoints1, imagePoints2, imageSize, cameraMatrix1,
    distCoeffs1, cameraMatrix2, distCoeffs2, 
    None, None, None, None, None, None, None, None, None, None, None, 
    None
 )
# 计算立体矫正参数
R1, R2, P1, P2, Q, roi1, roi2 = cv2.stereoRectify(
    cameraMatrix1, distCoeffs1, cameraMatrix2, distCoeffs2, 
    imageSize, R, T,
    flags=cv2.CALIB_ZERO_DISPARITY, alpha=0)

_, cameraMatrix1, distCoeffs1, cameraMatrix2, distCoeffs2, R, T, _, _ = cv2.stereoCalibrate(objectPoints, imagePoints1, imagePoints2, imageSize, cameraMatrix1, distCoeffs1, cameraMatrix2, distCoeffs2)
# 使用cv2.findFundamentalMat函数计算基础矩阵，用于描述不同视角下的特征点对之间的关系
fundamental = cv2.findFundamentalMat(imagePoints1, imagePoints2, cv2.FM_LMEDS)
# 使用cv2.findEssentialMat函数计算本质矩阵，用于描述两个相机之间的相对运动
essential = cv2.findEssentialMat(imagePoints1, imagePoints2, cameraMatrix1, cv2.RANSAC,
                                 threshold=0.001)
# 使用cv2.triangulatePoints函数计算空间点
points4D = cv2.triangulatePoints(P1, P2, imagePoints1, imagePoints2)
points4D = points4D.T
