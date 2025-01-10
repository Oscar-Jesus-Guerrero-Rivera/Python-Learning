def file_type_getter(file_extension_tuples):
    
    # Initialize an empty dictionary to store the mapping of file extensions to file types
    file_ext_dict = {}
    
    # Iterate through each tuple in the input list
    for file_type, ext in file_extension_tuples:
        # For each file type, iterate through the list of associated extensions
        for x in ext:
            # Map each extension to its corresponding file type
            file_ext_dict[x] = file_type

    # Return a lambda function that fetches the file type for a given extension
    # If the extension is not found, it returns "Unknown"
    return lambda x: file_ext_dict.get(x, "Unknown")



### Test Cases


run_cases = [
    (
        [("document", [".doc", ".docx"]), ("image", [".jpg", ".png"])],
        ".doc",
        "document",
    ),
    (
        [("document", [".doc", ".docx"]), ("image", [".jpg", ".png"])],
        ".png",
        "image",
    ),
]

submit_cases = run_cases + [
    (
        [("document", [".doc", ".docx"]), ("image", [".jpg", ".png"])],
        ".txt",
        "Unknown",
    ),
    (
        [("code", [".py", ".js"]), ("markup", [".html", ".xml"])],
        ".js",
        "code",
    ),
]


def test(file_extension_tuples, ext, expected_output):
    try:
        print("---------------------------------")
        print("Input tuples:")
        for file_type, exts in file_extension_tuples:
            print(f"  {file_type}: {exts}")
        print(f"Extension: {ext}")
        print(f"Expecting: {expected_output}")
        getter_function = file_type_getter(file_extension_tuples)
        result = getter_function(ext)
        print(f"Actual: {result}")
        if result == expected_output:
            print("Pass")
            return True
        print("Fail")
        return False
    except Exception as e:
        print("Fail")
        print(e)
        return False


def main():
    passed = 0
    failed = 0
    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            passed += 1
        else:
            failed += 1
    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    print(f"{passed} passed, {failed} failed")


test_cases = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()
