import json
import os
from datetime import datetime

class MediaTracker:
    def __init__(self, filename='media_data.json'):
        self.filename = filename
        self.media_list = self.load_data()
    
    def load_data(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                return json.load(f)  # converts json file to python dictionary
        return []
    
    def save_data(self):
        with open(self.filename, 'w') as f:
            json.dump(self.media_list, f, indent=2)  # converts python dictionary to json file
        print('✓ Data successfully saved')
    
    def add_item(self):
        print('\n--- Add New Item ---')
        title = input('Title: ').strip()
        
        print('\nCategories: ')
        categories = ["Book", "Movie", "Show", "Anime", "Webtoon", "Fanfic"]
        for i, cat in enumerate(categories, 1):
            print(f"{i}. {cat}")
        
        cat_choice = input("\nPick a value from the given selections (1-6): ").strip()
        category = categories[int(cat_choice)-1] if cat_choice.isdigit() and 1<=int(cat_choice)<=6 else "Other"
        
        print("\nStatus:")
        statuses = ["plan to watch/read", "watching/reading", "on hold", "dropped", "completed"]
        for i, stat in enumerate(statuses, 1):
            print(f"{i}. {stat}")
        
        stat_choice = input("\nPick a value from the given selections (1-5): ").strip()
        status = statuses[int(stat_choice)-1] if stat_choice.isdigit() and 1<=int(stat_choice)<=5 else "plan to watch/read"
        
        item = {
            "id": len(self.media_list) + 1,
            "title": title,
            "category": category,
            "status": status,
            "rating": None,
            "comment": None,
            "date_added": datetime.now().strftime("%d-%m-%Y"),
            "date_completed": None
        }
        
        self.media_list.append(item)
        self.save_data()
        print(f"\n✓ '{title}' added successfully!")
    
    def view_all(self):
        if not self.media_list:
            print("\nNo items yet. Add some media to track!")
            return
        
        print("\n" + "="*80)
        print("YOUR MEDIA LIST".center(80))
        print("="*80)
        
        for item in self.media_list:
            print(f"\nID: {item['id']} | {item['category']}")
            print(f"Title: {item['title']}")
            print(f"Status: {item['status']}")
            if item['rating']:
                print(f"Rating: {item['rating']}/10")
            if item['comment']:
                print(f"Comment: {item['comment']}")
            print(f"Date Added: {item['date_added']}")
            if item['date_completed']:
                print(f"Date Completed: {item['date_completed']}")
            print("-" * 80)
    
    def view_by_status(self):
        print("\nFilter by status:")
        statuses = ["plan to watch/read", "watching/reading", "on hold", "dropped", "completed"]
        for i, status in enumerate(statuses, 1):
            print(f"{i}. {status}")
        
        choice = input("\nChoose status (1-5): ").strip()
        if not choice.isdigit() or not 1 <= int(choice) <= 5:
            print("Invalid choice!")
            return
        
        selected_status = statuses[int(choice) - 1]
        filtered = [item for item in self.media_list if item['status'] == selected_status]
        
        if not filtered:
            print(f"\nNo items with status '{selected_status}'")
            return
        
        print(f"\n--- {selected_status} ---")
        for item in filtered:
            print(f"\n{item['id']}. {item['title']} ({item['category']})")
            if item['rating']:
                print(f"   Rating: {item['rating']}/10")
    
    def update_item(self):
        """Update an existing item"""
        if not self.media_list:
            print("\nNo items to update!")
            return
        
        self.view_all()
        item_id = input("\nEnter ID of item to update: ").strip()
        
        if not item_id.isdigit():
            print("Invalid ID!")
            return
        
        item_id = int(item_id)
        item = next((i for i in self.media_list if i['id'] == item_id), None)
        
        if not item:
            print("Item not found!")
            return
        
        print(f"\nUpdating: {item['title']}")
        print("1. Update Status")
        print("2. Add/Update Rating")
        print("3. Add/Update Comment")
        print("4. Back")
        
        choice = input("\nChoose option: ").strip()
        
        if choice == '1':
            statuses = ["plan to watch/read", "watching/reading", "on hold", "dropped", "completed"]
            for i, status in enumerate(statuses, 1):
                print(f"{i}. {status}")
            status_choice = input("\nChoose new status (1-5): ").strip()
            if status_choice.isdigit() and 1 <= int(status_choice) <= 5:
                item['status'] = statuses[int(status_choice) - 1]
                if item['status'] == 'completed' and not item['date_completed']:
                    item['date_completed'] = datetime.now().strftime("%d-%m-%Y")
                self.save_data()
                print("✓ Status updated!")
        
        elif choice == '2':
            rating = input("Enter rating (1-10): ").strip()
            if rating.isdigit() and 1 <= int(rating) <= 10:
                item['rating'] = int(rating)
                self.save_data()
                print("✓ Rating updated!")
            else:
                print("Invalid rating! Must be 1-10")
        
        elif choice == '3':
            comment = input("Enter your comment: ").strip()
            item['comment'] = comment
            self.save_data()
            print("✓ Comment updated!")
    
    def delete_item(self):
        """Delete an item"""
        if not self.media_list:
            print("\nNo items to delete!")
            return
        
        self.view_all()
        item_id = input("\nEnter ID of item to delete: ").strip()
        
        if not item_id.isdigit():
            print("Invalid ID!")
            return
        
        item_id = int(item_id)
        item = next((i for i in self.media_list if i['id'] == item_id), None)
        
        if not item:
            print("Item not found!")
            return
        
        confirm = input(f"Delete '{item['title']}'? (yes/no): ").strip().lower()
        if confirm == 'yes':
            self.media_list = [i for i in self.media_list if i['id'] != item_id]
            self.save_data()
            print(f"✓ '{item['title']}' deleted!")
        else:
            print("Deletion cancelled.")
    
    def get_stats(self):
        """Display statistics"""
        if not self.media_list:
            print("\nNo data to show stats!")
            return
        
        total = len(self.media_list)
        completed = len([i for i in self.media_list if i['status'] == 'completed'])
        currently = len([i for i in self.media_list if i['status'] == 'watching/reading'])
        on_hold = len([i for i in self.media_list if i['status'] == 'on hold'])
        dropped = len([i for i in self.media_list if i['status'] == 'dropped'])
        planned = len([i for i in self.media_list if i['status'] == 'plan to watch/read'])
        
        print("\n" + "="*50)
        print("STATISTICS".center(50))
        print("="*50)
        print(f"Total Items: {total}")
        print(f"Completed: {completed}")
        print(f"Currently Watching/Reading: {currently}")
        print(f"On Hold: {on_hold}")
        print(f"Dropped: {dropped}")
        print(f"Plan to Watch/Read: {planned}")
        
        categories = {}
        for item in self.media_list:
            categories[item['category']] = categories.get(item['category'], 0) + 1
        
        print("\nBy Category:")
        for cat, count in categories.items():
            print(f"  {cat}: {count}")
        
        rated_items = [i for i in self.media_list if i['rating']]
        if rated_items:
            avg_rating = sum(i['rating'] for i in rated_items) / len(rated_items)
            print(f"\nAverage Rating: {avg_rating:.1f}/10 ({len(rated_items)} items rated)")


def main():
    tracker = MediaTracker()
    
    while True:
        print("\n" + "="*50)
        print("MEDIA TRACKER".center(50))
        print("="*50)
        print("1. Add New Item")
        print("2. View All Items")
        print("3. View by Status")
        print("4. Update Item")
        print("5. Delete Item")
        print("6. View Statistics")
        print("7. Exit")
        print("="*50)
        
        choice = input("\nChoose an option (1-7): ").strip()
        
        if choice == '1':
            tracker.add_item()
        elif choice == '2':
            tracker.view_all()
        elif choice == '3':
            tracker.view_by_status()
        elif choice == '4':
            tracker.update_item()
        elif choice == '5':
            tracker.delete_item()
        elif choice == '6':
            tracker.get_stats()
        elif choice == '7':
            print("\nThanks for using Media Tracker! Goodbye!")
            break
        else:
            print("\nInvalid option! Please choose 1-7.")


if __name__ == "__main__":
    main()