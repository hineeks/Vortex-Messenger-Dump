"""
Data exporters for various formats
"""

import json
import csv
from typing import List, Dict, Optional
from datetime import datetime


class BaseExporter:
    """Base exporter class"""
    
    def export(self, data: List[Dict], output_file: str) -> bool:
        """Export data to file"""
        raise NotImplementedError


class JSONExporter(BaseExporter):
    """Export data to JSON format"""
    
    def export(self, data: List[Dict], output_file: str) -> bool:
        """
        Export to JSON file
        
        Args:
            data: List of messages
            output_file: Output file path
            
        Returns:
            bool: True if successful
        """
        try:
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump({
                    'messages': data,
                    'count': len(data),
                    'exported_at': datetime.now().isoformat()
                }, f, ensure_ascii=False, indent=2)
            return True
        except Exception as e:
            print(f"Error exporting to JSON: {e}")
            return False


class CSVExporter(BaseExporter):
    """Export data to CSV format"""
    
    def export(self, data: List[Dict], output_file: str) -> bool:
        """
        Export to CSV file
        
        Args:
            data: List of messages
            output_file: Output file path
            
        Returns:
            bool: True if successful
        """
        if not data:
            print("No data to export")
            return False
        
        try:
            with open(output_file, 'w', newline='', encoding='utf-8') as f:
                fieldnames = ['timestamp', 'user_id', 'username', 'chat_id', 'content']
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()
                
                for message in data:
                    row = {k: message.get(k, '') for k in fieldnames}
                    writer.writerow(row)
            return True
        except Exception as e:
            print(f"Error exporting to CSV: {e}")
            return False


class HTMLExporter(BaseExporter):
    """Export data to HTML format"""
    
    def export(self, data: List[Dict], output_file: str) -> bool:
        """
        Export to HTML file
        
        Args:
            data: List of messages
            output_file: Output file path
            
        Returns:
            bool: True if successful
        """
        try:
            html = self._generate_html(data)
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(html)
            return True
        except Exception as e:
            print(f"Error exporting to HTML: {e}")
            return False
    
    def _generate_html(self, data: List[Dict]) -> str:
        """Generate HTML content"""
        messages_html = ""
        
        for msg in data:
            timestamp = msg.get('timestamp', 'N/A')
            username = msg.get('username', 'Unknown')
            content = msg.get('content', '')
            
            messages_html += f"""
            <div class="message">
                <div class="message-header">
                    <span class="username">{username}</span>
                    <span class="timestamp">{timestamp}</span>
                </div>
                <div class="message-content">{content}</div>
            </div>
            """
        
        return f"""<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Vortex Messenger Export</title>
    <style>
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            max-width: 900px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f5f5f5;
        }}
        .header {{
            background-color: #2c3e50;
            color: white;
            padding: 20px;
            border-radius: 5px;
            margin-bottom: 20px;
        }}
        .message {{
            background-color: white;
            margin-bottom: 10px;
            padding: 15px;
            border-radius: 5px;
            border-left: 4px solid #3498db;
        }}
        .message-header {{
            display: flex;
            justify-content: space-between;
            margin-bottom: 10px;
            font-size: 12px;
            color: #666;
        }}
        .username {{
            font-weight: bold;
            color: #2c3e50;
        }}
        .message-content {{
            color: #333;
            line-height: 1.5;
        }}
    </style>
</head>
<body>
    <div class="header">
        <h1>🌀 Vortex Messenger Export</h1>
        <p>Экспортировано: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
        <p>Всего сообщений: {len(data)}</p>
    </div>
    {messages_html}
</body>
</html>
"""
