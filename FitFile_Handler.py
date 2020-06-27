# -*- coding: utf-8 -*-

import fitparse
import pytz
import csv
import os
import datetime


# ----------------------------------------------------------------------------
class FitFile_handler(object):
    """
    This class is build to manage all the operations possible with a .fit file
        - load a file
        - parse a file
        - send a data to the db
    """
    UTC = pytz.UTC
    CST = pytz.timezone('US/Central')
    
    # ------------------------------------------------------------------------
    def __init__(self, parameters, logger, file):
        
        self.parameters = parameters
        self.logger = logger
        self.file = file
        self.filename = self.file[:-4].split(os.sep)[-1]
        
        self.allowed_fields = ['timestamp','position_lat','position_long',
                          'enhanced_altitude', 'altitude','enhanced_speed',
                          'speed', 'heart_rate','cadence','fractional_cadence', 'power']
        self.required_fields = ['timestamp', 'position_lat', 'position_long', 'altitude']
        
    # ------------------------------------------------------------------------
    def load_file(self):
        self.fitfile = fitparse.FitFile(self.file, data_processor=fitparse.StandardUnitsDataProcessor())
        
    # ------------------------------------------------------------------------
    def parse(self):
        messages = self.fitfile.messages
        self.data = []
        for m in messages:
            skip=False
            if not hasattr(m, 'fields'):
                continue
            fields = m.fields
            #check for important data types
            mdata = {}
            for field in fields:
                if field.name in self.allowed_fields:
                    mdata[field.name] = field.value
            mdata['event_name'] = self.filename
            for rf in self.required_fields:
                if rf not in mdata:
                    skip=True
            if not skip:
                self.data.append(mdata)
                
    # ------------------------------------------------------------------------
    def to_csv(self):
        """
        Legacy function
        """

        with open(self.filename + '.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerow(self.allowed_fields)
            for entry in self.data:
                writer.writerow([ str(entry.get(k, '')) for k in self.allowed_fields])
        self.logger.debug('wrote %s' % (self.filename + '.csv'))
        

        
        

        
    