def main():
    path_to_file = "c:/Users/cammy/.vscode/Backend_y_Frontend/Python/Learning_projects/Book_Bot/Books/frankenstein.txt"

    try:
        with open(path_to_file, "r") as f:
            file_contents = f.read()
        return file_contents
    
    except FileNotFoundError:
        print(f"Error: The file '{path_to_file}' was not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
    
def count_words():
    book_text = main()
    if book_text is None:
        print("No text to process. Exiting.")
        return
    
    word_list = book_text.split()
    word_number = len(word_list)
    print(f"The total number of words is: {word_number}")


count_words()
