# 导入wxpython
import wx
# 定义一个子类
class MyFrame(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self,parent,id,title="创建TextCtrl类",pos=(100,100),size=(800,600))
        panel = wx.Panel(self)
        self.title = wx.StaticText(panel,label='请输入用户名和密码')
        font = wx.Font(wx.FontInfo(12).FaceName("Helvetica").Italic())
        self.title.SetFont(font)
        self.label_user = wx.StaticText(panel,label='用户名')
        self.text_user = wx.TextCtrl(panel,size=(235,25),style=wx.TE_LEFT)
        self.label_password = wx.StaticText(panel,label='密   码')
        self.text_password = wx.TextCtrl(panel,size=(235,25),style=wx.TE_PASSWORD)
        """创建确定和取消按钮"""
        self.bt_confirm = wx.Button(panel,label="确定")
        self.bt_confirm.Bind(wx.EVT_BUTTON,self.OnclickSubmit)
        self.bt_cancle= wx.Button(panel,label="取消")
        self.bt_cancle.Bind(wx.EVT_BUTTON,self.OnclickReset)
        # 使用布局进行适配
        hsizer_user = wx.BoxSizer(wx.HORIZONTAL)
        # vsizer = wx.BoxSizer(wx.VERTICAL)
        hsizer_user.Add(self.label_user,proportion=0,flag=wx.ALL,border=5)
        hsizer_user.Add(self.text_user,proportion=1,flag=wx.ALL,border=5)
        hsizer_pwd = wx.BoxSizer(wx.HORIZONTAL)
        hsizer_pwd.Add(self.label_password,proportion=0,flag=wx.ALL,border=5)
        hsizer_pwd.Add(self.text_password,proportion=1,flag=wx.ALL,border=5)
        hsizer_button = wx.BoxSizer(wx.HORIZONTAL)
        hsizer_button.Add(self.bt_confirm,proportion=0,flag=wx.ALL,border=5)
        hsizer_button.Add(self.bt_cancle,proportion=0,flag=wx.ALL,border=5)
        vsizer_all = wx.BoxSizer(wx.VERTICAL)
        vsizer_all.Add(self.title,proportion=0,flag=wx.BOTTOM | wx.TOP | wx.ALIGN_CENTER,border=15)
        vsizer_all.Add(hsizer_user,proportion=0,flag=wx.EXPAND | wx.LEFT | wx.RIGHT,border=45)
        vsizer_all.Add(hsizer_pwd,proportion=0,flag=wx.EXPAND | wx.LEFT | wx.RIGHT,border=45)
        vsizer_all.Add(hsizer_button,proportion=0,flag=wx.ALIGN_CENTER | wx.TOP,border=15)
        # vsizer.Add(self.title,proportion=0,flag=wx.BOTTOM | wx.TOP | wx.ALIGN_CENTER,border=15)
        panel.SetSizer(vsizer_all)
    def OnclickSubmit(self,event):
      message = ""
      username = self.text_user.GetValue()
      password = self.text_password.GetValue()
      if username == "" or password == "":
        message = "用户名或密码不能为空"
      elif username == "mr" and password == "mrsoft":
        message = "登录成功"
      else:
        message= "用户名和密码不匹配"
      wx.MessageBox(message)
    def OnclickReset(self,event):
       self.text_user.SetValue("")
       self.text_password.SetValue("")
if __name__ == '__main__':
    # 实例化子类
    app = wx.App()
    frame = MyFrame(parent=None,id=-1)
    frame.Show()
    # 调用主循环方法
    app.MainLoop()