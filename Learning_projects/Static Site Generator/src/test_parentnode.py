import unittest

from parentnode import *

class TestParentNode(unittest.TestCase):
    def run_tests():
        node = ParentNode(tag="div", children=[])
        assert node.to_html() == "<div></div>", "Test 1 failed"

        node = ParentNode(tag="div", children=["Hello, World!"])
        assert node.to_html() == "<div>Hello, World!</div>", "Test 2 failed"

        node = ParentNode(tag="div", children=["Hello", " ", "World!"])
        assert node.to_html() == "<div>Hello World!</div>", "Test 3 failed"

        node = ParentNode(tag="div", children=[
            ParentNode(tag="p", children=["This is a paragraph."]),
            ParentNode(tag="p", children=["This is another paragraph."])
        ])
        expected_html = "<div><p>This is a paragraph.</p><p>This is another paragraph.</p></div>"
        assert node.to_html() == expected_html, "Test 4 failed"

        node = ParentNode(tag="div", children=[
            "Hello, ",
            ParentNode(tag="span", children=["World"]),
            "!"
        ])
        expected_html = "<div>Hello, <span>World</span>!</div>"
        assert node.to_html() == expected_html, "Test 5 failed"

        try:
            node = ParentNode(tag=None, children=["Hello"])
            node.to_html()
        except ValueError as e:
            assert str(e) == "The object doesn't have a tag", "Test 6 failed"

        try:
            node = ParentNode(tag="div", children=None)
            node.to_html()
        except ValueError as e:
            assert str(e) == "The object doesn't have children", "Test 7 failed"

        node = ParentNode(tag="div", children=[123, 456])
        assert node.to_html() == "<div>123456</div>", "Test 8 failed"

if __name__ == "__main__":
    unittest.main()