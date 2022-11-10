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

    def __init__(self, parent, title):
#        super(Example, self).__init__(parent, title=title)
        super(Example, self).__init__(parent, title=title,
            size=(350, 300))

        self.InitUI()
        self.Centre()

    def InitUI(self):
        LLoad = False

        self.panel = wx.Panel(self)
#        self.panel = wx.Panel(self)

        font = wx.SystemSettings.GetFont(wx.SYS_SYSTEM_FONT)

        font.SetPointSize(9)

        self.vbox = wx.BoxSizer(wx.VERTICAL)

        LLoad = True

        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        st1 = wx.StaticText(self.panel, label='Load From File')
        st1.SetFont(font)
        hbox1.Add(st1, flag=wx.RIGHT, border=8)

        self.vbox.Add(hbox1, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)

#        tc = wx.TextCtrl(self.panel)
#        hbox1.Add(tc, proportion=1)
        btn0 = wx.Button(self.panel, label='Open', size=(50, 30))
        hbox1.Add(btn0, flag=wx.LEFT, border=8)
        btn0.Bind(wx.EVT_BUTTON,  self.LoadFiles)
        self.vbox.Add((-1, 10))

#        self.Destroy()
#        self.panel.Hide()
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        st2 = wx.StaticText(self.panel, label='Generate_Structure')
        st2.SetFont(font)
        hbox2.Add(st2, flag=wx.RIGHT, border=8)
        self.vbox.Add(hbox2, flag=wx.LEFT | wx.TOP, border=10)

        self.Font = font
        btn1 = wx.Button(self.panel, label='Generate', size=(50, 30))
        hbox2.Add(btn1, flag=wx.LEFT, border=12)
#        btn1.Bind(wx.EVT_BUTTON, self.newwindow, btn1)
        btn1.Bind(wx.EVT_BUTTON,  self.Generate)

        self.panel.SetSizer(self.vbox)




        if LLoad == False :

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

#        win = wx.FileDialog(self, -1, u'子窗口')    #创建子窗口
        self.Centre()
        dialog = wx.FileDialog(self, "Choose a file", os.getcwd(),
            "")
        if dialog.ShowModal() == wx.ID_OK:
             print(dialog.GetPath())
             self.Destroy()



#    def Position(self, event):
 #       print(self.Elements)
 #       print(self.Nums)

#        splitter1 = wx.SplitterWindow(self, style=wx.SP_3D, size=(450,400))
#        splitter2 = wx.SplitterWindow(splitter1, style=wx.SP_3D, size=(350,300))

#        home_dir = str(Path.home())

#        self.dirWid = wx.GenericDirCtrl(splitter1, dir=home_dir, 
#                style=wx.DIRCTRL_DIR_ONLY)
                
#        self.lc1 = wx.ListCtrl(splitter2, style=wx.LC_LIST)
#        self.lc2 = wx.ListCtrl(splitter2, style=wx.LC_LIST)

#        dt = MyTextDropTarget(self.lc2)
#        self.lc2.SetDropTarget(dt)
        
#        self.Bind(wx.EVT_LIST_BEGIN_DRAG, self.OnDragInit, id=self.lc1.GetId())

#        tree = self.dirWid.GetTreeCtrl()

#        splitter2.SplitHorizontally(self.lc1, self.lc2, 150)
#        splitter1.SplitVertically(self.dirWid, splitter2, 200)

#        self.Bind(wx.EVT_TREE_SEL_CHANGED, self.OnSelect, id=tree.GetId())

#        self.OnSelect(3)

#        self.SetTitle('Drag and drop text')


    def LoadImages(self):

        self.rotunda = wx.StaticBitmap(self.panel, wx.ID_ANY,
            wx.Bitmap("BCC_logo-1.png", wx.BITMAP_TYPE_ANY))

    def OnExit(self, event):
        self.Close()

    def Generate(self, event):
        self.panel.Hide()
        secondWindow = window2(parent=self.panel)
        secondWindow.Show()


class window2(wx.Frame):

#    title = "new Window"

    def __init__(self,parent):
        wx.Frame.__init__(self,parent, -1,title ='Construct_Parameter', size=(1000,300))
        self.panel2=wx.Panel(self, -1)

        self.Generate_UI()
        self.Centre()

    def Generate_UI(self):

        font = wx.SystemSettings.GetFont(wx.SYS_SYSTEM_FONT)

        font.SetPointSize(12)
        self.Font = font

#        self.panel.Hide()
        self.vbox2 = wx.BoxSizer(wx.VERTICAL)
        hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        str_element = wx.StaticText(self.panel2, label='Type_of_Elements, separated by comma')
