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

        self.Bind(wx.EVT_PAINT, self.OnPaint)

        self.SetTitle("Gradients")
        self.Centre()

    def OnPaint(self, event):

        dc = wx.PaintDC(self)

        dc.GradientFillLinear((20, 20, 180, 40), '#ffec00', '#000000', wx.NORTH)
        dc.GradientFillLinear((20, 80, 180, 40), '#ffec00', '#000000', wx.SOUTH)
        dc.GradientFillLinear((20, 140, 180, 40), '#ffec00', '#000000', wx.EAST)
        dc.GradientFillLinear((20, 200, 180, 40), '#ffec00', '#000000', wx.WEST)


def main():

    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
