# -*- coding: utf-8 -*-

import os
import wx
import datetime
import wx.ribbon as RB

import UI_parameters
import images

from Utils import CreateBitmap
from Project_Frame import Project_frame
from Logger import Logger
from DB_Handler import DB_Handler
from User_profil import User_profil
from FitFile_Handler import FitFile_handler

from DlgAddUser import DlgAddUser
from DlgDelUser import DlgDelUser
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
        self.db_params = DB_Handler('parameters', self.parameters, self.logger)
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
        
        self.myUser = Project_frame(panel, db_user=self.db_user, db_event=self.db_event, db_params=self.db_params)
        s.Add(self._ribbon, 0, wx.EXPAND)
        s.Add(self.myUser, 1, wx.EXPAND)
        
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
    
    def insert_user(self, user_profil):
        user_id, user_param = user_profil.split_profil()
        print("user_id %s" %user_id)
        print("user_param %s" %user_param)
        self.db_user.insert_data(user_id)
        
        sql_query = "SELECT id FROM users WHERE name LIKE '%{}%' AND nickname LIKE '%{}%'".format(user_id['name'], user_id['nickname'])
        
        rows = self.db_user.load_data(sql_query)[0]
        print("rows %s" %rows)
        user_param['user_id'] = rows[0]
        user_param['timestamp'] = datetime.datetime.now()
        print("user_param complete %s" %user_param)
        self.db_params.insert_data(user_param)
        
    def OnMnuUndo(self, event):
        pass
    
    def OnMnuRedo(self, event):
        pass
    
    def OnMnuFilePrint(self, event):
        pass
    
    def OnMnuAddU(self, event):
        dlg = DlgAddUser(self, wx.ID_ANY)
        dlg.ShowModal()
        rep = dlg.getReturnAction()
        
        if rep == wx.ID_OK:
            self.insert_user(dlg.user)
            self.myUser.user_tab.refresh_user_list()
            self.myUser.user_tab.update(dlg.user)
            self.myUser.user_tab.refresh_events_list()

    def OnMnuDelU(self, event):
        dlg = DlgDelUser(self, wx.ID_ANY, users=self.myUser.user_tab.users, db_user=self.db_user, db_params=self.db_params, db_event=self.db_event)
        dlg.ShowModal()
        rep = dlg.getReturnAction()
        
        if rep == wx.ID_OK:
            self.myUser.user_tab.refresh_user_list()
            self.myUser.user_tab.refresh_events_list()
    
    def OnMnuEditU(self, event):
        pass

        
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
                    v['user_id'] = self.myUser.user_tab.user.user_id
                    self.db_event.insert_data(v)
                    
        self.myUser.user_tab.refresh_events_list()
                    
    def OnMnuDelEvent(self, event):
        pass

    def Close(self, force=False):

        self.db_params.off()
        self.db_event.off()
        self.db_user.off()
        self.Destroy()