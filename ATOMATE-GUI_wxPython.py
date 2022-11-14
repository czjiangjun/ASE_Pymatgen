#!/home/jun_jiang/.local/bin/python3
#coding:utf-8

from pathlib import Path
import os
import wx
import wx.adv
import wx.grid as gridlib

class configWizard(wx.adv.Wizard):
    def __init__(self, addNew = False):
        super(configWizard, self).__init__(None, -1, "Configuration Wizard")

        self.Bind(wx.adv.EVT_WIZARD_PAGE_CHANGED, self.OnPageChanged)
        self.Bind(wx.adv.EVT_WIZARD_PAGE_CHANGING, self.OnPageChanging)

        self.firstInfoPage = Info1Page(self,'title1')
        self.machineSelectPage = Info2Page(self,'title2')

        wx.adv.WizardPageSimple.Chain(self.firstInfoPage, self.machineSelectPage)

        # self.GetPageAreaSizer().Add(self.firstInfoPage)
        self.RunWizard(self.firstInfoPage)
        self.Destroy()

    def OnPageChanging(self, e):
        print(e.GetPage())
        # e.GetPage().StoreData()

    def OnPageChanged(self, e):
        if e.GetPage().AllowNext():
            self.FindWindowById(wx.ID_FORWARD).Enable()
        else:
            self.FindWindowById(wx.ID_FORWARD).Disable()
        if e.GetPage().AllowBack():
            self.FindWindowById(wx.ID_BACKWARD).Enable()
        else:
            self.FindWindowById(wx.ID_BACKWARD).Disable()


class Info1Page(wx.adv.WizardPageSimple):
    def __init__(self, parent, title):
        wx.adv.WizardPageSimple.__init__(self, parent)
        sizer = wx.GridBagSizer(5, 5)
        self.sizer = sizer
        self.SetSizer(sizer)

        title = wx.StaticText(self, -1, title)
        title.SetFont(wx.Font(18, wx.SWISS, wx.NORMAL, wx.BOLD))
        sizer.Add(title, pos=(0, 0), span=(1, 2), flag=wx.ALIGN_CENTRE | wx.ALL)
        sizer.Add(wx.StaticLine(self, -1), pos=(1, 0), span=(1, 2), flag=wx.EXPAND | wx.ALL)
        sizer.AddGrowableCol(1)

    def  AllowNext(self):
        print(1)
        return True

    def AllowBack(self):
        print(2)
        return False

class Info2Page(wx.adv.WizardPageSimple):
    def __init__(self, parent, title):
        wx.adv.WizardPageSimple.__init__(self, parent)
        sizer = wx.GridBagSizer(5, 5)
        self.sizer = sizer
        self.SetSizer(sizer)

        title = wx.StaticText(self, -1, title)
        title.SetFont(wx.Font(18, wx.SWISS, wx.NORMAL, wx.BOLD))
        sizer.Add(title, pos=(0, 0), span=(1, 2), flag=wx.ALIGN_CENTRE | wx.ALL)
        sizer.Add(wx.StaticLine(self, -1), pos=(1, 0), span=(1, 2), flag=wx.EXPAND | wx.ALL)
        sizer.AddGrowableCol(1)

    def  AllowNext(self):
        print(1)
        return True

    def AllowBack(self):
        print(2)
        return True

class PanelOne(wx.Panel):
    """""" 
    def __init__(self, parent):
        """Load_Or_Create_A_POSCAR"""
        wx.Panel.__init__(self, parent=parent, size=(500,300))
#        txt = wx.TextCtrl(self)
        self.InitUI()
        self.Centre()

    def InitUI(self):
        self.vbox = wx.BoxSizer(wx.VERTICAL)

        font = wx.SystemSettings.GetFont(wx.SYS_SYSTEM_FONT)
        font.SetPointSize(12)

        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        self.vbox.Add((-1, 80))
        st1 = wx.StaticText(self, label='Load From File')
        st1.SetFont(font)
        hbox1.Add(st1, flag=wx.RIGHT, border=8)

        self.vbox.Add(hbox1, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)
        btn0 = wx.Button(self, label='Open', size=(50, 30))
        hbox1.Add(btn0, flag=wx.LEFT, border=8)
        btn0.Bind(wx.EVT_BUTTON,  self.LoadFiles)
