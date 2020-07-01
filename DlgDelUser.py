# -*- coding: utf-8 -*-
import wx

class DlgDelUser(wx.Dialog):
    def __init__(self, parent, ID, users, db_user, db_params, db_event):
        wx.Dialog.__init__(self, parent, ID, ("Delete a user"), style = wx.RESIZE_BORDER|wx.CAPTION)
        self.name, self.nickname, self.user_id = None, None, None
        self.users = users
        self.db_user = db_user
        self.db_params = db_params
        self.db_event = db_event
        
        self._returnAction = wx.ID_CANCEL

        self.user_list = wx.ListBox(self, id=wx.ID_ANY, choices = self.users, size=(120,240))
        self.Bind(wx.EVT_LISTBOX, self.onListBox, self.user_list)
        
        
        btnOk = wx.Button(self, wx.OK, ('&OK'))
        btnOk.SetDefault()
        btnCancel = wx.Button(self, wx.CANCEL, ('&Cancel'))
       
        self.Bind(wx.EVT_BUTTON, self._onCmdOk, id=wx.OK)
        self.Bind(wx.EVT_BUTTON, self._onCmdCancel, id=wx.CANCEL)
        
        
        szr1 = wx.BoxSizer(wx.VERTICAL)
        szr1.Add(self.user_list, 0, wx.GROW|wx.ALL, 10)
        
        szr2 = wx.BoxSizer(wx.HORIZONTAL)
        szr2.Add(btnOk, 0, wx.ALL, 5)
        szr2.Add(btnCancel, 0, wx.ALL, 5)
        
        szr3 = wx.BoxSizer(wx.VERTICAL)
        szr3.Add(szr1, 0, wx.GROW|wx.ALL, 10)
        szr3.Add(szr2, 0, wx.GROW|wx.ALL, 10)

        self.SetSizer(szr3)
        self.SetAutoLayout(True)
        szr3.Fit(self)
        
    def onListBox(self, event):
        self.name, self.nickname = event.GetEventObject().GetStringSelection().split(" ")
        
        sql_query = "SELECT DISTINCT id FROM users WHERE name LIKE '%{}%' AND nickname LIKE '%{}%'".format(self.name, self.nickname)
        
        row = list(self.db_user.load_data(sql_query)[0])
        self.user_id = int(row[0])
        
        
    def _onCmdOk(self, event):
        
        if self.user_id is not None:
            dlg = wx.MessageDialog(None, "Do you want to  delete the user : [%s %s] (profil and races) ?"%(self.name, self.nickname)
                                   ,'Deleter',wx.YES_NO | wx.ICON_QUESTION)
            result = dlg.ShowModal()
            
            if result == wx.ID_YES:
                self.delete_user()
        
        
        self._returnAction = wx.ID_OK
        self.Close()
                
    def delete_user(self):
        self.db_user.delete_data(self.user_id)
        
        sql_query = "SELECT id FROM parameters WHERE user_id=%s"%self.user_id
        rows = self.db_params.load_data(sql_query)[0]
        
        for row in rows:
            self.db_params.delete_data(row)
            
        sql_query = "SELECT id FROM event WHERE user_id=%s"%self.user_id
        rows = self.db_event.load_data(sql_query)
        if rows:
            rows = rows[0]
        
        for row in rows:
            self.db_event.delete_data(row)
        
    def _onCmdCancel(self, event):
        self._returnAction = wx.ID_CANCEL
        self.Close()
        
    def getReturnAction(self):
        return self._returnAction