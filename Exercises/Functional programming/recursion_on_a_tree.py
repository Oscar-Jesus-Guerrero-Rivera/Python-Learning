def list_files(parent_directory, current_filepath=""):
    file_list = []
    
    for key, value in parent_directory.items():
        new_path = f"{current_filepath}/{key}"
        
        if value is None: 
            file_list.append(new_path)
        else:  
            file_list.extend(list_files(value, new_path))
    
    return file_list


run_cases = [
    (
        {
            "Documents": {
                "Proposal.docx": None,
                "Report": {"AnnualReport.pdf": None, "Financials.xlsx": None},
            },
            "Downloads": {"picture1.jpg": None, "picture2.jpg": None},
        },
        [
            "/Documents/Proposal.docx",
            "/Documents/Report/AnnualReport.pdf",
            "/Documents/Report/Financials.xlsx",
            "/Downloads/picture1.jpg",
            "/Downloads/picture2.jpg",
        ],
    )
]

submit_cases = run_cases + [
    ({}, []),
    (
        {
            "Work": {
                "ProjectA": {
                    "Documentation": {"README.md": None, "GUIDE.md": None},
                    "Source": {"main.py": None, "util.py": None},
                },
                "ProjectB": {"Presentation.pptx": None},
            }
        },
        [
            "/Work/ProjectA/Documentation/GUIDE.md",
            "/Work/ProjectA/Documentation/README.md",
            "/Work/ProjectA/Source/main.py",
            "/Work/ProjectA/Source/util.py",
            "/Work/ProjectB/Presentation.pptx",
        ],
    ),
    (
        {
            "Music": {
                "Pop": {"song1.mp3": None},
                "Classical": {"Beethoven": {"symphony9.mp3": None}},
            }
        },
        ["/Music/Classical/Beethoven/symphony9.mp3", "/Music/Pop/song1.mp3"],
    ),
]


def test(input1, expected_output):
    print("---------------------------------")
    print(f"Input: {input1}")
    print(f"Expecting:")
    for output in expected_output:
        print(f"    {output}")
    try:
        result = sorted(list_files(input1))
        print(f"Actual:")
        for res in result:
            print(f"    {res}")
    except Exception as e:
        result = e
        print(f"Error: {e}")
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
