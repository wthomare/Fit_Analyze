# -*- coding: utf-8 -*-

class User_profil(object):
    
    # ------------------------------------------------------------------------
    def __init__(self):
        self.name = ""
        self.nickname = ""
        self.user_id = 1
        self.age = 0
        self.size = 0
        self.weight = 0.0
        self.FCMin = 0
        self.FCMax = 0
        self.FTP = 0
    
    # ------------------------------------------------------------------------
    def check(self):
        assert(isinstance(self.name, str))
        assert(isinstance(self.nickname, str))
        assert(isinstance(self.age, int))
        assert(isinstance(self.size, int))
        assert(isinstance(self.weight, float))
        assert(isinstance(self.FCMin, int))
        assert(isinstance(self.FCMax, int))
        assert(isinstance(self.FTP, int))
        assert(isinstance(self.user_id, int))

        
    # ------------------------------------------------------------------------
    def copy(self, user):
        self.name = user.name
        self.nickname = user.nickname
        self.age = user.age
        self.size = user.size
        self.weight = user.weight
        self.FCMin = user.FCMin
        self.FCMax = user.FCMax
        self.FTP = user.FTP
        self.user_id = user.user_id
        
        self.check()        
        
    # ------------------------------------------------------------------------
    def from_db(self, profil):
        self.name = str(profil[0])
        self.nickname = str(profil[1])
        self.user_id = int(profil[2])
        self.age = int(profil[3])
        self.weight = float(profil[4])
        self.size = int(profil[5])
        self.FCMin = int(profil[6])
        self.FCMax = int(profil[7])
        self.FTP = int(profil[8])
        
        self.check()
        
        
    # ------------------------------------------------------------------------
    def split_profil(self):
        user_id = {
            'name':self.name,
            'nickname':self.nickname,
            }
        
        user_params = {
            'user_id': int(self.user_id),
            'age': int(self.age),
            'weight': float(self.weight),
            'size': int(self.size),
            'FCMin': int(self.FCMin),
            'FCMax': int(self.FCMax),
            'FTP': int(self.FTP)           
            
            }
        return user_id, user_params 
