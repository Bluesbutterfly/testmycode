"""
使用torch.load函数加载已训练好的模型，并进行后续的推断
"""
import torch

# 定义模型类
class MyModel(torch.nn.Module):
    def __init__(self):
        super(MyModel, self).__init__()
        # 定义模型的结构
        print("模型结构",self)


# 创建一个模型实例
model = MyModel()

# 加载已训练好的权重
checkpoint = torch.load('model.pth')
model.load_state_dict(checkpoint['state_dict'])

# 设置为推断模式
model.eval()

# 进行推断
input_data = torch.tensor(..., dtype=torch.float32)  # 输入数据
output = model(input_data)

# 处理输出
# ...
print(output)