#        self.Destroy()
#        self.panel.Hide()

#        tc = wx.TextCtrl(self)
#        hbox1.Add(tc, proportion=1)
        self.SetSizer(self.vbox)

        self.Centre()

    def LoadFiles(self, event):

#        win = wx.FileDialog(self, -1, u'子窗口')    #创建子窗口
        dialog = wx.FileDialog(self, "Choose a file", os.getcwd(),
            "")
        if dialog.ShowModal() == wx.ID_OK:
             print(dialog.GetPath())
             self.Destroy()


class PanelTwo(wx.Panel):
    """"""
    def __init__(self, parent):
        """Generate_A_POSCAR"""
        wx.Panel.__init__(self, parent=parent)
#        self.grid = gridlib.Grid(self)
#        self.grid.CreateGrid(25,12)
        self.Generate_UI()
        self.Centre()

    def Generate_UI(self):
#        configWizard()
        self.sizer = wx.BoxSizer(wx.VERTICAL)
#        sizer.Add(self.grid, 0, wx.EXPAND)

        font = wx.SystemSettings.GetFont(wx.SYS_SYSTEM_FONT)
        font.SetPointSize(12)
        self.Font = font

        self.sizer.Add((-1, 80))
#        self.vbox2 = wx.BoxSizer(wx.VERTICAL)
        hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        str_element = wx.StaticText(self, label='Type_of_Elements, separated by comma')
#        dialog = wx.TextEntryDialog(self, "Choose Type of Elements")
        str_element.SetFont(self.Font)
        hbox3.Add(str_element, flag=wx.LEFT | wx. TOP, border=20)
        self.sizer.Add(hbox3, flag=wx.RIGHT | wx.TOP, border=10)

        hbox4 = wx.BoxSizer(wx.HORIZONTAL)
        self.tc = wx.TextCtrl(self)
        hbox4.Add(self.tc, proportion=1, flag=wx.LEFT | wx. TOP)
        btn4 = wx.Button(self, label='Modeling', size=(80, 30))
        hbox4.Add(btn4, flag=wx.LEFT, border=12)
        btn4.Bind(wx.EVT_BUTTON,  self.Model)
        self.sizer.Add(hbox4, flag=wx.RIGHT | wx.TOP, border=20)

        self.SetSizer(self.sizer)
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
            element_index = wx.StaticText(self, label='Element:'+i)
            element_index.SetFont(self.Font)
            hbox.Add(element_index, flag=wx.LEFT | wx. TOP, border=15)
#            self.element = wx.TextCtrl(self)
#            self.element.Bind(wx.EVT_TEXT, self.OnElement)
#            hbox.Add(self.element, proportion=1)

            number_index = wx.StaticText(self, label='Number:')
            hbox.Add(number_index, flag=wx.LEFT | wx. TOP, border=15)
#        dialog = wx.TextEntryDialog(self, "Choose Type of Elements")
            cb = wx.ComboBox(self, pos=(50, 30), choices=Index_num,
                    style=wx.CB_READONLY)

            self.st = wx.StaticText(self, label='', pos=(50, 140))
            hbox.Add(cb, flag=wx.LEFT, border=12)
            cb.Bind(wx.EVT_COMBOBOX, self.OnSelect)

            self.SetSize((550, 530))
#        self.SetTitle('wx.ComboBox')
            self.sizer.Add(hbox, flag=wx.RIGHT | wx.TOP, border=10)
            self.sizer.Add((-1, 10))
         

        Total_Atoms = 0
        for i in self.Nums:
            Total_Atoms = Total_Atoms + int(i)

        hbox5 = wx.BoxSizer(wx.HORIZONTAL)
        btn5 = wx.Button(self, label='OK', size=(50, 30))
        hbox5.Add(btn5)
