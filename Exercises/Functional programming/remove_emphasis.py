"""
Complete the remove_emphasis, remove_emphasis_from_line, 
and remove_emphasis_from_word functions. They are currently no-ops.

remove_emphasis is the parent function. It takes a full document 
and removes any single or double * characters that are at the start or end of a word. 
(Emphasis in markdown)

For example, this:
I *love* markdown.
I **really love** markdown.

Should become:
I love markdown.
I really love markdown.

Write the helper functions, they will make the remove_emphasis function much easier to write:

The remove_emphasis_from_line function should remove emphasis from a single line of text.
The remove_emphasis_from_word function should remove emphasis from a single word.
Tips
For the sake of practice, try it without the .replace() string method. I used some of these built-ins:

str.split
str.strip
map
join
"""

def remove_emphasis_from_word(word):
    return word.strip("*")


def remove_emphasis_from_line(line):
    words = line.split()
    new_words = map(remove_emphasis_from_word, words)
    return " ".join(new_words)


def remove_emphasis(doc_content):
    lines = doc_content.split("\n")
    new_lines = map(remove_emphasis_from_line, lines)
    return "\n".join(new_lines)


#### Test cases ###


run_cases = [
    (
        "*Don't* panic.\n",
        "Don't panic.\n",
    ),
    (
        "The **answer to the ultimate question** of life, the universe and everything is *42*\n",
        "The answer to the ultimate question of life, the universe and everything is 42\n",
    ),
    (
        "For a moment, *nothing* happened.\nThen, after a second or so, nothing **continued** to happen.\n",
        "For a moment, nothing happened.\nThen, after a second or so, nothing continued to happen.\n",
    ),
]

submit_cases = run_cases + [
    (
        "",
        "",
    ),
    (
        "The Hitchhiker's Guide is a d*mn **useful** book.\n",
        "The Hitchhiker's Guide is a d*mn useful book.\n",
    ),
    (
        "In the beginning the *universe* was created.\nThis has made a lot of people very *angry* and been widely regarded as a bad move.\n",
        "In the beginning the universe was created.\nThis has made a lot of people very angry and been widely regarded as a bad move.\n",
    ),
    (
        "Ford, you're turning into a *penguin*\n",
        "Ford, you're turning into a penguin\n",
    ),
    (
        "*Space* is big.\nYou just won't **believe** how vastly, hugely, mind-bogglingly big it is.\n",
        "Space is big.\nYou just won't believe how vastly, hugely, mind-bogglingly big it is.\n",
    ),
]


def test(input_doc, expected_output):
    print("---------------------------------")
    print(f"Input document:\n{input_doc}")
    print(f"Expected output:\n{expected_output}")
    result = remove_emphasis(input_doc)
    print(f"Actual output:\n{result}")
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
