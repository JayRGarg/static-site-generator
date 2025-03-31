from htmlnode import HTMLNode

class LeafNode(HTMLNode):

    def __init__(self, tag:str|None, value:str, props: dict[str,str]|None=None) -> None:
        super().__init__(tag=tag, value=value, children=None, props=props)

    def to_html(self) -> str:
        if self.value is None:
            raise ValueError("Node value can not be NoneType.")
        if not self.tag:
            return self.value
        else:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self) -> str:
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
