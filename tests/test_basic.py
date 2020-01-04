import os
import unittest

import app

class BasicTests(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        self.app = app.test_client()

    def tearDown(self):
        pass

    def test_main_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
 
 
if __name__ == "__main__":
    unittest.main()