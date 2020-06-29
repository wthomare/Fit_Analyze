# -*- coding: utf-8 -*-
import wx


class DlgImport(wx.FileDialog):
    def __init__(self, parent):
        wx.FileDialog.__init__(self, parent, "Load", "", "", "fit files (*.fit)|*.fit", wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
        self.ShowModal()
        