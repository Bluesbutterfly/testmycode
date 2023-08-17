# 导入wxpython
import wx
# 定义一个子类
class App(wx.App):
    def OnInit(self):
        frame = wx.Frame(parent=None,title="Hellow wxPython")
        frame.Show()
        return True
if __name__ == '__main__':
    # 实例化子类
    app = App()
    # 调用主循环方法
    app.MainLoop()