#        btn5.Bind(wx.EVT_BUTTON,  self.Generate)
        self.sizer.Add(hbox5, flag=wx.RIGHT | wx.TOP, border=10)
        btn5.Bind(wx.EVT_BUTTON,  self.Position)
        self.sizer.Add(hbox5, flag=wx.RIGHT | wx.TOP, border=10)
        self.sizer.Add((-1, 10))

        self.SetSizer(self.sizer)
#        self.vbox.Add((-1, 10))
#        btn3.Bind(wx.EVT_BUTTON,  self.Position)
    def OnSelect(self, e):

        i = e.GetString()
        self.Nums.append(i)
#        print(self.Nums)

    def Position(self, event):

#        print(self.Elements)
#        print(self.Nums)
        thirdWindow = window3(parent=self, Elements=self.Elements, Nums=self.Nums)
        thirdWindow.Show()



class Example(wx.Frame):

    def __init__(self, parent, title):
#        super(Example, self).__init__(parent, title=title)
        super(Example, self).__init__(parent, title=title,
            size=(350, 300))

        self.InitUI()
        self.Centre()

    def InitUI(self):
#        configWizard()
        self.LoadImages()

#        self.vbox = wx.BoxSizer(wx.VERTICAL)
        font = wx.SystemSettings.GetFont(wx.SYS_SYSTEM_FONT)
        font.SetPointSize(9)
        self.Font = font

        self.panel_one = PanelOne(self)
        self.panel_two = PanelTwo(self)
        self.panel_one.Hide()
        self.panel_two.Hide()
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.panel_one, 1, wx.EXPAND)
        self.sizer.Add(self.panel_two, 1, wx.EXPAND)

        self.sizer.Add((-1, 80))
        hbox1 = wx.BoxSizer(wx.HORIZONTAL)

        #self.st1 = wx.StaticText(self, label='Load From File', pos=(0,250))
        self.st1 = wx.StaticText(self, label='Load_From_File           ')
        self.st1.SetFont(font)
        hbox1.Add(self.st1, flag=wx.RIGHT, border=8)
        self.sizer.Add(hbox1, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)
        self.btn0 = wx.Button(self, label='Open', size=(50, 30))
        hbox1.Add(self.btn0, flag=wx.LEFT, border=8)
        self.btn0.Bind(wx.EVT_BUTTON,  self.LoadFiles)

        self.sizer.Add((-1, 10))
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        self.st2 = wx.StaticText(self, label='Generate_Structure')
        self.st2.SetFont(font)
        hbox2.Add(self.st2, flag=wx.RIGHT, border=8)
        self.sizer.Add(hbox2, flag=wx.LEFT | wx.TOP, border=10)

        self.btn1 = wx.Button(self, label='Generate', size=(60, 30))
        hbox2.Add(self.btn1, flag=wx.LEFT, border=12)
#        btn1.Bind(wx.EVT_BUTTON, self.newwindow, btn1)
        self.btn1.Bind(wx.EVT_BUTTON,  self.Generate)

        self.SetSizer(self.sizer)

    def Generate(self, event):
        """"""
#        if self.panel_one.IsShown():
        self.SetTitle("Generate_A_POSCAR")
        self.SetSize((550, 530))
        self.panel_one.Hide()
        self.panel_two.Show()
        self.st1.Hide()
        self.st2.Hide()
        self.btn0.Hide()
        self.btn1.Hide()
#        else:
    def LoadFiles(self, event):
        """"""
#        self.panel.Hide()
        self.SetTitle("Choose_A_POSCAR")
        self.panel_one.Show()
        self.panel_two.Hide()
        self.st1.Hide()
        self.st2.Hide()
        self.btn0.Hide()
        self.btn1.Hide()
        self.Layout()

# Run the program

