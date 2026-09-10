"""
Example: Searching messages
"""

from vortex_dump import VortexDump


def main():
    dump = VortexDump()
    
    if dump.load_data("data.json"):
        # Search for specific keyword
        print("🔎 Message Search")
        print("=" * 50)
        
        query = "important"
        print(f"\nSearching for: '{query}'")
        
        results = dump.search(query, limit=20)
        
        print(f"\nFound {len(results)} messages:\n")
        
        for idx, msg in enumerate(results, 1):
            timestamp = msg.get('timestamp', 'N/A')
            username = msg.get('username', 'Unknown')
            content = msg.get('content', '')
            
            print(f"{idx}. [{timestamp}] {username}:")
            print(f"   {content}\n")


if __name__ == "__main__":
    main()
