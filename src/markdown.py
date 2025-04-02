from htmlnode import HTMLNode
from textnode import TextType, TextNode, text_node_to_html_node
from parentnode import ParentNode
from leafnode import LeafNode
from block import markdown_to_blocks, block_to_block_type, BlockType
from inline import text_to_textnodes





def markdown_to_html_node(md:str) -> HTMLNode:

    blocks:list[str] = markdown_to_blocks(md)
    children:list[HTMLNode] = list(map(block_to_node, blocks))
    parent:HTMLNode = ParentNode(tag='div', children=children)
    return parent


def block_to_node(block:str) -> HTMLNode:
    block_type = block_to_block_type(block)
    if block_type == BlockType.HEADING:
        text, tag = get_heading_text_tag(block)
        children = text_to_children_gen(text)
        return ParentNode(tag, children)
    elif block_type == BlockType.CODE:
        text = block[3:len(block)-3]#.strip()
        text = text[1:]#removing first newline
        return ParentNode("pre", [text_node_to_html_node(TextNode(text, TextType.CODE))])
    elif block_type == BlockType.QUOTE:
        lines = block.split('\n')
        text = '\n'.join([line[1:].strip() for line in lines])
        children = text_to_children_gen(text)
        return ParentNode('blockquote', children)
    elif block_type == BlockType.UNORDERED_LIST:
        lines = block.split('\n')
        text = '\n'.join([line[2:] for line in lines])
        children = text_to_children_list(text)
        return ParentNode('ul', children)
    elif block_type == BlockType.ORDERED_LIST:
        lines = block.split('\n')
        text = '\n'.join([line[3:] for line in lines])
        children = text_to_children_list(text)
        return ParentNode('ol', children)
    elif block_type == BlockType.PARAGRAPH:
        text = block
        children = text_to_children_gen(text)
        return ParentNode("p", children)
    else:
        raise Exception("Invalid BlockType")

#General Usage
def text_to_children_gen(text:str) -> list[HTMLNode]:
    text = text.replace('\n', ' ')
    textnodes = text_to_textnodes(text)
    children = list(map(text_node_to_html_node, textnodes))
    return children

def text_to_children_list(text:str) -> list[HTMLNode]:
    lines = text.split('\n')
    children:list[HTMLNode] = []
    textnodes:list[TextNode] = []
    for line in lines:
        textnodes = text_to_textnodes(line)
        grandchildren = list(map(text_node_to_html_node, textnodes))
        children.append(ParentNode('li', grandchildren))
    return children

def get_heading_text_tag(block:str) -> tuple[str, str]:
    if block.startswith('###### '):
        return (block[7:], 'h6')
    elif block.startswith('##### '):
        return (block[6:], 'h5')
    elif block.startswith('#### '):
        return (block[5:], 'h4')
    elif block.startswith('### '):
        return (block[4:], 'h3')
    elif block.startswith('## '):
        return (block[3:], 'h2')
    elif block.startswith('# '):
        return (block[2:], 'h1')
    else:
        raise Exception("Improper Heading Format")

def extract_title(markdown:str) -> str:
    lines = markdown.split('\n')
    for line in lines:
        if line.startswith("# "):
            return line[2:].strip()
    raise Exception("No H1 ('#') Header Included!")

