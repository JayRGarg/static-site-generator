from htmlnode import HTMLNode

class ParentNode(HTMLNode):

    def __init__(self, tag:str, children:list[HTMLNode], props:dict[str,str]|None=None) -> None:
        super().__init__(tag=tag, value=None, children=children, props=props)

    def to_html(self) -> str:
        if not self.tag:
            raise ValueError("Node tag does not exist.")
        if not self.children:
            raise ValueError("Node children do not exist.")
        else:
            out : str = f"<{self.tag}{self.props_to_html()}>"
            for child in self.children:
                out += f"{child.to_html()}"
            out += f"</{self.tag}>"
            return out

    def __repr__(self) -> str:
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
