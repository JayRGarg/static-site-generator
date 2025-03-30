from __future__ import annotations
from functools import reduce

class HTMLNode:

    def __init__(self, tag:str=None, value:str=None, children:list[HTMLNode]=None, props:dict[str,str] =None) -> None:
        self.tag: str = tag
        self.value: str = value
        self.children: list[HTMLNode] = children
        self.props: dict[str,str] = props

    def to_html(self) -> None:
        raise NotImplementedError

    def props_to_html(self) -> str:
        return reduce(lambda x, y: x + f' {y[0]}="{y[1]}"', self.props.items(), "") if self.props else ""

    def __repr__(self) -> str:
        return f"HTMLNode(tag: {self.tag},\nvalue: {self.value},\nchildren: {self.children},\nprops: {self.props})"
