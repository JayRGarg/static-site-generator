from __future__ import annotations
from enum import Enum
from htmlnode import HTMLNode
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

def text_node_to_html_node(text_node: TextNode) -> HTMLNode:
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(tag=None, value=text_node.text)
        case TextType.BOLD:
            return LeafNode(tag='b', value=text_node.text)
        case TextType.ITALIC:
            return LeafNode(tag='i', value=text_node.text)
        case TextType.CODE:
            return LeafNode(tag='code', value=text_node.text)
        case TextType.LINK:
            if text_node.url is not None: return LeafNode(tag='a', value=text_node.text, props={'href': text_node.url})
            else: raise Exception("Missing URL!")
        case TextType.IMAGE:
            if text_node.url is not None: return LeafNode(tag='img', value='', props={'src': text_node.url, 'alt': text_node.text})
            else: raise Exception("Missing Image URL!")
        case _:
            raise Exception("Invalid TextNode type!")
