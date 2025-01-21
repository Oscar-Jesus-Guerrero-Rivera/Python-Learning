from htmlnode import *

class LeafNode(HTMLNode):
    def __init__(self, tag = None, value=None, props=None):
        if value is None:
            raise ValueError("The 'value' parameter is required for a LeafNode.")
        super().__init__(tag=tag, value=value, children=None, props=props)
        self.children = []

    def to_html(self):
        if not self.value:
            raise ValueError("LeafNode must have a value to render as HTML.")
        
        if not self.tag:
            return self.value

        props_html = self.props_to_html()
        return f"<{self.tag}{props_html}>{self.value}</{self.tag}>"