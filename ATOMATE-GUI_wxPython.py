#!/home/jun_jiang/.local/bin/python3
#coding:utf-8

from pathlib import Path
import os
import wx

class MyTextDropTarget(wx.TextDropTarget):

    def __init__(self, object):

        wx.TextDropTarget.__init__(self)
        self.object = object

    def OnDropText(self, x, y, data):

        self.object.InsertItem(0, data)
        return True


class Example(wx.Frame):

    def __init__(self, parent, title, *args, **kw):
#        super(Example, self).__init__(parent, title=title)
        super(Example, self).__init__(parent, title=title,
            size=(350, 300))

        self.InitUI()
        self.Centre()

    def InitUI(self):

        self.panel = wx.Panel(self)

        font = wx.SystemSettings.GetFont(wx.SYS_SYSTEM_FONT)

        font.SetPointSize(9)

        vbox = wx.BoxSizer(wx.VERTICAL)

        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        st1 = wx.StaticText(self.panel, label='Load From File')
        st1.SetFont(font)
        hbox1.Add(st1, flag=wx.RIGHT, border=8)
        tc = wx.TextCtrl(self.panel)
        hbox1.Add(tc, proportion=1)
        btn0 = wx.Button(self.panel, label='Open', size=(50, 30))
        hbox1.Add(btn0, flag=wx.LEFT, border=8)
        btn0.Bind(wx.EVT_BUTTON,  self.LoadFiles)
        vbox.Add(hbox1, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)

        vbox.Add((-1, 10))

        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        st2 = wx.StaticText(self.panel, label='Matching Classes')
        st2.SetFont(font)
        hbox2.Add(st2)
        vbox.Add(hbox2, flag=wx.LEFT | wx.TOP, border=10)

        vbox.Add((-1, 10))

        hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        tc2 = wx.TextCtrl(self.panel, style=wx.TE_MULTILINE)
        hbox3.Add(tc2, proportion=1, flag=wx.EXPAND)
        vbox.Add(hbox3, proportion=1, flag=wx.LEFT|wx.RIGHT|wx.EXPAND,
            border=10)

        vbox.Add((-1, 25))

        hbox4 = wx.BoxSizer(wx.HORIZONTAL)
        cb1 = wx.CheckBox(self.panel, label='Case Sensitive')
        cb1.SetFont(font)
        hbox4.Add(cb1)
        cb2 = wx.CheckBox(self.panel, label='Nested Classes')
        cb2.SetFont(font)
        hbox4.Add(cb2, flag=wx.LEFT, border=10)
        cb3 = wx.CheckBox(self.panel, label='Non-Project classes')
        cb3.SetFont(font)
        hbox4.Add(cb3, flag=wx.LEFT, border=10)
        vbox.Add(hbox4, flag=wx.LEFT, border=10)

        vbox.Add((-1, 25))

        hbox5 = wx.BoxSizer(wx.HORIZONTAL)
        btn1 = wx.Button(self.panel, label='Ok', size=(70, 30))
        hbox5.Add(btn1)
        btn2 = wx.Button(self.panel, label='Close', size=(70, 30))
        hbox5.Add(btn2)

#        exitButton = wx.Button(self.panel, wx.ID_ANY, 'Exit', size=(70, 30))
        btn3 = wx.Button(self.panel, wx.ID_ANY, 'Exit', size=(70, 30))

        self.Bind(wx.EVT_BUTTON,  self.OnExit, id=btn3.GetId())
#        self.SetTitle("Automatic ids")

        hbox5.Add(btn3, flag=wx.LEFT|wx.BOTTOM, border=5)
        vbox.Add(hbox5, flag=wx.ALIGN_RIGHT|wx.RIGHT, border=10)
        self.panel.SetSizer(vbox)


#        pnl = wx.Panel(self)
#        exitButton = wx.Button(self.panel, wx.ID_ANY, 'Exit', size=(70, 30))
#
#        self.Bind(wx.EVT_BUTTON,  self.OnExit, id=exitButton.GetId())
#
#        self.SetTitle("Automatic ids")
#

# ***** BackgroundColour *********
#        self.panel.SetBackgroundColour("gray")
#        self.LoadImages()

#        self.mincol.SetPosition((20, 20))
#        self.bardejov.SetPosition((40, 160))
#        self.rotunda.SetPosition((170, 50))
#        self.rotunda.SetPosition((20, 20))

        self.Centre()

    def LoadFiles(self, event):

        splitter1 = wx.SplitterWindow(self, style=wx.SP_3D)
        splitter2 = wx.SplitterWindow(splitter1, style=wx.SP_3D)

        home_dir = str(Path.home())

        self.dirWid = wx.GenericDirCtrl(splitter1, dir=home_dir, 
                style=wx.DIRCTRL_DIR_ONLY)
                
        self.lc1 = wx.ListCtrl(splitter2, style=wx.LC_LIST)
        self.lc2 = wx.ListCtrl(splitter2, style=wx.LC_LIST)

        dt = MyTextDropTarget(self.lc2)
        self.lc2.SetDropTarget(dt)
        
        self.Bind(wx.EVT_LIST_BEGIN_DRAG, self.OnDragInit, id=self.lc1.GetId())

        tree = self.dirWid.GetTreeCtrl()

        splitter2.SplitHorizontally(self.lc1, self.lc2, 150)
        splitter1.SplitVertically(self.dirWid, splitter2, 200)

        self.Bind(wx.EVT_TREE_SEL_CHANGED, self.OnSelect, id=tree.GetId())

        self.OnSelect(0)

        self.SetTitle('Drag and drop text')
        self.Centre()

    def OnSelect(self, event):

        list = os.listdir(self.dirWid.GetPath())

        self.lc1.ClearAll()
        self.lc2.ClearAll()

        for i in range(len(list)):

            if list[i][0] != '.':
                self.lc1.InsertItem(0, list[i])

    def OnDragInit(self, event):

        text = self.lc1.GetItemText(event.GetIndex())
        tdo = wx.TextDataObject(text)
        tds = wx.DropSource(self.lc1)

        tds.SetData(tdo)
        tds.DoDragDrop(True)




    def LoadImages(self):

        self.rotunda = wx.StaticBitmap(self.panel, wx.ID_ANY,
            wx.Bitmap("BCC_logo-1.png", wx.BITMAP_TYPE_ANY))

    def OnExit(self, event):
        self.Close()

def main():

    app = wx.App()
    ex = Example(None, title='Go To Class')
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
