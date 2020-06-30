# -*- coding: utf-8 -*-
import wx
from User_profil import User_profil


class UserPanel(wx.Panel):
    [TXT_NAME, TXT_NICKAME, TXT_AGE, TXT_SIZE, TXT_WEIGHT, TXT_FCMIN, 
     TXT_FCMAX, TXT_FTP, BTN_UPDATE, BTN_DELETE, BTN_ADD] = range(11)
    
    def __init__(self, parent, db_user, db_event, event = None, Id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.DefaultSize,
      style=wx.TAB_TRAVERSAL, name=wx.PanelNameStr):
        
        wx.Panel.__init__(self, parent, Id, pos, size, style, name)
         
        self.db_event = db_event
        self.db_user = db_user
        self.load_users()
        self.user = User_profil()
      
        if event:
            self.events = event
        else:
            self.events = []
        
        lblName = wx.StaticText(self, wx.ID_ANY, ("User name"), style=wx.ALIGN_LEFT)
        self._txtName = wx.TextCtrl(self, self.TXT_NAME, value=self.user.name)
        
        lblNickname = wx.StaticText(self, wx.ID_ANY, ("User nickname"), style=wx.ALIGN_LEFT)
        self._txtNickname = wx.TextCtrl(self, self.TXT_NICKAME, value=self.user.nickname)

        lblAge = wx.StaticText(self, wx.ID_ANY, ("User age"), style=wx.ALIGN_LEFT)
        self._txtAge = wx.TextCtrl(self, self.TXT_AGE, value=str(self.user.age))

        lblSize = wx.StaticText(self, wx.ID_ANY, ("User Size"), style=wx.ALIGN_LEFT)
        self._txtSize = wx.TextCtrl(self, self.TXT_SIZE, value=str(self.user.size))

        lblWeight = wx.StaticText(self, wx.ID_ANY, ("User Weight"), style=wx.ALIGN_LEFT)
        self._txtWeight = wx.TextCtrl(self, self.TXT_WEIGHT, value=str(self.user.weight))

        lblFCMin = wx.StaticText(self, wx.ID_ANY, ("FC Minimal"), style=wx.ALIGN_LEFT)
        self._txtFCMin = wx.TextCtrl(self, self.TXT_FCMIN, value=str(self.user.FCMin))

        lblFCMax = wx.StaticText(self, wx.ID_ANY, ("FC Maximal"), style=wx.ALIGN_LEFT)
        self._txtFCMax = wx.TextCtrl(self, self.TXT_FCMAX, value=str(self.user.FCMax))

        lblFTP = wx.StaticText(self, wx.ID_ANY, ("FTP"), style=wx.ALIGN_LEFT)
        self._txtFTP = wx.TextCtrl(self, self.TXT_FTP, value=str(self.user.FTP))


        self.Bind(wx.EVT_TEXT, self._onTxtName, id=self.TXT_NAME)
        self.Bind(wx.EVT_TEXT, self._onTxtNickName, id=self.TXT_NICKAME)
        self.Bind(wx.EVT_TEXT, self._onTxtAge, id=self.TXT_AGE)
        self.Bind(wx.EVT_TEXT, self._onTxtSize, id=self.TXT_SIZE)
        self.Bind(wx.EVT_TEXT, self._onTxtWeight, id=self.TXT_WEIGHT)        
        self.Bind(wx.EVT_TEXT, self._onTxtFCMin, id=self.TXT_FCMIN)        
        self.Bind(wx.EVT_TEXT, self._onTxtFCMax, id=self.TXT_FCMAX)        
        self.Bind(wx.EVT_TEXT, self._onTxtFTP, id=self.TXT_FTP)        
        
        btnUpdate = wx.Button(self, self.BTN_UPDATE, ('&Update profil'))
        btnDelete = wx.Button(self, self.BTN_DELETE, ('&Delete profil'))

        self.Bind(wx.EVT_BUTTON, self._onCmdUpdate, id=self.BTN_UPDATE)
        self.Bind(wx.EVT_BUTTON, self._onCmdDelete, id=self.BTN_DELETE)
        
        self.event_list = wx.ListBox(self, id=wx.ID_ANY, choices = self.events, style=wx.LB_MULTIPLE, size=(120,240))
        self.user_list = wx.ListBox(self, id=wx.ID_ANY, choices = self.users, size=(120,240))


        self.Bind(wx.EVT_LISTBOX, self.onListBox, self.user_list)
        
        szr = wx.BoxSizer(wx.HORIZONTAL)

        # Sizer of the user column
        szr0 = wx.BoxSizer(wx.VERTICAL)
        
        # Sizer for the user parameters
        szr1 = wx.GridSizer(cols = 2, rows=8, hgap=5, vgap=5)
        szr1.AddMany([
                
                (lblName, 0, wx.ALIGN_LEFT),
                (self._txtName, 0, wx.ALIGN_LEFT),
                
                (lblNickname, 0, wx.ALIGN_LEFT),
                (self._txtNickname, 0, wx.ALIGN_LEFT),
                
                (lblAge, 0, wx.ALIGN_LEFT),
                (self._txtAge, 0, wx.ALIGN_LEFT),
                
                (lblSize, 0, wx.ALIGN_LEFT),
                (self._txtSize, 0, wx.ALIGN_LEFT),
                
                (lblWeight, 0, wx.ALIGN_LEFT),
                (self._txtWeight, 0, wx.ALIGN_LEFT),
                
                (lblFCMin, 0, wx.ALIGN_LEFT),
                (self._txtFCMin, 0, wx.ALIGN_LEFT),
                   
                (lblFCMax, 0, wx.ALIGN_LEFT),
                (self._txtFCMax, 0, wx.ALIGN_LEFT),
                   
                (lblFTP, 0, wx.ALIGN_LEFT),
                (self._txtFTP, 0, wx.ALIGN_LEFT),
                                                   
                ])
    
        
        szr.Add(self.user_list, 0, wx.ALL)
        
        # Sizer of the user buttons
        szr2 = wx.BoxSizer(wx.HORIZONTAL)
        szr2.Add(btnUpdate, 0, wx.ALL, 5)
        szr2.Add(btnDelete, 0, wx.ALL, 5)


        szr0.Add(szr1, 0, wx.GROW|wx.ALL, 10)
        szr0.Add(szr2, 0, wx.GROW|wx.ALL, 10)
        
        szr3 = wx.BoxSizer(wx.VERTICAL)
        szr3.Add(self.event_list, 0, wx.ALL)
        
        szrMain = wx.BoxSizer(wx.HORIZONTAL)
        szrMain.Add(szr, 0, wx.GROW|wx.ALL, 10)
        szrMain.Add(szr0, 0, wx.GROW|wx.ALL, 10)
        szrMain.Add(szr3, 0, wx.GROW|wx.ALL, 10)
        
        self.SetSizer(szrMain)
        self.SetAutoLayout(True)
        szrMain.Fit(self)
        
    def _onCmdUpdate(self, event):
        self.user.check()
    
    def _onCmdDelete(self, event):
        pass
           
    
    def _onTxtName(self, event):
        self.user.name = event.GetString().strip()
  
    def _onTxtNickName(self, event):
        self.user.nickname = event.GetString().strip()
        
    def _onTxtAge(self, event):
        self.user.age = event.GetString().strip()

    def _onTxtSize(self, event):
        self.user.size = event.GetString().strip()

    def _onTxtWeight(self, event):
        self.user.weight = event.GetString().strip()

    def _onTxtFCMin(self, event):
        self.user.FCMin = event.GetString().strip()
  
    def _onTxtFCMax(self, event):
        self.user.FCMax = event.GetString().strip()

    def _onTxtFTP(self, event):
        self.user.FTP = event.GetString().strip()

    def update(self):
        self._txtName.SetValue(str(self.user.name))
        self._txtNickname.SetValue(str(self.user.nickname))
        self._txtAge.SetValue(str(self.user.age))
        self._txtSize.SetValue(str(self.user.size))
        self._txtWeight.SetValue(str(self.user.weight))
        self._txtFCMin.SetValue(str(self.user.FCMin))
        self._txtFCMax.SetValue(str(self.user.FCMax))
        self._txtFTP.SetValue(str(self.user.FTP))
        
    def update_list(self, events):
        self.event_list.Clear()
        self.event_list.Append(events)
        
    def onListBox(self, event):
        name, nickname = event.GetEventObject().GetStringSelection().split(" ")
        
        sql_query = "SELECT id, age , weight, size ,FCMin ,FCMax ,FTP FROM users WHERE name LIKE '%{}%' AND nickname LIKE '%{}%'".format(name, nickname)
        
        rows = list(self.db_user.load_data(sql_query)[0])

        rows.insert(0, nickname)
        rows.insert(0, name)
        rows = tuple(rows)
        
        self.user.from_db(rows)
        self.update()
        self.refresh_events_list()
        
    def refresh_events_list(self):
        sql_query = "SELECT DISTINCT event_name FROM event WHERE user_id={}".format(self.user.user_id)
        rows = self.db_event.load_data(sql_query)
        
        self.events = [str(row[0]) for row in rows]
        self.update_list(self.events)
        
    def refresh_user_list(self):
        self.load_users()
        self.user_list.Clear()
        self.user_list.Append(self.users)
        
    def load_users(self):
        sql_query = "SELECT DISTINCT name, nickname FROM users"
        rows = self.db_user.load_data(sql_query)
        
        self.users = [str(row[0]) + ' ' + str(row[1]) for row in rows]
        