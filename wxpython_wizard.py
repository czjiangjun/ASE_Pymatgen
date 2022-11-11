#!/home/jun_jiang/.local/bin/python3
#coding:utf-8

import wx
import wx.adv

class configWizard(wx.adv.Wizard):
    def __init__(self, addNew = False):
        super(configWizard, self).__init__(None, -1, "Configuration Wizard")

        self.Bind(wx.adv.EVT_WIZARD_PAGE_CHANGED, self.OnPageChanged)
        self.Bind(wx.adv.EVT_WIZARD_PAGE_CHANGING, self.OnPageChanging)

        self.firstInfoPage = Info1Page(self,'title1')
        self.machineSelectPage = Info2Page(self,'title2')
        self.finialInfoPage = Info3Page(self,'title3')

        wx.adv.WizardPageSimple.Chain(self.firstInfoPage, self.machineSelectPage)
        wx.adv.WizardPageSimple.Chain(self.machineSelectPage, self.finialInfoPage)

        # self.GetPageAreaSizer().Add(self.firstInfoPage)
        self.RunWizard(self.firstInfoPage)
        self.Destroy()

    def OnPageChanging(self, e):
        print(e.GetPage())
        print('TEST')
#        print(e.GetPage().StoreData())

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

class Info3Page(wx.adv.WizardPageSimple):
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

class Example(wx.Frame):
    def __init__(self, *args, **kw):
        super(Example, self).__init__(*args, **kw)
        configWizard()
        self.InitButton()
        self.SetSize((300, 200))
        self.SetTitle('wx.Gauge')
        self.Centre()
        self.Show(True)
    def InitButton(self):
        pnl = wx.Panel(self)
        self.btn1 = wx.Button(pnl, label="Start")
        self.Bind(wx.EVT_BUTTON, self.OnStart, self.btn1)
    def OnStart(self, e):
        pass
        self.Destroy()

def main():
    ex = wx.App()
    Example(None)
    ex.MainLoop()


if __name__ == '__main__':
    main()

