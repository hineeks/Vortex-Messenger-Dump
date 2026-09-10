"""
Tests for analysis functionality
"""

import unittest
from vortex_dump.analyzers import StatisticsAnalyzer


class TestAnalyzer(unittest.TestCase):
    """Test statistics analyzer"""
    
    def setUp(self):
        """Set up test data"""
        self.analyzer = StatisticsAnalyzer()
        self.test_data = [
            {
                'timestamp': '2024-01-01T10:00:00',
                'user_id': 'user1',
                'content': 'Hello'
            },
            {
                'timestamp': '2024-01-01T10:05:00',
                'user_id': 'user2',
                'content': 'World'
            },
            {
                'timestamp': '2024-01-01T10:10:00',
                'user_id': 'user1',
                'content': 'Test'
            }
        ]
    
    def test_analyze_statistics(self):
        """Test statistics analysis"""
        stats = self.analyzer.analyze(self.test_data)
        
        self.assertEqual(stats['total_messages'], 3)
        self.assertEqual(stats['unique_users'], 2)
        self.assertAlmostEqual(stats['average_messages_per_user'], 1.5)
    
    def test_analyze_activity(self):
        """Test activity analysis"""
        activity = self.analyzer.analyze_activity(self.test_data)
        
        self.assertIn('peak_hour', activity)
        self.assertIn('top_user', activity)
    
    def test_empty_data(self):
        """Test with empty data"""
        stats = self.analyzer.analyze([])
        
        self.assertEqual(stats['total_messages'], 0)
        self.assertEqual(stats['unique_users'], 0)


if __name__ == '__main__':
    unittest.main()
