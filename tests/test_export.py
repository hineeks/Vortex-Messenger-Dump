"""
Tests for export functionality
"""

import unittest
import json
import os
from vortex_dump.exporters import JSONExporter, CSVExporter, HTMLExporter


class TestExporters(unittest.TestCase):
    """Test exporters"""
    
    def setUp(self):
        """Set up test data"""
        self.test_data = [
            {
                'timestamp': '2024-01-01T10:00:00',
                'user_id': 'user1',
                'username': 'Alice',
                'chat_id': 'chat123',
                'content': 'Hello, World!'
            },
            {
                'timestamp': '2024-01-01T10:05:00',
                'user_id': 'user2',
                'username': 'Bob',
                'chat_id': 'chat123',
                'content': 'Hi Alice!'
            }
        ]
    
    def test_json_exporter(self):
        """Test JSON export"""
        exporter = JSONExporter()
        output_file = 'test_export.json'
        
        result = exporter.export(self.test_data, output_file)
        self.assertTrue(result)
        self.assertTrue(os.path.exists(output_file))
        
        with open(output_file, 'r') as f:
            data = json.load(f)
            self.assertEqual(len(data['messages']), 2)
        
        os.remove(output_file)
    
    def test_csv_exporter(self):
        """Test CSV export"""
        exporter = CSVExporter()
        output_file = 'test_export.csv'
        
        result = exporter.export(self.test_data, output_file)
        self.assertTrue(result)
        self.assertTrue(os.path.exists(output_file))
        
        os.remove(output_file)
    
    def test_html_exporter(self):
        """Test HTML export"""
        exporter = HTMLExporter()
        output_file = 'test_export.html'
        
        result = exporter.export(self.test_data, output_file)
        self.assertTrue(result)
        self.assertTrue(os.path.exists(output_file))
        
        os.remove(output_file)


if __name__ == '__main__':
    unittest.main()
