import unittest
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_to_html_with_tag_and_props(self):
        node = LeafNode(tag="a", value="Click me!", props={"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_to_html_with_tag_no_props(self):
        node = LeafNode(tag="p", value="This is a paragraph of text.")
        self.assertEqual(node.to_html(), '<p>This is a paragraph of text.</p>')

    def test_to_html_no_tag(self):
        node = LeafNode(value="Raw text")
        self.assertEqual(node.to_html(), "Raw text")

    def test_to_html_no_value(self):
        with self.assertRaises(ValueError):
            LeafNode(tag="p").to_html()

if __name__ == "__main__":
    unittest.main()
