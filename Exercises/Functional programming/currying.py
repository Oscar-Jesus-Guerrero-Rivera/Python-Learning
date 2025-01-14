"""
Fix the converted_font_size function. 
We are using a 3rd party code library that expects our function to be a curried series 
of functions that each take a single argument.

converted_font_size should just take a single argument, 
font_size and return a function that takes a single argument, doc_type. 
That function should return the font_size multiplied by the appropriate value for the given 
doc_type.
"""

def converted_font_size(font_size):
    def aux (doc_type):
        if doc_type == "txt":
            return font_size
        if doc_type == "md":
            return font_size * 2
        if doc_type == "docx":
            return font_size * 3
        raise ValueError("Invalid doc type")
    return aux



run_cases = [
    (12, "txt", 12),
    (16, "md", 32),
]

submit_cases = run_cases + [
    (14, "html", "Invalid doc type"),
    (0, "txt", 0),
    (50, "md", 100),
]


def test(input1, input2, expected_output):
    print("---------------------------------")
    print(f"Inputs:")
    print(f" * font_size: {input1}")
    print(f" * doc_type: {input2}")
    print(f"Expecting: {expected_output}")
    try:
        result = converted_font_size(input1)(input2)
    except Exception as error:
        result = str(error)
    print(f"Actual: {result}")
    if result == expected_output:
        print("Pass")
        return True
    print("Fail")
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
