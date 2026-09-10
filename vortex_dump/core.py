"""
Core VortexDump class for managing messenger data
"""

import json
from datetime import datetime
from typing import List, Dict, Optional, Any
from .exporters import JSONExporter, CSVExporter, HTMLExporter
from .analyzers import StatisticsAnalyzer


class VortexDump:
    """
    Main class for exporting and analyzing Vortex Messenger data
    """
    
    def __init__(self, token: str = None):
        """
        Initialize VortexDump
        
        Args:
            token: Authentication token for Vortex API
        """
        self.token = token
        self.messages = []
        self.chats = {}
        self.users = {}
        
    def load_data(self, filepath: str) -> bool:
        """
        Load data from JSON file
        
        Args:
            filepath: Path to JSON file with exported data
            
        Returns:
            bool: True if successful
        """
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.messages = data.get('messages', [])
                self.chats = data.get('chats', {})
                self.users = data.get('users', {})
            return True
        except Exception as e:
            print(f"Error loading data: {e}")
            return False
    
    def export_messages(self, chat_id: str, format: str = "json", 
                       output_file: str = None, start_date: str = None,
                       end_date: str = None) -> bool:
        """
        Export messages from specific chat
        
        Args:
            chat_id: ID of the chat
            format: Export format (json, csv, html)
            output_file: Output file path
            start_date: Start date filter (YYYY-MM-DD)
            end_date: End date filter (YYYY-MM-DD)
            
        Returns:
            bool: True if successful
        """
        filtered_messages = self._filter_messages(chat_id, start_date, end_date)
        
        if format == "json":
            exporter = JSONExporter()
        elif format == "csv":
            exporter = CSVExporter()
        elif format == "html":
            exporter = HTMLExporter()
        else:
            print(f"Unknown format: {format}")
            return False
        
        return exporter.export(filtered_messages, output_file or f"export.{format}")
    
    def get_statistics(self, chat_id: str = None) -> Dict[str, Any]:
        """
        Get statistics for chat or all chats
        
        Args:
            chat_id: Optional chat ID
            
        Returns:
            Dictionary with statistics
        """
        analyzer = StatisticsAnalyzer()
        messages = self.messages
        
        if chat_id:
            messages = [m for m in messages if m.get('chat_id') == chat_id]
        
        return analyzer.analyze(messages, self.users)
    
    def search(self, query: str, chat_id: str = None, limit: int = 100) -> List[Dict]:
        """
        Search messages by query
        
        Args:
            query: Search query string
            chat_id: Optional chat ID to limit search
            limit: Maximum results
            
        Returns:
            List of matching messages
        """
        results = []
        query_lower = query.lower()
        
        for message in self.messages:
            if chat_id and message.get('chat_id') != chat_id:
                continue
            
            content = message.get('content', '').lower()
            if query_lower in content:
                results.append(message)
                
            if len(results) >= limit:
                break
        
        return results
    
    def analyze_activity(self, chat_id: str = None) -> Dict[str, Any]:
        """
        Analyze user activity in chat
        
        Args:
            chat_id: Optional chat ID
            
        Returns:
            Dictionary with activity analysis
        """
        analyzer = StatisticsAnalyzer()
        messages = self.messages
        
        if chat_id:
            messages = [m for m in messages if m.get('chat_id') == chat_id]
        
        return analyzer.analyze_activity(messages)
    
    def _filter_messages(self, chat_id: str, start_date: str = None, 
                        end_date: str = None) -> List[Dict]:
        """
        Filter messages by chat and date range
        
        Args:
            chat_id: Chat ID
            start_date: Start date (YYYY-MM-DD)
            end_date: End date (YYYY-MM-DD)
            
        Returns:
            Filtered messages list
        """
        messages = [m for m in self.messages if m.get('chat_id') == chat_id]
        
        if start_date:
            start = datetime.strptime(start_date, "%Y-%m-%d")
            messages = [m for m in messages if datetime.fromisoformat(m.get('timestamp', '')) >= start]
        
        if end_date:
            end = datetime.strptime(end_date, "%Y-%m-%d")
            messages = [m for m in messages if datetime.fromisoformat(m.get('timestamp', '')) <= end]
        
        return messages
