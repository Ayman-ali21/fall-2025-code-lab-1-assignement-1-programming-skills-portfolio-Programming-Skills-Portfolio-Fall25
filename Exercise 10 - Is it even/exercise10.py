# Function to determine if a number is even or odd
def check_even_odd(number):
    if number % 2 == 0:
        return f"{number} is even."
    else:
        return f"{number} is odd."

# Main function to get user input and display the result
def main():
    try:
        # Ask the user to enter a number
        user_input = int(input("Enter a number: "))
        
        # Call the function and store the result
        result = check_even_odd(user_input)
        
        # Print the result
        print(result)
    except ValueError:
        print("Please enter a valid integer.")

# Run the main function
if __name__ == "__main__":
    main()