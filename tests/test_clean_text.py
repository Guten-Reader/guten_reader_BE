import unittest

from app import app
from services.clean_text import clean_text

class TestCleanText(unittest.TestCase):
    def setUp(self):
        app.config.from_object('config.TestingConfig')
        self.app = app.test_client()

    def test_clean_text(self):
        dirty = 'This text\r\n\r\nis dirty.'
        cleaned = clean_text(dirty)
        expected = 'This text is dirty.'
        self.assertEqual(expected, cleaned)


if __name__ == "__main__":
    unittest.main()
