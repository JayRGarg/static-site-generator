from htmlnode import HTMLNode

class LeafNode(HTMLNode):

    def __init__(self, tag:str, value:str, props: dict[str,str]=None) -> str:
        super().__init__(tag=tag, value=value, children=None, props=props)

    def to_html(self) -> str:
        if not self.value:
            raise ValueError("Node value does not exist.")
        if not self.tag:
            return self.value
        else:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self) -> str:
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
