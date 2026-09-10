"""
Basic example of using Vortex Dump
"""

from vortex_dump import VortexDump


def main():
    # Create VortexDump instance
    dump = VortexDump()
    
    # Load data from JSON file
    print("Loading data...")
    if dump.load_data("data.json"):
        print("✓ Data loaded successfully")
        
        # Get statistics
        print("\n📊 Statistics:")
        stats = dump.get_statistics()
        print(f"  Total messages: {stats['total_messages']}")
        print(f"  Unique users: {stats['unique_users']}")
        print(f"  Avg messages per user: {stats['average_messages_per_user']:.2f}")
        
        # Export to different formats
        print("\n📥 Exporting...")
        if dump.export_messages("chat_123", format="json", output_file="export.json"):
            print("  ✓ JSON export successful")
        
        if dump.export_messages("chat_123", format="csv", output_file="export.csv"):
            print("  ✓ CSV export successful")
        
        if dump.export_messages("chat_123", format="html", output_file="export.html"):
            print("  ✓ HTML export successful")
    else:
        print("✗ Failed to load data")


if __name__ == "__main__":
    main()
