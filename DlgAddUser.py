# -*- coding: utf-8 -*-
import wx
from User_profil import User_profil

[TXT_NAME, TXT_NICKAME, TXT_AGE, TXT_SIZE, TXT_WEIGHT, TXT_FCMIN, TXT_FCMAX,
 TXT_FTP] = range(8)

class DlgAddUser(wx.Dialog):
    
    def __init__(self, parent, ID):
    
        wx.Dialog.__init__(self, parent, ID, ("Add a new user"), style = wx.RESIZE_BORDER|wx.CAPTION)
        
        self.user = User_profil()
        self._returnAction = wx.ID_CANCEL
        
        lblName = wx.StaticText(self, wx.ID_ANY, ("User name"), style=wx.ALIGN_LEFT)
        self._txtName = wx.TextCtrl(self, TXT_NAME, value=self.user.name)
        
        lblNickname = wx.StaticText(self, wx.ID_ANY, ("User nickname"), style=wx.ALIGN_LEFT)
        self._txtNickname = wx.TextCtrl(self, TXT_NICKAME, value=self.user.nickname)

        lblAge = wx.StaticText(self, wx.ID_ANY, ("User age"), style=wx.ALIGN_LEFT)
        self._txtAge = wx.TextCtrl(self, TXT_AGE, value=self.user.nickname)

        lblSize = wx.StaticText(self, wx.ID_ANY, ("User Size"), style=wx.ALIGN_LEFT)
        self._txtSize = wx.TextCtrl(self, TXT_SIZE, value=self.user.nickname)

        lblWeight = wx.StaticText(self, wx.ID_ANY, ("User Weight"), style=wx.ALIGN_LEFT)
        self._txtWeight = wx.TextCtrl(self, TXT_WEIGHT, value=self.user.nickname)

        lblFCMin = wx.StaticText(self, wx.ID_ANY, ("FC Minimal"), style=wx.ALIGN_LEFT)
        self._txtFCMin = wx.TextCtrl(self, TXT_FCMIN, value=self.user.nickname)

        lblFCMax = wx.StaticText(self, wx.ID_ANY, ("FC Maximal"), style=wx.ALIGN_LEFT)
        self._txtFCMax = wx.TextCtrl(self, TXT_FCMAX, value=self.user.nickname)

        lblFTP = wx.StaticText(self, wx.ID_ANY, ("FTP"), style=wx.ALIGN_LEFT)
        self._txtFTP = wx.TextCtrl(self, TXT_FTP, value=self.user.nickname)


        self.Bind(wx.EVT_TEXT, self._onTxtName, id=TXT_NAME)
        self.Bind(wx.EVT_TEXT, self._onTxtNickName, id=TXT_NICKAME)
        self.Bind(wx.EVT_TEXT, self._onTxtAge, id=TXT_AGE)
        self.Bind(wx.EVT_TEXT, self._onTxtSize, id=TXT_SIZE)
        self.Bind(wx.EVT_TEXT, self._onTxtWeight, id=TXT_WEIGHT)        
        self.Bind(wx.EVT_TEXT, self._onTxtFCMin, id=TXT_FCMIN)        
        self.Bind(wx.EVT_TEXT, self._onTxtFCMax, id=TXT_FCMAX)        
        self.Bind(wx.EVT_TEXT, self._onTxtFTP, id=TXT_FTP)    
    

        btnOk = wx.Button(self, wx.OK, ('&OK'))
        btnOk.SetDefault()
        btnCancel = wx.Button(self, wx.CANCEL, ('&Cancel'))
       
        self.Bind(wx.EVT_BUTTON, self._onCmdOk, id=wx.OK)
        self.Bind(wx.EVT_BUTTON, self._onCmdCancel, id=wx.CANCEL)

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

        szr2 = wx.BoxSizer(wx.HORIZONTAL)
        szr2.Add(btnOk, 0, wx.ALL, 5)
        szr2.Add(btnCancel, 0, wx.ALL, 5)

        szr3 = wx.BoxSizer(wx.VERTICAL)
        szr3.Add(szr1, 0, wx.GROW|wx.ALL, 10)
        szr3.Add(szr2, 0, wx.GROW|wx.ALL, 10)
            
        self.SetSizer(szr3)
        self.SetAutoLayout(True)
        szr3.Fit(self)
        
    def _onTxtName(self, event):
        self.user.name = event.GetString().strip()
  
    def _onTxtNickName(self, event):
        self.user.nickname = event.GetString().strip()
        
    def _onTxtAge(self, event):
        self.user.age = int(event.GetString().strip())

    def _onTxtSize(self, event):
        self.user.size = int(event.GetString().strip())

    def _onTxtWeight(self, event):
        self.user.weight = float(event.GetString().strip())

    def _onTxtFCMin(self, event):
        self.user.FCMin = int(event.GetString().strip())
  
    def _onTxtFCMax(self, event):
        self.user.FCMax = int(event.GetString().strip())

    def _onTxtFTP(self, event):
        self.user.FTP = int(event.GetString().strip())

    def _onCmdOk(self, event):
        self._returnAction = wx.ID_OK
        self.Close()
                
    def _onCmdCancel(self, event):
        self._returnAction = wx.ID_CANCEL
        self.Close()
        
    def getReturnAction(self):
        return self._returnAction