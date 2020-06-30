# -*- coding: utf-8 -*-
import wx

class DlgDelUser(wx.Dialog):
    def __init__(self, parent, ID, users):
        wx.Dialog.__init__(self, parent, ID, ("Delete a user"), style = wx.RESIZE_BORDER|wx.CAPTION)
        
        self.users = users
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
        
        
    def onListBox(self, event):
        name, nickname = event.GetEventObject().GetStringSelection().split(" ")
        
        sql_query = "SELECT DISTINCT id FROM users WHERE name LIKE '%{}%' AND nickname LIKE '%{}%'".format(name, nickname)
        
        row = list(self.db_user.load_data(sql_query)[0])
        self.user_id = int(row[0])
        
        
    def _onCmdOk(self, event):
        
        
        
        self._returnAction = wx.ID_OK
        self.Close()
                
    def _onCmdCancel(self, event):
        self._returnAction = wx.ID_CANCEL
        self.Close()
        
    def getReturnAction(self):
        return self._returnAction