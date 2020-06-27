# -*- coding: utf-8 -*-

import sys, os

sys.path.append(os.getcwd().split("test")[0])

import FitFile_Handler
import DB_Handler
import unittest

import xml.etree.ElementTree as ET

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

    def test_basic_process(self):
        files = os.listdir(os.path.join(self.REPO_DIR, 'source_data'))
        fit_files = [os.path.join(self.REPO_DIR, 'source_data', file) for file in files if file[-4:].lower()=='.fit']
        
        for file in fit_files:
            self.fit_files[file] = FitFile_Handler.FitFile_handler(self.parameters, self.logger, file)
            self.fit_files[file].load_file()
            

        for file, handler in self.fit_files.items():
            handler.parse()            

        self.db_user = DB_Handler.DB_Handler('users', self.parameters, self.logger)
        self.db_event = DB_Handler.DB_Handler("event", self.parameters, self.logger)
        for file, handler in self.fit_files.items():
            for v in handler.data:
                v['user_id'] = 1
                self.db_event.insert_data(v)
                
                
if __name__=="__main__":
    unittest.main()
    