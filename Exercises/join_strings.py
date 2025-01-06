"""
Join Strings
Write a function called join_strings() that takes a list of strings and returns a single string. Concatenate the strings from the list end-to-end, in order, with a comma between them. Don't use the .join() string method.

Example
string_list = ["hello", "my", "friend"]
joined_string = join_strings(string_list)
print(joined_string) # "hello,my,friend"

Tip
You don't want a comma at the beginning or the end of the final string!
"""

def join_strings(string_list):
    
    result = ""
    for i in range(len(string_list)):
        result += string_list[i]
        if i != len(string_list) - 1:
            result += ","
    return result

string_list = ["hello", "my", "friend"]
joined_string = join_strings(string_list)
print(joined_string)  
