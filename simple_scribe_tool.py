# String Manupulation

def string_manipulation():
    text = input("Enter your text: ")
    print(f"Original text: {text}")

    # Splitting strings into a list of words
    words = text.split()
    print(f"Words: {words}")

    # Checking if a string starts with a specific sequence
    starts_with = input("Enter a start sequence to check: ")
    print(f"Starts with {starts_with}: {text.startswith(starts_with)}")

    # Checking if a string ends with a specific sequence
    ends_with = input("Enter an end sequence to check: ")
    print(f"Ends with {ends_with}: {text.endswith(ends_with)}")

# Searching and Exracting
    
def search_and_extract():
    text = input("Enter your text for search and extract: ")
    search_query = input("Enter the substring to search: ")
    
    # Searching for a specific substring
    found_index = text.find(search_query)
    if found_index != -1:
        print(f"Substring found at index: {found_index}")
    else:
        print("Substring not found.")

# Formatting and Data Cleaning
    
def format_and_clean():
    text = input("Enter your text to format and clean: ")
    
    # Converting to lower case
    lower_text = text.lower()
    print(f"Lower case: {lower_text}")

    # Converting to upper case
    upper_text = text.upper()
    print(f"Upper case: {upper_text}")

    # Capitalize first letter of each word
    title_text = text.title()
    print(f"Title Case: {title_text}")

# Store Data in a Text File
    
def store_data():
    text = input("Enter your final text to store: ")
    filename = input("Enter the filename to store your data (without extension): ") + ".txt"
    
    try:
        with open(filename, 'w') as file:
            file.write(text)
        print(f"Data successfully stored in {filename}")
    except Exception as e:
        print(f"Error writing to file: {str(e)}")

 
        with open(filename, 'r+') as file:
            file.readline(text)
        print(f"Data Displayed: ")
    

# Main program
        
def simple_scribe():
    while True:
        print("\nSimple Scribe Tool")
        print("1. String Manipulation")
        print("2. Search and Extract")
        print("3. Format and Clean")
        print("4. Store Data in File")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            string_manipulation()
        elif choice == '2':
            search_and_extract()
        elif choice == '3':
            format_and_clean()
        elif choice == '4':
            store_data()
        elif choice == '5':
            print("Exiting Simple Scribe...")
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    simple_scribe()
