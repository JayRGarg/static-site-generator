from textnode import TextNode, TextType
import re

def text_to_textnodes(text:str) -> list[TextNode]:
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes

def split_nodes_delimiter(old_nodes:list[TextNode], delimiter:str, text_type:TextType) -> list[TextNode]:
    new_nodes:list[TextNode] = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            sections = node.text.split(delimiter)
            if len(sections) == 0:
                new_nodes.append(TextNode(node.text, TextType.TEXT, node.url))
            elif len(sections) % 2 == 1: #even number of delimiters
                count = len(sections)
                while count > 0:
                    if count % 2 == 1:
                        next_type = TextType.TEXT
                    else:
                        next_type = text_type
                    if sections[len(sections)-count]!="": new_nodes.append(TextNode(sections[len(sections)-count], next_type, node.url))
                    count -= 1
            else:
                raise Exception(f"Syntax Error: expection a: {delimiter}")
    return new_nodes

def extract_markdown_images(text:str) -> list[tuple[str,str]]:
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def extract_markdown_links(text:str) -> list[tuple[str,str]]:
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def split_nodes_image(old_nodes:list[TextNode]) -> list[TextNode]:
    new_nodes:list[TextNode] = []
    for node in old_nodes:
        extracted = extract_markdown_images(node.text)
        curr_text:str = node.text
        while extracted:
            img_alt, img_url = extracted[0]
            sections: list[str] = curr_text.split(f"![{img_alt}]({img_url})", 1)
            if sections[0]:#if curr_text does not start with image
                new_nodes.append(TextNode(sections[0], node.text_type, node.url))
            new_nodes.append(TextNode(img_alt, TextType.IMAGE, img_url))
            curr_text = sections[1] #if this is empty, then extraction will be empty anyways, next outer loop will iterate
            extracted = extracted[1:]
        if curr_text: new_nodes.append(TextNode(curr_text, node.text_type, node.url))
    return new_nodes

def split_nodes_link(old_nodes:list[TextNode]) -> list[TextNode]:
    new_nodes:list[TextNode] = []
    for node in old_nodes:
        extracted = extract_markdown_links(node.text)
        curr_text:str = node.text
        while extracted:
            link_anc, link_url = extracted[0]
            sections: list[str] = curr_text.split(f"[{link_anc}]({link_url})", 1)
            if sections[0]:#if curr_text does not start with link
                new_nodes.append(TextNode(sections[0], node.text_type, node.url))
            new_nodes.append(TextNode(link_anc, TextType.LINK, link_url))
            curr_text = sections[1] #if this is empty, then extraction will be empty anyways, next outer loop will iterate
            extracted = extracted[1:]
        if curr_text: new_nodes.append(TextNode(curr_text, node.text_type, node.url))
    return new_nodes
