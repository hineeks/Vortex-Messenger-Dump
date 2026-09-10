"""
Data analysis and statistics
"""

from typing import List, Dict, Any
from collections import Counter
from datetime import datetime


class StatisticsAnalyzer:
    """Analyzer for message statistics and activity"""
    
    def analyze(self, messages: List[Dict], users: Dict = None) -> Dict[str, Any]:
        """
        Analyze messages and return statistics
        
        Args:
            messages: List of message dictionaries
            users: Dictionary of user information
            
        Returns:
            Dictionary with statistics
        """
        if not messages:
            return {
                'total_messages': 0,
                'unique_users': 0,
                'average_messages_per_user': 0,
                'top_users': [],
                'date_range': None
            }
        
        user_counts = Counter(m.get('user_id') for m in messages)
        
        timestamps = [m.get('timestamp') for m in messages if m.get('timestamp')]
        date_range = None
        if timestamps:
            sorted_dates = sorted(timestamps)
            date_range = {
                'start': sorted_dates[0],
                'end': sorted_dates[-1]
            }
        
        return {
            'total_messages': len(messages),
            'unique_users': len(user_counts),
            'average_messages_per_user': len(messages) / len(user_counts) if user_counts else 0,
            'top_users': user_counts.most_common(10),
            'date_range': date_range,
            'user_distribution': dict(user_counts)
        }
    
    def analyze_activity(self, messages: List[Dict]) -> Dict[str, Any]:
        """
        Analyze user activity patterns
        
        Args:
            messages: List of messages
            
        Returns:
            Activity analysis dictionary
        """
        if not messages:
            return {}
        
        hourly_activity = Counter()
        daily_activity = Counter()
        user_activity = Counter()
        
        for msg in messages:
            timestamp_str = msg.get('timestamp', '')
            if not timestamp_str:
                continue
            
            try:
                dt = datetime.fromisoformat(timestamp_str)
                hourly_activity[dt.hour] += 1
                daily_activity[dt.weekday()] += 1
                user_activity[msg.get('user_id')] += 1
            except:
                continue
        
        peak_hour = max(hourly_activity, key=hourly_activity.get) if hourly_activity else None
        top_user = max(user_activity, key=user_activity.get) if user_activity else None
        
        return {
            'peak_hour': peak_hour,
            'hourly_distribution': dict(hourly_activity),
            'daily_distribution': dict(daily_activity),
            'top_user': top_user,
            'user_activity': dict(user_activity),
            'most_active_day': max(daily_activity, key=daily_activity.get) if daily_activity else None
        }
    
    def analyze_content(self, messages: List[Dict]) -> Dict[str, Any]:
        """
        Analyze message content
        
        Args:
            messages: List of messages
            
        Returns:
            Content analysis dictionary
        """
        word_counts = Counter()
        avg_length = 0
        total_length = 0
        
        for msg in messages:
            content = msg.get('content', '')
            total_length += len(content)
            
            words = content.lower().split()
            word_counts.update(words)
        
        if messages:
            avg_length = total_length / len(messages)
        
        return {
            'total_words': len(word_counts),
            'average_message_length': avg_length,
            'most_common_words': word_counts.most_common(20),
            'total_characters': total_length
        }
