from __future__ import annotations
from functools import reduce

class HTMLNode:

    def __init__(self, tag:str|None=None, value:str|None=None, children:list[HTMLNode]|None=None, props:dict[str,str]|None=None) -> None:
        self.tag: str|None = tag
        self.value: str|None = value
        self.children: list[HTMLNode]|None = children
        self.props: dict[str,str]|None = props

    def to_html(self) -> None:
        raise NotImplementedError

    def props_to_html(self) -> str:
        return reduce(lambda x, y: x + f' {y[0]}="{y[1]}"', self.props.items(), "") if self.props else ""

    def __repr__(self) -> str:
        return f"HTMLNode(tag: {self.tag},\nvalue: {self.value},\nchildren: {self.children},\nprops: {self.props})"
