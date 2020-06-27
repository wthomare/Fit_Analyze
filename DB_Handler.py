# -*- coding: utf-8 -*-

from urllib.request import pathname2url
import sqlite3

# ----------------------------------------------------------------------------
class DB_Handler(object):
    
    # ------------------------------------------------------------------------
    def __init__(self, db,  parameters, logger):
        self.db = db
        self.parameters = parameters
        self.logger = logger
        

        if not self.check_db():
            self.logger.warning("The DB [%s] not found. We will create it" %(self.db))
            self.create_db()
            if self.check_db():
                self.logger.info("The DB [%s] is created succesfully" %(self.db))
            else:
                raise sqlite3.OperationalError("Failed to create the db [%s] at first attempt" %self.db)        
        
    # ------------------------------------------------------------------------
    def check_db(self):
        try:
            dburi = 'file:{}?mode=rw'.format(pathname2url(self.db))
            self.conn = sqlite3.connect(dburi, uri=True)
            self.cursor = self.conn.cursor()
            self.logger.info("Found DB [%s]" %self.db)
            return True
        except sqlite3.OperationalError:
            return False
                                
    # ------------------------------------------------------------------------
    def create_db(self):
        
        if 'user' in self.db:
            sql_query = """
                        CREATE TABLE IF NOT EXISTS users(
                             id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
                             name TEXT,
                             age INTEGER,
                             weight FLOAT,
                             size INTEGER
                        )
                        """
        elif 'event' in self.db:
            sql_query = """
                        CREATE TABLE IF NOT EXISTS event(
                             id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
                             user_id INTEGER,
                             timestamp DATETIME,
                             position_lat FLOAT,
                             position_long FLOAT,
                             distance FLOAT,
                             enhanced_altitude FLOAT,
                             altitude FLOAT,
                             enhanced_speed FLOAT,
                             speed FLOAT,
                             heart_rate INTEGER,
                             cadence INTEGER,
                             fractional_cadence INTEGER
                        )            
            
                        """
        else:
            raise ValueError('The database [%s] is unknown in this project' %self.db)
        
        self.conn = sqlite3.connect(self.db)
        self.cursor = self.conn.cursor()
        self.logger.warning("Execute the query : [%s]" %sql_query)
        self.cursor.execute(sql_query)
        self.conn.commit()
        
    # ------------------------------------------------------------------------
    def delete_db(self):
        self.logger.warning("Delete the database : [%s]" %self.db)
        sql_query = """
                    DROP TABLE %s
                    """%self.db
        self.cursor.execute(sql_query)
        self.conn.commit()
        if not self.check_db():
            self.logger.warning("The database [%s] was deleted with success" %self.db)
        
    # ------------------------------------------------------------------------
    def insert_data(self, data:dict,):
        """
        Insert data into db, assert that data is a dictionnary
        """
        
        assert(isinstance(data, dict))
        field, value = "", ""
        for key in data.keys():
            field += key + ', '
            value += ':' + key + ', '
            
        field = field[:-2]
        value = value[:-2]
        
        sql_query = """INSERT INTO %s(%s) VALUES(%s)"""%(self.db, field, value)
        self.cursor.execute(sql_query, data)
        
    # ------------------------------------------------------------------------
    def load_data(self, sql_query):
        """
        This feature is to complex. You have to write your own query before executing it
        return rows of Xuple
        """
        self.cursor.execute(sql_query)
        rows = self.cursor.fetchall()
        self.logger.debug("Extract from [%s] %s Xuple" %(self.db, len(rows)))
        return rows
        
    # ------------------------------------------------------------------------
    def modify_data(self, sql_query):
        # cursor.execute("""UPDATE users SET age = ? WHERE id = 2""", (31,))
        
        self.cursor.execute(sql_query)
        
    # ------------------------------------------------------------------------
    def off(self):
        self.conn.close()