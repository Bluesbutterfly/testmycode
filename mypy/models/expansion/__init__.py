# 应用各种数据增强技术，如随机缩放、剪切、旋转、翻转等，来扩充训练数据集
import torch
import torchvision
import torchvision.transforms as transforms
import torch.optim as optim
import torch.nn as nn
from cnn import CNN
# 定义数据增强的transform
transform = transforms.Compose([
    transforms.RandomHorizontalFlip(),  # 随机水平翻转
    transforms.RandomVerticalFlip(),    # 随机垂直翻转
    transforms.RandomRotation(30),      # 随机旋转（最大旋转角度为30度）
    transforms.RandomResizedCrop(224),  # 随机裁剪和缩放到指定大小（这里假设输入图像尺寸为224x224）
    transforms.ToTensor(),               # 转为Tensor
    transforms.Normalize((0.5,), (0.5,)) # 归一化
])

# 加载训练数据集
train_dataset = torchvision.datasets.MNIST(
    root='./data', 
    train=True, 
    transform=torchvision.transforms.ToTensor(),
    download=True
    )
valid_dataset = torchvision.datasets.MNIST(
    root='./data', 
    train=True, 
    transform=torchvision.transforms.ToTensor(),
    download=True
)  # 自定义的验证数据集
# 定义数据加载器
train_loader = torch.utils.data.DataLoader(train_dataset, batch_size=32, shuffle=True)
valid_dataloader = torch.utils.data.DataLoader(valid_dataset, batch_size=32)
# 定义模型
model = CNN()
# 定义损失函数
criterion = nn.CrossEntropyLoss()

# 定义优化器
optimizer = optim.SGD(model.parameters(), lr=0.001)

# 训练循环
num_epochs = 10
for epoch in range(num_epochs):
    train_loss = 0.0
    valid_loss = 0.0
    # 训练模型
    model.train()
    for images, labels in train_loader:
        optimizer.zero_grad()  # 梯度清零
        
        # 数据增强
        # augmented_images = []
        # for image in images:
        #     augmented_image = transform(image)
        #     augmented_images.append(augmented_image)
        
        # augmented_images = torch.stack(augmented_images)
        
        # 将数据输入模型进行前向传播
        outputs = model(images)
        # 计算损失
        loss = criterion(outputs, labels)
        
        # 反向传播与参数更新
        loss.backward()
        optimizer.step()
        train_loss += loss.item() * images.size(0)
    # 在这里执行其他训练步骤，如记录损失，更新指标等
    # 验证模型
    model.eval()
    with torch.no_grad():
        for images, depths in valid_dataloader:
            outputs = model(images)
            loss = criterion(outputs, depths)
            valid_loss += loss.item() * images.size(0)

    # 计算平均损失值
    train_loss = train_loss / len(train_dataset)
    valid_loss = valid_loss / len(valid_dataset)
    # 打印结果
    print(f"Epoch [{epoch+1}/{num_epochs}], Train Loss: {train_loss}, Valid Loss: {valid_loss}")
    # 保存模型
    if valid_loss < train_loss:
        best_loss = valid_loss
        torch.save(model.state_dict(), "model.pth")
        print("Model Saved!")