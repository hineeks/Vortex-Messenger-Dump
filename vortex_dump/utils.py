"""
Utility functions for Vortex Dump
"""

import re
from datetime import datetime
from typing import List, Dict, Optional


def parse_date(date_string: str) -> Optional[datetime]:
    """
    Parse date string in various formats
    
    Args:
        date_string: Date string
        
    Returns:
        datetime object or None
    """
    formats = [
        "%Y-%m-%d",
        "%Y-%m-%d %H:%M:%S",
        "%d.%m.%Y",
        "%d.%m.%Y %H:%M:%S"
    ]
    
    for fmt in formats:
        try:
            return datetime.strptime(date_string, fmt)
        except ValueError:
            continue
    
    return None


def clean_text(text: str) -> str:
    """
    Clean and normalize text
    
    Args:
        text: Raw text
        
    Returns:
        Cleaned text
    """
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    # Remove special characters but keep basic punctuation
    text = re.sub(r'[^\w\s\.\,\!\?\-]', '', text)
    return text


def format_size(bytes: int) -> str:
    """
    Format byte size to human readable format
    
    Args:
        bytes: Size in bytes
        
    Returns:
        Formatted string
    """
    for unit in ['B', 'KB', 'MB', 'GB']:
        if bytes < 1024:
            return f"{bytes:.2f} {unit}"
        bytes /= 1024
    return f"{bytes:.2f} TB"


def validate_chat_id(chat_id: str) -> bool:
    """
    Validate chat ID format
    
    Args:
        chat_id: Chat ID to validate
        
    Returns:
        True if valid
    """
    return bool(re.match(r'^[a-zA-Z0-9_-]+$', chat_id))


def split_into_chunks(data: List, chunk_size: int) -> List[List]:
    """
    Split list into chunks
    
    Args:
        data: List to split
        chunk_size: Size of each chunk
        
    Returns:
        List of chunks
    """
    return [data[i:i + chunk_size] for i in range(0, len(data), chunk_size)]
