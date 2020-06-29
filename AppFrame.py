# -*- coding: utf-8 -*-

import wx
import wx.ribbon as RB

import UI_parameters
import images
from Utils import CreateBitmap

class RibbonFrame(wx.Frame):
    
    def __init__(self, parent, id=wx.ID_ANY, title="", pos=wx.DefaultPosition, size=wx.DEFAULT_FRAME_STYLE, log=None):

        wx.Frame.__init__(self, parent, id, title, pos, size)
        panel = wx.Panel(self)
        
        self._ribbon = RB.RibbonBar(panel, style=RB.RIBBON_BAR_DEFAULT_STYLE |RB.RIBBON_BAR_SHOW_PANEL_EXT_BUTTONS)
        
        self._bitmap_creation_dc = wx.MemoryDC()
        self._colour_data = wx.ColourData()
        
        home = RB.RibbonPage(self._ribbon, wx.ID_ANY, "HomePage", CreateBitmap("ribbon"))
        
        
        # First page
        toolbar_panel = RB.RibbonPanel(home, wx.ID_ANY, "Toolbar", style = RB.RIBBON_PANEL_NO_AUTO_MINIMISE | RB.RIBBON_PANEL_EXT_BUTTON)
        toolbar = RB.RibbonToolBar(toolbar_panel, UI_parameters.ID_MAIN_TOOLBAR)
        toolbar.AddTool(UI_parameters.ID_MNUUNDO, wx.ArtProvider.GetBitmap(wx.ART_UNDO, wx.ART_OTHER, wx.Size(24,23)))
        toolbar.AddTool(UI_parameters.ID_MNUREDO, wx.ArtProvider.GetBitmap(wx.ART_REDO, wx.ART_OTHER, wx.Size(24,23)))
        toolbar.AddSeparator()
        
        toolbar.AddTool(UI_parameters.ID_MNUFILEOPEN, wx.ArtProvider.GetBitmap(wx.ART_FILE_OPEN, wx.ART_OTHER, wx.Size(24,23)))
        toolbar.AddTool(UI_parameters.ID_MNUFILESAVE, wx.ArtProvider.GetBitmap(wx.ART_FILE_SAVE, wx.ART_OTHER, wx.Size(24,23)))
        toolbar.AddTool(UI_parameters.ID_MNUFILESAVEAS, wx.ArtProvider.GetBitmap(wx.ART_FILE_SAVE, wx.ART_OTHER, wx.Size(24,23)))
        toolbar.AddTool(UI_parameters.ID_MNUFILEPRINT, wx.ArtProvider.GetBitmap(wx.ART_PRINT, wx.ART_OTHER, wx.Size(24,23)))
        toolbar.AddSeparator()
        toolbar.SetRows(2, 3)
        
        user_panel = RB.RibbonPanel(home, wx.ID_ANY, "User",style = RB.RIBBON_PANEL_NO_AUTO_MINIMISE | RB.RIBBON_PANEL_EXT_BUTTON)
        user = RB.RibbonToolBar(user_panel, wx.ID_ANY)
        user.AddTool(UI_parameters.ADD_User, wx.ArtProvider.GetBitmap(wx.ART_PLUS , wx.ART_OTHER, wx.Size(24,23)), "Add User")
        user.AddTool(UI_parameters.DEL_User, wx.ArtProvider.GetBitmap(wx.ART_MINUS , wx.ART_OTHER, wx.Size(24,23)), "Delete User")
        user.AddTool(UI_parameters.EDIT_User, wx.ArtProvider.GetBitmap(wx.ART_FIND_AND_REPLACE , wx.ART_OTHER, wx.Size(24,23)), "Modify User")

        event_panel = RB.RibbonPanel(home, wx.ID_ANY, "Event",style = RB.RIBBON_PANEL_NO_AUTO_MINIMISE | RB.RIBBON_PANEL_EXT_BUTTON)
        event = RB.RibbonToolBar(event_panel, wx.ID_ANY)
        event.AddTool(UI_parameters.ADD_Event, wx.ArtProvider.GetBitmap(wx.ART_PLUS , wx.ART_OTHER, wx.Size(24,23)), "Add Event")
        event.AddTool(UI_parameters.DEL_Event, wx.ArtProvider.GetBitmap(wx.ART_MINUS , wx.ART_OTHER, wx.Size(24,23)), "Delete Event")


        # Second page
        stats_page = RB.RibbonPage(self._ribbon, wx.ID_ANY, "Statistic analyzes", CreateBitmap("eye"))
        stats_panel = RB.RibbonPanel(stats_page, wx.ID_ANY, "Save", CreateBitmap("selection_panel"))
        stats_tools = RB.RibbonToolBar(stats_panel, wx.ID_ANY)
        stats_tools.AddTool(UI_parameters.ID_MNUFILEOPEN, wx.ArtProvider.GetBitmap(wx.ART_FILE_OPEN, wx.ART_OTHER, wx.Size(24,23)))
        stats_tools.AddTool(UI_parameters.ID_MNUFILESAVE, wx.ArtProvider.GetBitmap(wx.ART_FILE_SAVE, wx.ART_OTHER, wx.Size(24,23)))
        stats_tools.AddSeparator()
        stats_tools.AddTool(UI_parameters.ID_MNUFILESAVEAS, wx.ArtProvider.GetBitmap(wx.ART_FILE_SAVE, wx.ART_OTHER, wx.Size(24,23)))        
        stats_tools.AddTool(UI_parameters.ID_MNUFILEPRINT, wx.ArtProvider.GetBitmap(wx.ART_PRINT, wx.ART_OTHER, wx.Size(24,23)))
        stats_tools.SetRows(2, 3)
        

        s = wx.BoxSizer(wx.VERTICAL)
        s.Add(self._ribbon, 0, wx.EXPAND)
        
        panel.SetSizer(s)
        self.panel = panel

        self._BindEvents(toolbar)

        self.SetIcon(images.mondrian.Icon)
        self.CenterOnScreen()
        self._ribbon.Realize()

        
    def _BindEvents(self, toolbar):
        
        """
        Callbacks
        """        
        #Undo / Redo
        toolbar.Bind(RB.EVT_RIBBONTOOLBAR_CLICKED, self.OnMnuUndo, id=UI_parameters.ID_MNUUNDO)
        toolbar.Bind(RB.EVT_RIBBONTOOLBAR_CLICKED, self.OnMnuRedo, id=UI_parameters.ID_MNUREDO)
        
        # Print
        toolbar.Bind(RB.EVT_RIBBONTOOLBAR_CLICKED, self.OnMnuFilePrint, id=UI_parameters.ID_MNUFILEPRINT)

        for ID in {UI_parameters.ADD_User, UI_parameters.DEL_User, UI_parameters.EDIT_User,
                   UI_parameters.ADD_Event, UI_parameters.DEL_Event}:
            self.Bind(RB.EVT_RIBBONTOOLBAR_CLICKED, (lambda x: self.OnNewAction(x)), id=ID)
            
        
    def OnMnuUndo(self, event):
        pass
    
    def OnMnuRedo(self, event):
        pass
    
    def OnMnuFilePrint(self, event):
        pass

    def OnNewAction(self, event):
        self._ctrl.setCurrentAction(UI_parameters.ACTIONS[event.GetId()])
        self._fileHandling.setModified(True)
        self._ctrl.updateTitle()