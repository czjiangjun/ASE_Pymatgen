import wx

class TextFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, 'Text Editor', size=(300, 250))

        self.panel = wx.Panel(self, -1) 

        self.multiText = wx.TextCtrl(self.panel, -1,"",size=(200, 100), style=wx.TE_MULTILINE|wx.EXPAND)

        sizer = wx.BoxSizer()
        sizer.Add(self.multiText, proportion=1, flag=wx.CENTER|wx.EXPAND)
        self.panel.SetSizer(sizer)

        self.CreateStatusBar()

        self.multiText.Bind(wx.EVT_KEY_DOWN, self.updateLineCol)
        self.multiText.Bind(wx.EVT_LEFT_DOWN, self.updateLineCol)

    def updateLineCol(self, event):
        #lineNum = len(self.multiText.GetRange( 0, self.multiText.GetInsertionPoint() ).split("\n"))
        l,c = self.multiText.PositionToXY(self.multiText.GetInsertionPoint())

        self.StatusBar.SetStatusText(str(l)+","+str(c), number=0)

        event.Skip()

app = wx.App(False)
frame = TextFrame()
frame.Show()
app.MainLoop()
