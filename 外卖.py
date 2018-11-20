# coding:utf8
import wx
#导入wxpyhton，pyhton自带的GUI库
# #import wx.xrc
import pymysql #用于操作数据库
import sys
reload(sys)
sys.setdefaultencoding('utf8')
###########################################################################
## Class MyFrame1 ####################
# ####################################
# ################### #建一个窗口类MyFrame1继承wx.Frame
class MyFrame1(wx.Frame):
    def __init__(self, parent):
        #Wx.Frame (parent, id, title, pos, size, style, name)
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"广油计科17-1电力公司收费管理系统管理系统", pos=wx.DefaultPosition, size=wx.Size(610, 400),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)
        self.Center() #居中显示 # 小构件，如按钮，文本框等被放置在面板窗口。 wx.Panel类通常是被放在一个wxFrame对象中。这个类也继承自wxWindow类。

        self.m_panel1 = wx.Panel(self)
        # 标签，一行或多行的只读文本， Wx.StaticText(parent, id, label, position, size, style)
        # self.m_staticText1 = wx.StaticText(self.m_panel1, wx.ID_ANY, u"客户：", (20, 20))
        self.m_button1 = wx.Button(self.m_panel1, wx.ID_ANY, u"操作客户表", (130, 20), wx.DefaultSize, style=wx.BORDER_MASK)
        self.m_button2 = wx.Button(self.m_panel1, wx.ID_ANY, u"操作费用管理表", (250, 20), wx.DefaultSize, style=wx.BORDER_MASK)
        self.m_button3 = wx.Button(self.m_panel1, wx.ID_ANY, u"操作收费等级表", (370, 20), wx.DefaultSize, style=wx.BORDER_MASK)
        # self.m_staticText2 = wx.StaticText(self.m_panel1, wx.ID_ANY, u"用电类型：", (20, 90))
        self.m_button4 = wx.Button(self.m_panel1, wx.ID_ANY, u"操作电类型表", (130, 90), wx.DefaultSize,
                                   style=wx.BORDER_MASK)
        self.m_button5 = wx.Button(self.m_panel1, wx.ID_ANY, u"操作结余登记表", (250, 90), wx.DefaultSize,
                                   style=wx.BORDER_MASK)
        # self.m_button6 = wx.Button(self.m_panel1, wx.ID_ANY, u"解雇派送员", (370, 90), wx.DefaultSize,
        #                            style=wx.BORDER_MASK)
        # self.m_staticText3 = wx.StaticText(self.m_panel1, wx.ID_ANY, u"员工：", (20, 160))
        self.m_button6 = wx.Button(self.m_panel1, wx.ID_ANY, u"操作员工表", (370, 90), wx.DefaultSize,
                                   style=wx.BORDER_MASK)
        # self.m_button8 = wx.Button(self.m_panel1, wx.ID_ANY, u"聘请客服人员", (250, 160), wx.DefaultSize,
        #                            style=wx.BORDER_MASK)
        # self.m_button9 = wx.Button(self.m_panel1, wx.ID_ANY, u"解雇客服人员", (370, 160), wx.DefaultSize,
        #                            style=wx.BORDER_MASK)
        # self.m_staticText4 = wx.StaticText(self.m_panel1, wx.ID_ANY, u"关于用电信息：", (20, 230))
        self.m_button7 = wx.Button(self.m_panel1, wx.ID_ANY, u"操作用电信息表", (130, 160), wx.DefaultSize,
                                    style=wx.BORDER_MASK)
        # self.m_button11 = wx.Button(self.m_panel1, wx.ID_ANY, u"学生订餐", (250, 230), wx.DefaultSize,
        #                             style=wx.BORDER_MASK)
        # self.m_button12 = wx.Button(self.m_panel1, wx.ID_ANY, u"取消订单", (370, 230), wx.DefaultSize,
        #                             style=wx.BORDER_MASK)
        # self.m_button13 = wx.Button(self.m_panel1, wx.ID_ANY, u"修改订单", (490, 230), wx.DefaultSize,
        #                             style=wx.BORDER_MASK)
        # self.m_staticText5 = wx.StaticText(self.m_panel1, wx.ID_ANY, u"关于物流：", (20, 300))
        # self.m_button14 = wx.Button(self.m_panel1, wx.ID_ANY, u"配送信息", (250, 160), wx.DefaultSize,
        #                             style=wx.BORDER_MASK)
        # self.m_button15 = wx.Button(self.m_panel1, wx.ID_ANY, u"安排配送", (250, 300), wx.DefaultSize,
        #                             style=wx.BORDER_MASK)
        # self.m_button16 = wx.Button(self.m_panel1, wx.ID_ANY, u"取消配送", (370, 300), wx.DefaultSize,
        #                             style=wx.BORDER_MASK)

if __name__ == "__main__":
    app = wx.App()
    MyFrame1(None).Show()
    app.MainLoop()

