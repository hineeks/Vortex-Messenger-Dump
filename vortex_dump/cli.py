#!/usr/bin/env python3
"""
CLI tool for Vortex Messenger Dump
Powerful command-line interface for exporting and analyzing messenger data
"""

import argparse
import sys
from datetime import datetime
from vortex_dump import VortexDump


def main():
    parser = argparse.ArgumentParser(
        description='🌀 Vortex Messenger Dump - Export and analyze messenger data',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Examples:
  # Export all messages to JSON
  %(prog)s export --input data.json --chat-id 123456 --format json

  # Analyze statistics
  %(prog)s analyze --input data.json

  # Search for messages
  %(prog)s search --input data.json --query "important" --limit 50

  # Export with date range
  %(prog)s export --input data.json --chat-id 123456 --format html \\
            --start-date 2024-01-01 --end-date 2024-12-31
        '''
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # Export command
    export_parser = subparsers.add_parser('export', help='Export messages from chat')
    export_parser.add_argument('--input', '-i', required=True, help='Input JSON file')
    export_parser.add_argument('--chat-id', required=True, help='Chat ID to export')
    export_parser.add_argument('--format', '-f', choices=['json', 'csv', 'html'], 
                              default='json', help='Export format')
    export_parser.add_argument('--output', '-o', help='Output file path')
    export_parser.add_argument('--start-date', help='Start date (YYYY-MM-DD)')
    export_parser.add_argument('--end-date', help='End date (YYYY-MM-DD)')
    
    # Analyze command
    analyze_parser = subparsers.add_parser('analyze', help='Analyze chat statistics')
    analyze_parser.add_argument('--input', '-i', required=True, help='Input JSON file')
    analyze_parser.add_argument('--chat-id', '-c', help='Specific chat ID (optional)')
    analyze_parser.add_argument('--output', '-o', help='Output file for report')
    
    # Search command
    search_parser = subparsers.add_parser('search', help='Search in messages')
    search_parser.add_argument('--input', '-i', required=True, help='Input JSON file')
    search_parser.add_argument('--query', '-q', required=True, help='Search query')
    search_parser.add_argument('--chat-id', '-c', help='Specific chat ID (optional)')
    search_parser.add_argument('--limit', '-l', type=int, default=100, help='Result limit')
    
    # Info command
    info_parser = subparsers.add_parser('info', help='Show file information')
    info_parser.add_argument('--input', '-i', required=True, help='Input JSON file')
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return
    
    dump = VortexDump()
    
    if args.command != 'info' and not dump.load_data(args.input):
        print("❌ Failed to load data file")
        sys.exit(1)
    
    if args.command == 'export':
        print(f"📥 Exporting messages from chat {args.chat_id}...")
        output_file = args.output or f"export_{datetime.now().strftime('%Y%m%d_%H%M%S')}.{args.format}"
        
        if dump.export_messages(args.chat_id, args.format, output_file, 
                               args.start_date, args.end_date):
            print(f"✅ Export successful! File: {output_file}")
        else:
            print("❌ Export failed")
    
    elif args.command == 'analyze':
        print("📊 Analyzing statistics...")
        stats = dump.get_statistics(args.chat_id)
        
        print("\n" + "="*50)
        print("📈 Statistics")
        print("="*50)
        print(f"Total messages: {stats['total_messages']}")
        print(f"Unique users: {stats['unique_users']}")
        print(f"Avg messages per user: {stats['average_messages_per_user']:.2f}")
        
        if stats.get('date_range'):
            print(f"Date range: {stats['date_range']['start']} → {stats['date_range']['end']}")
        
        print("\n👥 Top 5 Users:")
        for idx, (user, count) in enumerate(stats['top_users'][:5], 1):
            print(f"  {idx}. User {user}: {count} messages")
        
        activity = dump.analyze_activity(args.chat_id)
        print("\n🕐 Activity:")
        print(f"  Peak hour: {activity.get('peak_hour')}:00")
        print(f"  Most active user: {activity.get('top_user')}")
        print(f"  Most active day: {['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'][activity.get('most_active_day', 0)]}")
    
    elif args.command == 'search':
        print(f"🔍 Searching for '{args.query}'...")
        results = dump.search(args.query, args.chat_id, args.limit)
        
        print(f"\n✅ Found {len(results)} results:\n")
        for idx, msg in enumerate(results, 1):
            timestamp = msg.get('timestamp', 'N/A')
            username = msg.get('username', 'Unknown')
            content = msg.get('content', '')[:60]
            
            print(f"{idx}. [{timestamp}] {username}:")
            print(f"   {content}...\n")
    
    elif args.command == 'info':
        print("ℹ️  File Information")
        print("="*50)
        
        if dump.load_data(args.input):
            stats = dump.get_statistics()
            print(f"Total messages: {stats['total_messages']}")
            print(f"Unique users: {stats['unique_users']}")
            print(f"Chats in file: {len(dump.chats)}")
        else:
            print("❌ Could not read file information")


if __name__ == '__main__':
    main()
