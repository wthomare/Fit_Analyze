# -*- coding: utf-8 -*-

import sys, os
import time

sys.path.append(os.getcwd().split("test")[0])

import FitFile_Handler
import DB_Handler
import Graphic_store

import unittest

import xml.etree.ElementTree as ET
import numpy as np

from Logger import Logger

class Test_process(unittest.TestCase):
    
    def setUp(self):
        
        logger = Logger('test_process')
        logger.add_StreamHandler()
        logger.add_FileHandler('Initial_test.log')
        self.logger = logger.logger
        
        self.parameters =  {}
        tree = ET.parse("parameters.xml")
        root = tree.getroot()
        for child in root:
            for sub_child in child:
                self.parameters[sub_child.tag] = sub_child.test.encode('utf8')
        
        
        self.REPO_DIR = os.getcwd().split("test")[0]
        self.parameters["REPO_DIR"] = self.REPO_DIR
        self.fit_files = {}
        self.graphic = Graphic_store.Graphic_store(self.parameters, self.logger)

    def test_basic_process(self):
        files = os.listdir(os.path.join(self.REPO_DIR, 'source_data'))
        fit_files = [os.path.join(self.REPO_DIR, 'source_data', file) for file in files if file[-4:].lower()=='.fit']
        
        for file in fit_files:
            self.fit_files[file] = FitFile_Handler.FitFile_handler(self.parameters, self.logger, file)
            self.fit_files[file].load_file()
            

        for file, handler in self.fit_files.items():
            handler.parse()            
        # Create db
        self.db_user = DB_Handler.DB_Handler('users', self.parameters, self.logger)
        self.db_event = DB_Handler.DB_Handler("event", self.parameters, self.logger)
        
        # Insert data into db
        for file, handler in self.fit_files.items():
            for v in handler.data:
                v['user_id'] = 1
                self.db_event.insert_data(v)
             
        # Reload those data from db
        sql_query = "SELECT position_lat, position_long, power FROM event WHERE user_id=1"
        rows = self.db_event.load_data(sql_query)

        longitude, latitude, power = np.array([]), np.array([]), np.array([])
        for row in rows:
            longitude = np.append(longitude, row[0])
            latitude = np.append(latitude, row[1])
            power = np.append(power, row[2])
        
        print(len(longitude))    
        print(len(latitude))    
        print(len(power))
        print(power.max())
        
        self.graphic.draw_2D_enriched('test_power.jpeg', latitude, longitude, power)

        self.db_user.off()
        self.db_event.off()
        
        
if __name__=="__main__":
    unittest.main()
    