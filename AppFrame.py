# -*- coding: utf-8 -*-

import os
import copy
import wx
import wx.ribbon as RB
import wx.grid as gridlib

import UI_parameters
import images

from Utils import CreateBitmap
from UserPannel import UserPannel
from Logger import Logger
from DB_Handler import DB_Handler
from User_profil import User_profil
from FitFile_Handler import FitFile_handler

from DlgAddUser import DlgAddUser
from DlgImport import DlgImport

import xml.etree.ElementTree as ET


class RibbonFrame(wx.Frame):
    
    def __init__(self, parent, id=wx.ID_ANY, title="", pos=wx.DefaultPosition, size=wx.DEFAULT_FRAME_STYLE, log=None):

        wx.Frame.__init__(self, parent, id, title, pos, size)
        panel = wx.Panel(self)
        
        
        logger = Logger('FIT_UI')
        logger.add_StreamHandler()
        logger.add_FileHandler('Initial_test.log')
        self.logger = logger.logger
        
        self.parameters =  {}
        tree = ET.parse("parameters.xml")
        root = tree.getroot()
        for child in root:
            for sub_child in child:
                self.parameters[sub_child.tag] = sub_child.test.encode('utf8')
        self.parameters["REPO_DIR"] = os.getcwd()
        
        
        self._ribbon = RB.RibbonBar(panel, style=RB.RIBBON_BAR_DEFAULT_STYLE |RB.RIBBON_BAR_SHOW_PANEL_EXT_BUTTONS)
        
        self._bitmap_creation_dc = wx.MemoryDC()
        self._colour_data = wx.ColourData()
        self.db_user = DB_Handler('users', self.parameters, self.logger)
        self.db_event = DB_Handler("event", self.parameters, self.logger)
        self.events = []
        self.fit_dict = {}
        
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

        race_panel = RB.RibbonPanel(home, wx.ID_ANY, "Event",style = RB.RIBBON_PANEL_NO_AUTO_MINIMISE | RB.RIBBON_PANEL_EXT_BUTTON)
        race = RB.RibbonToolBar(race_panel, wx.ID_ANY)
        race.AddTool(UI_parameters.ADD_Event, wx.ArtProvider.GetBitmap(wx.ART_PLUS , wx.ART_OTHER, wx.Size(24,23)), "Add Event")
        race.AddTool(UI_parameters.DEL_Event, wx.ArtProvider.GetBitmap(wx.ART_MINUS , wx.ART_OTHER, wx.Size(24,23)), "Delete Event")


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
        # window splitting
        self._logwindow = wx.SplitterWindow(panel, wx.ID_ANY)
        
        #♦ User browser
        self.current_user = User_profil()
        self.load_users()
        self.user_list = wx.ListBox(self._logwindow, id=wx.ID_ANY, choices = self.users, pos=wx.DefaultPosition, size=wx.DefaultSize, style=wx.LC_ICON, validator=wx.DefaultValidator, name=wx.ListCtrlNameStr)
        
        
        self.myUser = UserPannel(self._logwindow)
        
        # Set splitter
        self._logwindow.SetMinimumPaneSize(20)
        self._logwindow.SplitVertically(self.user_list, self.myUser, sashPosition = 160)
                
        
        
        s.Add(self._ribbon, 0, wx.EXPAND)
        s.Add(self._logwindow, 1, wx.EXPAND)
        
        panel.SetSizer(s)
        self.panel = panel

        self._BindEvents(toolbar, user, race)

        self.SetIcon(images.mondrian.Icon)
        self.CenterOnScreen()
        self._ribbon.Realize()

        
    def _BindEvents(self, toolbar, user, race):
        
        """
        Callbacks
        """        
        toolbar.Bind(RB.EVT_RIBBONTOOLBAR_CLICKED, self.OnMnuUndo, id=UI_parameters.ID_MNUUNDO)
        toolbar.Bind(RB.EVT_RIBBONTOOLBAR_CLICKED, self.OnMnuRedo, id=UI_parameters.ID_MNUREDO)
        toolbar.Bind(RB.EVT_RIBBONTOOLBAR_CLICKED, self.OnMnuFilePrint, id=UI_parameters.ID_MNUFILEPRINT)
        
        user.Bind(RB.EVT_RIBBONTOOLBAR_CLICKED, self.OnMnuAddU, id=UI_parameters.ADD_User)
        user.Bind(RB.EVT_RIBBONTOOLBAR_CLICKED, self.OnMnuDelU, id=UI_parameters.DEL_User)
        user.Bind(RB.EVT_RIBBONTOOLBAR_CLICKED, self.OnMnuEditU, id=UI_parameters.EDIT_User)
        
        race.Bind(RB.EVT_RIBBONTOOLBAR_CLICKED, self.OnMnuAddEvent, id=UI_parameters.ADD_Event)
        race.Bind(RB.EVT_RIBBONTOOLBAR_CLICKED, self.OnMnuDelEvent, id=UI_parameters.DEL_Event)
        
        self.Bind(wx.EVT_LISTBOX, self.onListBox, self.user_list)
        
        
    def load_users(self):
        sql_query = "SELECT DISTINCT name, nickname FROM users"
        rows = self.db_user.load_data(sql_query)
        
        self.users = [str(row[0]) + ' ' + str(row[1]) for row in rows]
        
    
    def insert_user(self, user_profil):
        print(user_profil)
        self.db_user.insert_data(user_profil)
    
    def onListBox(self, event):
        name, nickname = event.GetEventObject().GetStringSelection().split(" ")
        
        sql_query = "SELECT id, age , weight, size ,FCMin ,FCMax ,FTP FROM users WHERE name LIKE '%{}%' AND nickname LIKE '%{}%'".format(name, nickname)
        
        rows = list(self.db_user.load_data(sql_query)[0])

        rows.insert(0, nickname)
        rows.insert(0, name)
        rows = tuple(rows)
        
        self.current_user.from_db(rows)
        self.myUser.update(self.current_user)
        
        self.refresh_events_list()
        
    def refresh_events_list(self):
        sql_query = "SELECT DISTINCT event_name FROM event WHERE user_id={}".format(self.current_user.user_id)
        rows = self.db_event.load_data(sql_query)
        
        self.events = [str(row[0]) for row in rows]
        self.myUser.update_list(self.events)
    
    def OnMnuUndo(self, event):
        pass
    
    def OnMnuRedo(self, event):
        pass
    
    def OnMnuFilePrint(self, event):
        pass
    
    def OnMnuAddU(self, event):
        select_user = copy.copy(self.current_user)
        dlg = DlgAddUser(self, wx.ID_ANY)
        dlg.ShowModal()
        rep = dlg.getReturnAction()
        
        if rep == wx.ID_OK:
            self.insert_user(dlg.user.to_db())
            self.myUser.update(self.current_user)
        else:
            self.current_user = select_user
    
    def OnMnuDelU(self, event):
        pass
    
    def OnMnuEditU(self, event):
        pass

    def OnNewAction(self, event):
        self._ctrl.setCurrentAction(UI_parameters.ACTIONS[event.GetId()])
        self._fileHandling.setModified(True)
        self._ctrl.updateTitle()
        
    def OnMnuAddEvent(self, event):
        dlg =  DlgImport(self)
        fit_path = os.path.dirname(dlg.GetPath())
        dlg.Destroy()
        if fit_path == None:
            pass # TODO what if nothing selected ?
        else:
            files = os.listdir(fit_path)
            fit_files = [os.path.join(fit_path, file) for file in files if file[-4:].lower()=='.fit']
            
            for file in fit_files:
                self.fit_dict[file] = FitFile_handler(self.parameters, self.logger, file)
                self.fit_dict[file].load_file()
                
    
            for file, handler in self.fit_dict.items():
                handler.parse()  

            for file, handler in self.fit_dict.items():
                for v in handler.data:
                    v['user_id'] = self.current_user.user_id
                    self.db_event.insert_data(v)
                    
        self.refresh_events_list()
                    
    def OnMnuDelEvent(self, event):
        pass
