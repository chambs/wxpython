#Boa:Frame:Frame1

import wx

def create(parent):
    return Frame1(parent)

[wxID_FRAME1, wxID_FRAME1BUTTON1, wxID_FRAME1STATICTEXT1, 
] = [wx.NewId() for _init_ctrls in range(3)]

class Frame1(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,
              pos=wx.Point(400, 134), size=wx.Size(578, 475),
              style=wx.DEFAULT_FRAME_STYLE, title=u'my frist app')
        self.SetClientSize(wx.Size(578, 475))
        self.SetMaxSize(wx.Size(578, 475))
        self.SetMinSize(wx.Size(578, 475))

        self.button1 = wx.Button(id=wxID_FRAME1BUTTON1, label=u'Click me',
              name='button1', parent=self, pos=wx.Point(0, 0), size=wx.Size(112,
              48), style=0)
        self.button1.SetMinSize(wx.Size(112, 48))
        self.button1.SetMaxSize(wx.Size(112, 48))
        self.button1.Bind(wx.EVT_BUTTON, self.OnButton1Button,
              id=wxID_FRAME1BUTTON1)

        self.staticText1 = wx.StaticText(id=wxID_FRAME1STATICTEXT1,
              label=u'Welcome to my first app!', name='staticText1',
              parent=self, pos=wx.Point(192, 88), size=wx.Size(168, 32),
              style=0)
        self.staticText1.SetToolTipString(u'RUCULA')

    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnButton1Button(self, event):
        dlg = wx.MessageDialog(self, 'This is a simple modal window', 'first app modal', wx.OK)
        dlg.ShowModal()
        dlg.Destroy()
        event.Skip()
