# -*- coding: utf-8 -*-

import wx
import numpy as np
import wx.aui as AUI

from matplotlib.backends.backend_wxagg  import FigureCanvasWxAgg as FigCanvas
from matplotlib.figure import Figure
from UserPanel import UserPanel
# from StatPanel import StatPanel
# from GraphPanel import GraphPanel

# parent is the panel of AppFrame

class Project_frame(AUI.AuiNotebook):
    
    def __init__(self, parent, db_user, db_event, db_params):
        AUI.AuiNotebook.__init__(self, parent, wx.ID_ANY, style=wx.NB_FLAT)
        
        self.user_tab = UserPanel(self, db_user=db_user, db_event=db_event, db_params=db_params)
        self.stat_tab = Tab(self)
        self.graph_tab = Tab(self)
        
        self.stat_tab.draw()
        self.graph_tab.draw()
        
        
        self.AddPage(self.user_tab, "User")
        self.AddPage(self.stat_tab, "Statistic")
        self.AddPage(self.graph_tab, "Graphic")
        
        
class Tab(wx.Panel):
    """
    Stupid tab for test
    """
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.figure = Figure()
        self.axes = self.figure.add_subplot(111)
        self.canvas = FigCanvas(self, -1, self.figure)
        self.axes.set_xlabel("Time")
        self.axes.set_ylabel("Test")
        
        szr = wx.BoxSizer(wx.HORIZONTAL)
        szr.Add(self.canvas, 1, wx.EXPAND)
        
        self.SetSizer(szr)

    def draw(self):
        x = np.arange(0,5,0.1)
        y = np.sin(np.pi*x)
        self.axes.plot(x,y)