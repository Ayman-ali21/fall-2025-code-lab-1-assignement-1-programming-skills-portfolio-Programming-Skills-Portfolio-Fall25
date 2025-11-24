# Initialize the list of names
names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

# Ask the user to input the name they want to search for
search_name = input("Enter the name you want to search for: ")

# Check if the entered name is in the list (case-sensitive)
if search_name in names:
    print(f"{search_name} was found in the list!")
else:
    print(f"{search_name} was not found in the list.")