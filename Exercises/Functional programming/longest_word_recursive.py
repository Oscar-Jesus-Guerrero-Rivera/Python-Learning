def find_longest_word(document, longest_word=""):
    if isinstance(document, str):
        document = document.split(" ")
    if document == []:
        return longest_word
    if len(document[0]) > len(longest_word):
        longest_word = document[0] 
    return find_longest_word(document[1:], longest_word)

run_cases = [
    ("Either that wallpaper goes, or I do.", "wallpaper"),
    (
        "Then I die happy",
        "happy",
    ),
    (
        "Et tu, Brute?",
        "Brute?",
    ),
]

submit_cases = run_cases + [
    (
        "",
        "",
    ),
    (
        " ",
        "",
    ),
    (
        "Let us cross over the river and rest under the shade of the trees",
        "cross",
    ),
]


def test(input1, expected_output):
    print("---------------------------------")
    print(f"Input: '{input1}'")
    print(f"Expecting: '{expected_output}'")
    result = find_longest_word(input1)
    print(f"Actual: '{result}'")
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
