# I- Create your database of contacts
def create_contact_list():
    """
    Prompts the user to enter contact names and phone numbers (use a while loop), 
    stores them in two lists, and returns them.
    The user can enter multiple contacts and signal completion by typing '!done'.
    
    Returns:
        Tuple of two lists - 'contacts' containing the names and 'phone_nb' 
        containing the phone numbers.
    """
    ...
    
# II- Display all the names in the list
def display_names(contacts):
    """
    Prints out each name from the contacts list.
    
    Args:
        contacts: List of contact names.
    """
    ...
    
# III- Find a number given a name
def search_number(contacts, numbers, name):
    """
    Searches for a name in the contacts list and 
    prints the associated phone number.
    
    Args:
        contacts: List of contact names.
        numbers: List of contact phone numbers, parallel to contacts.
        name: The name to search for within the contacts list.
    """
    ...
     
# IV- Main function
def main():
    """
    The main function to run the contact list application.
    It allows the creation of the contact list, displays all names, 
    and provides a search feature to find a phone number by name.
    """
    # Task 1. Create contacts
    ...
    # Task 2. Display all the names
    ...
    # Task 3. Find a number given a name
    ...
    
# Execute the main function
main()
