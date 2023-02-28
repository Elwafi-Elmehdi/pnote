import unittest
import csv
import os

from pnote import *

class TestPnote(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        self.working_dir = os.path.join('.','./fixtures/')
        self.db_file = os.path.join(working_dir,'testdb.csv')
        load_csv_database(self.working_dir,self.db_file)
    
    @classmethod
    def tearDownClass(cls):
        os.removedirs(self.work)
    
    
    def test_load_csv_database(self):
        self.assert

if __name__ == '__main__':
    unittest.main()
