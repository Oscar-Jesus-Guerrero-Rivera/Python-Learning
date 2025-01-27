from htmlnode import *

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, children, props)
        self.value = None

    def to_html(self):
        if not self.tag:
            raise ValueError("The object doesnt have a tag")
        if self.children is None:
            raise ValueError("The object doesnt have a children")
        children_html = ""
        for child in self.children:
            if isinstance(child,HTMLNode):
                children_html += child.to_html()
            else:
                children_html += str(child)
        parent_html = f"<{self.tag}>{children_html}</{self.tag}>"
        return parent_html
        