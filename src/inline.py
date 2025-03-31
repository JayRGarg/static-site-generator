from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes:list[TextNode], delimiter:str, text_type:TextType) -> list[TextNode]:
    new_nodes:list[TextNode] = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            sections = node.text.split(delimiter)
            if len(sections) == 0:
                new_nodes.append(TextNode(node.text, TextType.TEXT))
            elif len(sections) % 2 == 1: #even number of delimiters
                count = len(sections)
                while count > 0:
                    if count % 2 == 1:
                        next_type = TextType.TEXT
                    else:
                        next_type = text_type
                    if sections[len(sections)-count]!="": new_nodes.append(TextNode(sections[len(sections)-count], next_type))
                    count -= 1
            else:
                raise Exception(f"Syntax Error: expection a: {delimiter}")
    return new_nodes
