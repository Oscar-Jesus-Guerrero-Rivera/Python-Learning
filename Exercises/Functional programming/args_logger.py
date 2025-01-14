def args_logger(*args, **kwargs):
    # Print positional arguments with numbers and periods as prefixes
    for i, arg in enumerate(args, start=1):
        print(f"{i}. {arg}")
    
    # Print keyword arguments sorted alphabetically by key with asterisks and colons
    for key, value in sorted(kwargs.items()):
        print(f"* {key}: {value}")



def test(*args, **kwargs):
    args_logger(*args, **kwargs)
    print("========================================")


def main():
    test("Good", "riddance", date_str="01/01/2023")
    test(message="Hello World", to_delete="l")
    test("two", "star-crossed", "lovers")
    test("hi", True, f_name="Lane", l_name="Wagner", age=28)


main()