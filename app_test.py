import os
import app
import unittest
import tempfile

class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
        app.app.testing = True
        self.app = app.app.test_client()
        
        
    def test_first(self):
        result = self.app.get('/get_all_characters')
    #add assert    
        print(result.data)


if __name__ == '__main__':
    unittest.main()