#        dialog = wx.TextEntryDialog(self, "Choose Type of Elements")
        str_element.SetFont(self.Font)
        hbox3.Add(str_element, flag=wx.LEFT | wx. TOP, border=20)
        self.vbox2.Add(hbox3, flag=wx.RIGHT | wx.TOP, border=10)
        self.vbox2.Add((-1, 10))


        hbox4 = wx.BoxSizer(wx.HORIZONTAL)
        self.tc = wx.TextCtrl(self.panel2)
        hbox4.Add(self.tc, proportion=1, flag=wx.LEFT | wx. TOP, border=20)
        btn4 = wx.Button(self.panel2, label='Modeling', size=(50, 30))
        hbox4.Add(btn4, flag=wx.LEFT, border=12)
        btn4.Bind(wx.EVT_BUTTON,  self.Model)
        self.vbox2.Add(hbox4, flag=wx.RIGHT | wx.TOP, border=20)

        self.panel2.SetSizer(self.vbox2)
        self.Show()

    def Model(self, event):

        self.Nums = []
        elements = [i.strip() for i in self.tc.GetValue().split(',') if i.strip()!='']
#        print(elements)
        self.Elements = elements
#        exit()
        Index_num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

        for i in elements:

            hbox = wx.BoxSizer(wx.HORIZONTAL)
            element_index = wx.StaticText(self.panel2, label='Element:'+i)
            element_index.SetFont(self.Font)
            hbox.Add(element_index, flag=wx.LEFT | wx. TOP, border=15)
#            self.element = wx.TextCtrl(self.panel2)
#            self.element.Bind(wx.EVT_TEXT, self.OnElement)
#            hbox.Add(self.element, proportion=1)

            number_index = wx.StaticText(self.panel2, label='Number:')
            hbox.Add(number_index, flag=wx.LEFT | wx. TOP, border=15)
#        dialog = wx.TextEntryDialog(self, "Choose Type of Elements")
            cb = wx.ComboBox(self.panel2, pos=(50, 30), choices=Index_num,
                    style=wx.CB_READONLY)

            self.st = wx.StaticText(self.panel2, label='', pos=(50, 140))
            hbox.Add(cb, flag=wx.LEFT, border=12)
            cb.Bind(wx.EVT_COMBOBOX, self.OnSelect)

            self.SetSize((550, 530))
#        self.SetTitle('wx.ComboBox')
            self.vbox2.Add(hbox, flag=wx.RIGHT | wx.TOP, border=10)
            self.vbox2.Add((-1, 10))
         

        Total_Atoms = 0
        for i in self.Nums:
            Total_Atoms = Total_Atoms + int(i)

        hbox5 = wx.BoxSizer(wx.HORIZONTAL)
        btn5 = wx.Button(self.panel2, label='OK', size=(50, 30))
        hbox5.Add(btn5)
#        btn5.Bind(wx.EVT_BUTTON,  self.Generate)
        self.vbox2.Add(hbox5, flag=wx.RIGHT | wx.TOP, border=10)
        btn5.Bind(wx.EVT_BUTTON,  self.Position)
        self.vbox2.Add(hbox5, flag=wx.RIGHT | wx.TOP, border=10)
        self.vbox2.Add((-1, 10))

#        self.vbox.Add((-1, 10))
#        btn3.Bind(wx.EVT_BUTTON,  self.Position)
    def OnSelect(self, e):

        i = e.GetString()
        self.Nums.append(i)
#        print(self.Nums)

    def Position(self, event):

#        print(self.Elements)
#        print(self.Nums)
        thirdWindow = window3(parent=self.panel2, Elements=self.Elements, Nums=self.Nums)
        thirdWindow.Show()

class window3(wx.Frame):

#    title = "new Window"

    def __init__(self, parent, Elements, Nums):
        wx.Frame.__init__(self,parent, -1,title ='Construct_Parameter', size=(1000,300))
        self.panel3=wx.Panel(self, -1)
#        print(Nums)
#        exit()
        self.Position_UI(Elements, Nums)
        self.Centre()

    def Position_UI(self, Elements, Nums):
        Total_atoms = 0
        self.vec=[]
        self.atom=[]
        self.atoms=Elements
        self.nums=Nums
        self.name=''
        for i in Elements:
            if (int(Nums[Elements.index(i)])>1):
               self.name=self.name+i+Nums[Elements.index(i)]
            else:
               self.name=self.name+i

        for i in Nums:
            Total_atoms = Total_atoms+int(i) 
