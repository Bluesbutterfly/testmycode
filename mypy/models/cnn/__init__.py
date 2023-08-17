# 构建CNN模型
import torch
import torch.nn as nn

# 定义CNN模型
class CNN(nn.Module):
    def __init__(self):
        super(CNN, self).__init__()
        
        # 定义卷积层
        # 通道数为1，输出通道数为16，卷积核大小为3x3，步幅为1，填充为1
        self.conv1 = nn.Conv2d(in_channels=1, out_channels=16, kernel_size=3, stride=1, padding=1)
        self.relu = nn.ReLU()
        # 激活函数使用ReLU，池化层使用nn.MaxPool2d函数定义，池化核大小为2x2，步幅为2
        self.maxpool = nn.MaxPool2d(kernel_size=2, stride=2)
        
        # 定义全连接层
        self.fc1 = nn.Linear(in_features=16 * 14 * 14, out_features=10)  # 假设输入为14x14的图像，输出为10个类别
        
    def forward(self, x):
        # 前向传播过程
        x = self.conv1(x)
        x = self.relu(x)
        x = self.maxpool(x)
        
        # 将卷积层的输出展平为一维向量
        x = x.view(x.size(0), -1)
        
        # 进入全连接层
        x = self.fc1(x)
        
        return x

# 创建模型的实例
model = CNN()
