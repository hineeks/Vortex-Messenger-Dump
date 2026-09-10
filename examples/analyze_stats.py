"""
Example: Analyzing statistics and activity
"""

from vortex_dump import VortexDump


def main():
    dump = VortexDump()
    
    if dump.load_data("data.json"):
        print("🔍 Activity Analysis")
        print("=" * 50)
        
        # Analyze overall statistics
        print("\n📈 Overall Statistics:")
        stats = dump.get_statistics()
        print(f"  Total messages: {stats['total_messages']}")
        print(f"  Unique users: {stats['unique_users']}")
        print(f"  Average per user: {stats['average_messages_per_user']:.2f}")
        
        if stats.get('date_range'):
            print(f"  Date range: {stats['date_range']['start']} to {stats['date_range']['end']}")
        
        # Analyze activity patterns
        print("\n🕐 Activity Patterns:")
        activity = dump.analyze_activity()
        print(f"  Peak hour: {activity.get('peak_hour')}:00")
        print(f"  Most active user: {activity.get('top_user')}")
        
        # Top 5 users
        print("\n👥 Top 5 Most Active Users:")
        for idx, (user, count) in enumerate(stats['top_users'][:5], 1):
            print(f"  {idx}. User {user}: {count} messages")


if __name__ == "__main__":
    main()
