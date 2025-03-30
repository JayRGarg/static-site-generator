from __future__ import annotations
from enum import Enum
from leafnode import LeafNode

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    
    def __init__(self, text:str, text_type:TextType, url:str|None=None) -> None:
        self.text:str = text
        self.text_type:TextType = text_type
        self.url:str|None = url

    def __eq__(self, other:TextNode) -> bool:
        return (self.text == other.text and \
                self.text_type == other.text_type and \
                self.url == other.url)

    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

# def text_node_to_html_node(text_node):
#     match text_node.text_type:
#         case TextType.TEXT:
#             return LeafNode()
