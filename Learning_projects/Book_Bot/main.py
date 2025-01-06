def main():
    # Path to the book file
    path_to_file = "c:/Users/cammy/.vscode/Backend_y_Frontend/Python/Learning_projects/Book_Bot/Books/frankenstein.txt"

    try: 
        # Attempts to open the book file. If the path and extension exist, it reads all 
        # the text from the book and stores it in the variable 'file_contents'.
        with open(path_to_file, "r") as f:
            file_contents = f.read()
        return file_contents  # Returns a string containing all the words in the book
    
    # Handles errors
    except FileNotFoundError:
        print(f"Error: The file '{path_to_file}' was not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def count_words(): 
    # Gets the book text using the main method
    book_text = main()

    # If the variable is None, it means an error occurred, so the program will stop
    if book_text is None:
        print("No text to process. Exiting.")
        return
    
    # Splits the text whenever there is a space, turning it into a list of words
    word_list = book_text.split()
    word_number = len(word_list)  # The number of words is equal to the length of the word list
    print(f"The total number of words is: {word_number}")  # Prints the total word count

def count_characters():
    # Gets the book text using the main method
    book_text = main()

    # If the variable is None, it means an error occurred, so the program will stop
    if book_text is None:
        print("No text to process. Exiting.")
        return

    # Converts all letters to lowercase to standardize them within the same 
    # ASCII value range (97 = 'a' to 123 = 'z')
    lower_text = book_text.lower()

    # Initializes a dictionary with every letter in the alphabet and sets its count to zero
    counted_chars = {chr(i): 0 for i in range(97, 123)}
    
    # Loops through each lowercase character in the text
    for x in lower_text:
        if x.isalpha():  # Processes only alphabetic characters
            counted_chars[x] += 1  # If the character is a letter, increment its count by one
    
    # Converts the dictionary into a list of dictionaries
    char_list = [{"char": char, "count": count} for char, count in counted_chars.items()]
    
    # Sorts the list of characters by their count in descending order
    char_list.sort(key=lambda d: d["count"], reverse=True)
    
    # Prints the sorted list of characters by frequency
    print("Characters sorted by frequency:")
    for item in char_list:
        print(f"{item['char']} appeared: {item['count']} times")
    return char_list

# Invokes the methods
count_words()
count_characters()