#        self.SetBackgroundColour(wx.Colour(100,100,100))
        self.total=Total_atoms
        font = wx.SystemSettings.GetFont(wx.SYS_SYSTEM_FONT)

        font.SetPointSize(12)
        self.Font = font

        self.vbox2 = wx.BoxSizer(wx.VERTICAL)
        hbox0 = wx.BoxSizer(wx.HORIZONTAL)
        str_element = wx.StaticText(self.panel3, label='Input The Parameter of Crystal')
#        dialog = wx.TextEntryDialog(self, "Choose Type of Elements")
#        str_element.SetFont(self.Font)
        hbox0.Add(str_element, flag=wx.RIGHT, border=25)
        self.vbox2.Add(hbox0, wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=40)

#        btn0 = wx.Button(self.panel3, label='Open', pos=(500,0), size=(50, 20))
#        hbox0.Add(btn0, flag=wx.RIGHT, border=8)
#        btn0.Bind(wx.EVT_BUTTON,  self.LoadFiles)
        self.vbox2.Add((-1, 10))

        for i in range(3):
            vec_i=[]
            hbox = wx.BoxSizer(wx.HORIZONTAL)
            str_vec = wx.StaticText(self.panel3, label='Vec_'+str(i))
            hbox.Add(str_vec, 1, flag = wx.TOP, border=10)
#            str_vec = wx.StaticText(self.panel3, label='Vec_1', pos=(500,50))
#            dialo = wx.TextEntryDialog(self, "Choose Type of Elements")
#            str_vec.SetFont(self.Font)

            tc1 = wx.TextCtrl(self.panel3)
            hbox.Add(tc1, proportion=1, border=10)
            vec_i.append(tc1)
            hbox.Add((15,10))
            tc2 = wx.TextCtrl(self.panel3)
            hbox.Add(tc2, proportion=1, border=10)
            vec_i.append(tc2)
            hbox.Add((15,10))
            tc3 = wx.TextCtrl(self.panel3)
            vec_i.append(tc3)
            hbox.Add(tc3, proportion=1, border=10)

            self.vbox2.Add(hbox, proportion=1, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)
            self.vbox2.Add((-1, 10))
            self.vec.append(vec_i)
#
#        self.vbox2.Add(hbox2, proportion=1, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=30)
        hbox4 = wx.BoxSizer(wx.HORIZONTAL)
        self.cb = wx.CheckBox(self.panel3, label='Select Dynamics')
        self.cb.SetFont(font)
        hbox4.Add(self.cb)
        self.vbox2.Add((-1, 10))
        self.vbox2.Add(hbox4, flag=wx.LEFT, border=10)
#
        for i in range(Total_atoms):
            vec_i=[]
            hbox = wx.BoxSizer(wx.HORIZONTAL)
            str_vec = wx.StaticText(self.panel3, label='Vec_'+str(i))
            hbox.Add(str_vec, 1, flag = wx.TOP, border=10)
#            str_vec = wx.StaticText(self.panel3, label='Vec_1', pos=(500,50))
#            dialo = wx.TextEntryDialog(self, "Choose Type of Elements")
#            str_vec.SetFont(self.Font)

            tc1 = wx.TextCtrl(self.panel3)
            hbox.Add(tc1, proportion=1, border=10)
            vec_i.append(tc1)
            hbox.Add((15,10))
            tc2 = wx.TextCtrl(self.panel3)
            hbox.Add(tc2, proportion=1, border=10)
            vec_i.append(tc2)
            hbox.Add((15,10))
            tc3 = wx.TextCtrl(self.panel3)
            vec_i.append(tc3)
            hbox.Add(tc3, proportion=1, border=10)

            self.vbox2.Add(hbox, proportion=1, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)
            self.vbox2.Add((-1, 10))
            self.atom.append(vec_i)

        hbox5 = wx.BoxSizer(wx.HORIZONTAL)
        btn1 = wx.Button(self.panel3, label='OK', size=(50, 30))
        hbox5.Add(btn1, flag=wx.LEFT, border=12)
        btn1.Bind(wx.EVT_BUTTON,  self.POSCAR)
        self.panel3.SetSizer(self.vbox2)
        self.Show()

    def POSCAR(self, event):
        print(self.name)
        print('   1.000000')
        for i in range(3):
            for j in self.vec[i]:
                print(j.GetValue())
        print(self.atoms)
        print(self.nums)
        if (self.cb.GetValue()):
            print('Select Dynamics')
        print('Direct')
        self.Destroy()
        for i in range(self.total):
            for j in self.atom[i]:
                print(j.GetValue())



def main():

    app = wx.App()
    ex = Example(None, title='Go To Class')
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
