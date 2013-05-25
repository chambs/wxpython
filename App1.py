#!/usr/bin/env python
#Boa:App:BoaApp

import wx

import script

modules ={u'script': [1, 'Main frame of Application', u'script.py']}

class BoaApp(wx.App):
    def OnInit(self):
        self.main = script.create(None)
        self.main.Show()
        self.SetTopWindow(self.main)
        return True

def main():
    application = BoaApp(0)
    application.MainLoop()

if __name__ == '__main__':
    main()
