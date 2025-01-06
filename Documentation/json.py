""" JSON """

"""
Python has a built-in package called `json`, which can be used to work with JSON data.

---

**Importing the `json` Module**

Example:
"""
import json

# Parse JSON - Convert from JSON to Python
"""
If you have a JSON string, you can parse it into a Python dictionary using `json.loads()`.

Example:
"""
x = '{ "name":"John", "age":30, "city":"New York"}'
y = json.loads(x)
print(y["age"])  # Output: 30

# Convert from Python to JSON
"""
You can convert a Python object into a JSON string using `json.dumps()`.

Example:
"""
x = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
y = json.dumps(x)
print(y)  # Output: JSON string representation of the Python dictionary

"""
Python objects that can be converted to JSON include:

- `dict`
- `list`
- `tuple`
- `string`
- `int`
- `float`
- `True`, `False`
- `None`
"""

# Example:
print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

"""
Python to JSON conversion mapping:

| Python      | JSON    |
|-------------|---------|
| dict        | Object  |
| list        | Array   |
| tuple       | Array   |
| str         | String  |
| int/float   | Number  |
| True        | true    |
| False       | false   |
| None        | null    |
"""

# Example:
x = {
    "name": "John",
    "age": 30,
    "married": True,
    "divorced": False,
    "children": ("Ann", "Billy"),
    "pets": None,
    "cars": [
        {"model": "BMW 230", "mpg": 27.5},
        {"model": "Ford Edge", "mpg": 24.1}
    ]
}
print(json.dumps(x))

# Format the Result
"""
The `json.dumps()` method provides options to format the JSON string for readability.

- Use the `indent` parameter to define the number of spaces for indentation.

Example:
"""
print(json.dumps(x, indent=4))

"""
- Use the `separators` parameter to change the default separators. The default is (", ", ": "), 
  which separates keys/values with `: ` and objects with `, `.

Example:
"""
print(json.dumps(x, indent=4, separators=(". ", " = ")))

# Order the Result
"""
The `sort_keys` parameter sorts the keys in the output.

Example:
"""
print(json.dumps(x, indent=4, sort_keys=True))
