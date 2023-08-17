import torchvision.transforms as transforms
from torchvision.datasets import ImageFolder

# 数据集路径
data_dir = "models/loadimg/dataset"


# 数据预处理
transform = transforms.Compose([
    transforms.Resize((224, 224)),  # 调整图像大小
    transforms.ToTensor(),  # 转换为张量
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])  # 标准化
])

# 加载数据集
dataset = ImageFolder(root=data_dir, transform=transform)

# 数据集类别名字列表
class_names = dataset.classes

# 数据集大小
dataset_size = len(dataset)

# 获取单个样本
image, label = dataset[0]
print(image)