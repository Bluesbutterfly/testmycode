# 导入wxpython
import wx
# 定义一个子类
class MyFrame(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self,parent,id,title="创建frame",pos=(100,100),size=(300,300))
if __name__ == '__main__':
    # 实例化子类
    app = wx.App()
    frame = MyFrame(parent=None,id=-1)
    frame.Show()
    # 调用主循环方法
    app.MainLoop()