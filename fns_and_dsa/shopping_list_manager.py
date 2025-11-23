def display_menu():
    """Prints the menu options for the shopping list manager."""
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    """
    Manages the shopping list by continuously displaying a menu and
    handling user input to add, remove, view, and exit.
    """
    # Core Requirement: Your script should start with an empty list
    shopping_list = []

    while True:
        display_menu()
        
        # User Interface Requirement: Use a loop to continuously display a menu
        choice = input("Enter your choice: ")

        if choice == '1':
            # Core Requirement: Implement functionality to add items
            item_to_add = input("Enter the item to add: ").strip()
            if item_to_add:
                shopping_list.append(item_to_add)
                print(f"'{item_to_add}' has been added to the list.")
            else:
                print("Item cannot be empty.")
            
        elif choice == '2':
            # Core Requirement: Implement functionality to remove items
            item_to_remove = input("Enter the item to remove: ").strip()
            if item_to_remove in shopping_list:
                # Remove item from shopping_list
                shopping_list.remove(item_to_remove)
                print(f"'{item_to_remove}' has been removed from the list.")
            else:
                # Requirement: If the item is not found, display a message
                print(f"'{item_to_remove}' was not found in the list.")
            
        elif choice == '3':
            # Core Requirement: Implement functionality to display the current list
            print("\n--- Current Shopping List ---")
            if shopping_list:
                # Requirement: View the list, print each item
                for item in shopping_list:
                    print(f"- {item}")
            else:
                print("The list is currently empty.")
            print("---------------------------")
            
        elif choice == '4':
            # Requirement: The menu should offer an option to exit
            print("Goodbye!")
            break
            
        else:
            # Requirement: Ensure your script handles invalid menu choices gracefully
            print("Invalid choice. Please enter a number from 1 to 4.")

if __name__ == "_main_":
    main()