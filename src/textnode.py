from enum import Enum
from htmlnode import LeafNode

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url =  url

    def __eq__(self, other):
        return (self.text == other.text and 
                self.text_type == other.text_type and 
                self.url == other.url)
    
    def __repr__(self):
        return f'TextNode({self.text}, {self.text_type}, {self.url})'
    
def handle_text(text_node):
        return LeafNode("", text_node.text)

def handle_bold(text_node):
        return LeafNode("b", text_node.text)
    
def handle_italic(text_node):
        return LeafNode("i", text_node.text)
    
def handle_code(text_node):
        return LeafNode("code", text_node.text)

def handle_link(text_node):
        return LeafNode("a", text_node.text, {"href": text_node.url})
    
def handle_image(text_node):
        return LeafNode("img", "", {"src": text_node.url,"alt": text_node.text})

def text_node_to_html_node(text_node):
    if text_node.text_type == TextType.TEXT:
        return handle_text(text_node)
    elif text_node.text_type == TextType.BOLD:
        return handle_bold(text_node)
    elif text_node.text_type == TextType.ITALIC:
        return handle_italic(text_node)
    elif text_node.text_type == TextType.CODE:
        return handle_code(text_node)
    elif text_node.text_type == TextType.LINK:
        return handle_link(text_node)
    elif text_node.text_type == TextType.IMAGE:
        return handle_image(text_node)
    raise Exception()