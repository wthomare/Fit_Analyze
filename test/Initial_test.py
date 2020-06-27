# -*- coding: utf-8 -*-

import FitFile_Handler
import DB_Handler
import unittest
import os

import xml.etree.ElementTree as ET

from Logger import Logger

class Test_process(unittest.TestCase):
    
    def setUp(self):
        
        logger = Logger('test_process')
        logger.add_StreamHandler()
        self.logger = logger.logger
        
        self.parameters =  {}
        tree = ET.parse("parameters.xml")
        root = tree.root()
        for child in root:
            for sub_child in child:
                self.parameters[sub_child.tag] = sub_child.test.encode('utf8')
        
        
        self.fit_files = {}
        self.REPO_DIR = os.getcwd().split("test")

    
    def test_read_files(self):
        files = os.listdir(os.path.join(self.REPO_DIR, 'source_data'))
        fit_files = [os.path.join(self.REPO_DIR, 'source_data', file) for file in files if file[-4:].lower()=='.fit']
        
        for file in fit_files:
            self.fit_files[file] = FitFile_Handler.FitFile_handler(self.parameters, self.logger, file)
            self.fit_files[file].load_file()
            
    def test_parse(self):
        for file, handler in self.fit_files.iteritems():
            handler.parse()
            
    def test_db_handler(self):
        self.db_user = DB_Handler.DB_Handler('users', self.parameters, self.logger)
        self.db_event = DB_Handler.DB_Handler("event", self.parameters, self.logger)
        
    def test_load_data(self):
        for file, handler in self.fit_files.iteritems():
            for k,v in handler.data.iteritems():
                v['user_id'] = 1
                self.db_event.load_data(v)
                
                
if __name__=="__main__":
    unittest.main()