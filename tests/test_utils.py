"""
Tests for utility functions
"""

import unittest
from vortex_dump.utils import (
    parse_date, clean_text, format_size,
    validate_chat_id, split_into_chunks
)


class TestUtils(unittest.TestCase):
    """Test utility functions"""
    
    def test_parse_date(self):
        """Test date parsing"""
        result = parse_date('2024-01-15')
        self.assertIsNotNone(result)
        self.assertEqual(result.year, 2024)
        self.assertEqual(result.month, 1)
        self.assertEqual(result.day, 15)
    
    def test_clean_text(self):
        """Test text cleaning"""
        text = "  Hello   World  !  "
        result = clean_text(text)
        self.assertEqual(result, "Hello World !")
    
    def test_format_size(self):
        """Test size formatting"""
        result = format_size(1024)
        self.assertIn('KB', result)
    
    def test_validate_chat_id(self):
        """Test chat ID validation"""
        self.assertTrue(validate_chat_id('chat_123'))
        self.assertTrue(validate_chat_id('chat-123'))
        self.assertFalse(validate_chat_id('chat@123'))
    
    def test_split_into_chunks(self):
        """Test data chunking"""
        data = list(range(10))
        chunks = split_into_chunks(data, 3)
        
        self.assertEqual(len(chunks), 4)
        self.assertEqual(len(chunks[0]), 3)
        self.assertEqual(len(chunks[-1]), 1)


if __name__ == '__main__':
    unittest.main()
