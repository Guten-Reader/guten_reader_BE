import unittest

from project import app
from project.services.clean_text import clean_text

class TestCleanText(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_client()

    def tearDown(self):
        pass

    def test_clean_text(self):
        dirty = 'This text\r\n\r\nis dirty.'
        cleaned = clean_text(dirty)
        expected = 'This text is dirty.'
        self.assertEqual(expected, cleaned)

