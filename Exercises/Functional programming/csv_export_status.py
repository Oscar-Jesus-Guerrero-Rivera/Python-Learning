"""
Complete the get_csv_status function. 
It should use a match case statement to select the correct response 
depending on the status of the export operation. 
Create functions to handle each operation as follows:

PENDING:
Return a tuple with the string "Pending..." and the data converted from 
a list of lists of anything, to a list of lists of strings. 
Try to use nested map functions to convert the data items into strings. 
Remember to convert from a map object back into a list.

PROCESSING:
Return a tuple with the string "Processing..." and the data converted 
from a list of lists of strings into one string in CSV format.

For each list of strings, combine the strings with join with commas inbetween to form a row.
For each row string, combine the strings with join with newlines "\n" inbetween to form a table.
SUCCESS:
Return a tuple with the string "Success!" and simply return the data as is.

FAILURE:
Return a tuple with the string "Unknown error, retrying..." and the data after it has been prepared and processed into a CSV string, by combining the steps for Pending and Processing.

Any Other Status:
If the input status is none of the above, raise an Exception with the string "Unknown export status".
"""

from enum import Enum


class CSVExportStatus(Enum):
    PENDING = 1
    PROCESSING = 2
    SUCCESS = 3
    FAILURE = 4


def get_csv_status(status, data):
    match status:
        case CSVExportStatus.PENDING:
            converted_data = [list(map(str, row)) for row in data]
            return "Pending...", converted_data

        case CSVExportStatus.PROCESSING:
            csv_string = "\n".join(",".join(row) for row in data)
            return "Processing...", csv_string

        case CSVExportStatus.SUCCESS:
            return "Success!", data

        case CSVExportStatus.FAILURE:
            converted_data = [list(map(str, row)) for row in data]
            csv_string = "\n".join(",".join(row) for row in converted_data)
            return "Unknown error, retrying...", csv_string

        case _:
            raise Exception("Unknown export status")


try:
    (
        CSVExportStatus.PENDING
        and CSVExportStatus.PROCESSING
        and CSVExportStatus.SUCCESS
        and CSVExportStatus.FAILURE
    )
except Exception as error:
    print(f"Error: Missing attribute {error} from enum")

    class CSVExportStatus(Enum):
        PENDING = None
        PROCESSING = None
        SUCCESS = None
        FAILURE = None


run_cases = [
    (
        CSVExportStatus.PENDING,
        [
            ["Customer ID", "Billed", "Paid"],
            [1, 100, 100],
            [2, 400, 99],
            [3, 50, 25],
        ],
        (
            "Pending...",
            [
                ["Customer ID", "Billed", "Paid"],
                ["1", "100", "100"],
                ["2", "400", "99"],
                ["3", "50", "25"],
            ],
        ),
    ),
    (
        CSVExportStatus.PROCESSING,
        [
            ["Customer ID", "Billed", "Paid"],
            ["1", "100", "100"],
            ["2", "400", "99"],
            ["3", "50", "25"],
        ],
        (
            "Processing...",
            "Customer ID,Billed,Paid\n1,100,100\n2,400,99\n3,50,25",
        ),
    ),
    (
        CSVExportStatus.SUCCESS,
        "Customer ID,Billed,Paid\n1,100,100\n2,400,99\n3,50,25",
        (
            "Success!",
            "Customer ID,Billed,Paid\n1,100,100\n2,400,99\n3,50,25",
        ),
    ),
    (
        CSVExportStatus.FAILURE,
        [
            ["Customer ID", "Billed", "Paid"],
            [1, 100, 100],
            [2, 400, 99],
            [3, 50, 25],
        ],
        (
            "Unknown error, retrying...",
            "Customer ID,Billed,Paid\n1,100,100\n2,400,99\n3,50,25",
        ),
    ),
]

submit_cases = run_cases + [
    (
        CSVExportStatus.PENDING,
        [
            ["Card Name", "Condition", "Value"],
            ["Sparky Mouse", "Fair", 100],
            ["Moist Turtle", "Good", 200],
            ["Burning Lizard", "Very Good", 1000],
            ["Mossy Frog", "Poor", 10],
        ],
        (
            "Pending...",
            [
                ["Card Name", "Condition", "Value"],
                ["Sparky Mouse", "Fair", "100"],
                ["Moist Turtle", "Good", "200"],
                ["Burning Lizard", "Very Good", "1000"],
                ["Mossy Frog", "Poor", "10"],
            ],
        ),
    ),
    (
        CSVExportStatus.PROCESSING,
        [
            ["Card Name", "Condition", "Value"],
            ["Sparky Mouse", "Fair", "100"],
            ["Moist Turtle", "Good", "200"],
            ["Burning Lizard", "Very Good", "1000"],
            ["Mossy Frog", "Poor", "10"],
        ],
        (
            "Processing...",
            "Card Name,Condition,Value\nSparky Mouse,Fair,100\nMoist Turtle,Good,200\nBurning Lizard,Very Good,1000\nMossy Frog,Poor,10",
        ),
    ),
    (
        CSVExportStatus.SUCCESS,
        "Card Name,Condition,Value\nSparky Mouse,Fair,100\nMoist Turtle,Good,200\nBurning Lizard,Very Good,1000\nMossy Frog,Poor,10",
        (
            "Success!",
            "Card Name,Condition,Value\nSparky Mouse,Fair,100\nMoist Turtle,Good,200\nBurning Lizard,Very Good,1000\nMossy Frog,Poor,10",
        ),
    ),
    (
        CSVExportStatus.FAILURE,
        [
            ["Card Name", "Condition", "Value"],
            ["Sparky Mouse", "Fair", 100],
            ["Moist Turtle", "Good", 200],
            ["Burning Lizard", "Very Good", 1000],
            ["Mossy Frog", "Poor", 10],
        ],
        (
            "Unknown error, retrying...",
            "Card Name,Condition,Value\nSparky Mouse,Fair,100\nMoist Turtle,Good,200\nBurning Lizard,Very Good,1000\nMossy Frog,Poor,10",
        ),
    ),
    (1, None, ("Exception Raised:", "Unknown export status")),
]


def test(status, data, expected_output):
    print("---------------------------------")
    print(f"Checking: {status}")
    print("Expected:")
    print(f"{expected_output[0]}")
    print(f"{expected_output[1]}")
    try:
        result = get_csv_status(status, data)
    except Exception as e:
        result = expected_output[0], str(e)
    print("Actual:")
    print(f"{result[0]}")
    print(f"{result[1]}")
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