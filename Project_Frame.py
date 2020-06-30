# -*- coding: utf-8 -*-

import wx
import wx.aui as AUI

from UserPanel import UserPanel
# from StatPanel import StatPanel
# from GraphPanel import GraphPanel

# parent is the panel of AppFrame

class Project_frame(AUI.AuiNotebook):
    
    def __init__(self, parent, db_user, db_event):
        AUI.AuiNotebook.__init__(self, parent, wx.ID_ANY, style=wx.NB_FLAT)
        
        self.user_tab = UserPanel(self, db_user=db_user, db_event=db_event)
        self.stat_tab = Tab(self)
        self.graph_tab = Tab(self)
        
        
        self.AddPage(self.user_tab, "User")
        self.AddPage(self.stat_tab, "Statistic")
        self.AddPage(self.graph_tab, "Graphic")
        
        
class Tab(wx.Panel):
    """
    Stupid tab for test
    """
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        t = wx.StaticText(self, -1, "This is a test", (20,20))