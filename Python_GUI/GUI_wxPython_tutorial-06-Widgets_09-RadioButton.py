#!/home/jun_jiang/.local/bin/python3
#coding:utf-8

"""
ZetCode wxPython tutorial

In this code example, we create a static line.

author: Jan Bodnar
website: www.zetcode.com
last modified: July 2020
"""
import wx


class Example(wx.Frame):

    def __init__(self, *args, **kw):
        super(Example, self).__init__(*args, **kw)

        self.InitUI()

    def InitUI(self):

        pnl = wx.Panel(self)

        self.rb1 = wx.RadioButton(pnl, label='Value A', pos=(10, 10),
            style=wx.RB_GROUP)
        self.rb2 = wx.RadioButton(pnl, label='Value B', pos=(10, 30))
        self.rb3 = wx.RadioButton(pnl, label='Value C', pos=(10, 50))

        self.rb1.Bind(wx.EVT_RADIOBUTTON, self.SetVal)
        self.rb2.Bind(wx.EVT_RADIOBUTTON, self.SetVal)
        self.rb3.Bind(wx.EVT_RADIOBUTTON, self.SetVal)

        self.sb = self.CreateStatusBar(3)

        self.sb.SetStatusText("True", 0)
        self.sb.SetStatusText("False", 1)
        self.sb.SetStatusText("False", 2)

        self.SetSize((210, 210))
        self.SetTitle('wx.RadioButton')
        self.Centre()
        self.Show(True)

    def SetVal(self, e):

        state1 = str(self.rb1.GetValue())
        state2 = str(self.rb2.GetValue())
        state3 = str(self.rb3.GetValue())

        self.sb.SetStatusText(state1, 0)
        self.sb.SetStatusText(state2, 1)
        self.sb.SetStatusText(state3, 2)

def main():

    ex = wx.App()
    Example(None)
    ex.MainLoop()

if __name__ == '__main__':
    main()

