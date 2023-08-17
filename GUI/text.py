# 导入wxpython
import wx
# 定义一个子类
class MyFrame(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self,parent,id,title="创建staticText 文本",pos=(100,100),size=(600,400))
        panel = wx.Panel(self)
        title = wx.StaticText(panel,label='python之蝉-Tim Peters',pos=(200,0))
        font = wx.Font(wx.FontInfo(12).FaceName("Helvetica").Italic())
        title.SetFont(font)
        wx.StaticText(panel,label='优美胜于丑陋',pos=(0,20))
        wx.StaticText(panel,label='明了胜于晦涩',pos=(0,40))
if __name__ == '__main__':
    # 实例化子类
    app = wx.App()
    frame = MyFrame(parent=None,id=-1)
    frame.Show()
    # 调用主循环方法
    app.MainLoop()