#        secondWindow = window2(parent=self.panel)
#        secondWindow.Show()


    def LoadImages(self):
#        bitmap = wx.Bitmap(path)
#        bitmap = wx.Bitmap("/home/jun_jiang/Softs/ASE_Pymatgen/BCC_logo-1.png")
        bitmap = wx.Bitmap("BCC_logo-1.png")
#        bitmap = scale_bitmap(bitmap, 300, 200)
        bitmap = self.scale_bitmap(bitmap, 300, 70)
#        control = wx.StaticBitmap(self, -1, bitmap)
        self.rotunda = wx.StaticBitmap(self, wx.ID_ANY, bitmap)
#        control.SetPosition((10, 10))
        self.rotunda.SetPosition((10, 10))

    def scale_bitmap(self, bitmap, width, height):
#        image = wx.ImageFromBitmap(bitmap)
        image = bitmap.ConvertToImage()
        image = image.Scale(width, height, wx.IMAGE_QUALITY_HIGH)
#        result = wx.BitmapFromImage(image)
        result = wx.Bitmap(image)
        return result

    def OnExit(self, event):
        self.Close()

#class Figures(wx.Panel):
#    def __init__(self, parent, path):
#        super(Panel, self).__init__(parent, -1)
#        bitmap = wx.Bitmap(path)
#        bitmap = scale_bitmap(bitmap, 300, 200)
#        control = wx.StaticBitmap(self, -1, bitmap)
#        control.SetPosition((10, 10))
#
#    def scale_bitmap(bitmap, width, height):
#        image = wx.ImageFromBitmap(bitmap)
#        image = image.Scale(width, height, wx.IMAGE_QUALITY_HIGH)
#        result = wx.BitmapFromImage(image)
#        return result

class window2(wx.Frame):

#    title = "new Window"

    def __init__(self,parent):
        wx.Frame.__init__(self,parent, -1,title ='Construct_Parameter', size=(1000,300))
        self.panel2=wx.Panel(self, -1)

        self.Generate_UI()
        self.Centre()

    def Generate_UI(self):
        pass

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
        vector=['x','y','z']

        for i in range(3):
            vec_i=[]
            hbox = wx.BoxSizer(wx.HORIZONTAL)
            str_vec = wx.StaticText(self.panel3, label='Vec_'+vector[i])
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
            str_vec = wx.StaticText(self.panel3, label='Atom_'+str(i+1))
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
        btn1 = wx.Button(self.panel3, label='OK')
        hbox5.Add(btn1, flag=wx.LEFT, border=5)
        btn1.Bind(wx.EVT_BUTTON,  self.POSCAR)
        self.vbox2.Add(hbox5, flag=wx.LEFT, border=5)
        self.panel3.SetSizer(self.vbox2)
        self.Layout()


    def POSCAR(self, event):
        Poscar_File = open('POSCAR', 'w')
        Poscar_File.writelines(' '+self.name+'\n')
        Poscar_File.writelines(' 1.000000\n')
        for i in range(3):
            Poscar_File.writelines('  ')
            for j in self.vec[i]:
                Poscar_File.writelines(j.GetValue()+'  ')
            Poscar_File.writelines('\n')
        Poscar_File.writelines(' ')
        for i in self.atoms:
            Poscar_File.writelines(i+'  ')
        Poscar_File.writelines('\n')
        Poscar_File.writelines(' ')
        for i in self.nums:
            Poscar_File.writelines(i+'  ')
        Poscar_File.writelines('\n')
        if (self.cb.GetValue()):
            Poscar_File.writelines(' Select Dynamics\n')
        Poscar_File.writelines(' Direct\n')
        for i in range(self.total):
            Poscar_File.writelines('  ')
            for j in self.atom[i]:
                Poscar_File.writelines(j.GetValue()+'  ')
            Poscar_File.writelines('\n')
        self.Destroy()


def main():

    app = wx.App()
    ex = Example(None, title='File_Of_Structure')
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
