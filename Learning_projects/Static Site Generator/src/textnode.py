from enum import Enum

class TextType(Enum):
    NORMAL = "normal"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode():
    def __init__(self, TEXT, TEXT_TYPE, URL = None):
        self.text = TEXT
        self.text_type = TEXT_TYPE
        self.url = URL
    
    def __eq__(self,another_text_node):
        if not isinstance(another_text_node, TextNode):
            return False
        return (
            self.text == another_text_node.text and
            self.text_type == another_text_node.text_type and
            self.url == another_text_node.url
        )
    
    def __repr__(self):
        representation = f"TextNode(TEXT = {self.text}, TEXT_TYPE = {self.text_type!r}, URL = {self.url})"
        return representation

