import unittest
import csv
import os

from pnote import *

class TestPnote(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.working_dir = os.path.join('.','./fixtures/')
        cls.db_file = os.path.join(working_dir,'testdb.csv')
        
    
    @classmethod
    def tearDownClass(cls):
        os.removedirs(cls.working_dir)

    def test_load_csv_database(self):
        load_csv_database(self.working_dir,self.db_file)
        
        self.assertTrue(os.path.isdir(self.working_dir),"Must find the working dir.")
        
        self.assertTrue(os.path.isfile(self.db_file),"Must find the csv file.")

        with open(self.db_file,'r') as f:
            lines = f.readlines()
        self.assertIn( 'id,datetime,title,body\n',lines,"Must find the csv headers in csv.")

    def test_generate_note_id(self):
        self.assertEqual(generate_note_id(self.db_file),1,"Must return ID of 1 because csv is empty.")
    
if __name__ == '__main__':
    unittest.main()
