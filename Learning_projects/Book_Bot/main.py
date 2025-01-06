def main():
    path_to_file = "Books/frankenstein.txt"

    try:
        with open(path_to_file) as f:
            file_contents = f.read()
        print(file_contents)

    except FileNotFoundError:
        print(f"Error: The file '{path_to_file}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}") 