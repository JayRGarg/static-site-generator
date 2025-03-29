from functools import reduce

class HTMLNode:

    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        return reduce(lambda x, y: x + f' {y[0]}="{y[1]}"', self.props.items(), "") if self.props else ""

    def __repr__(self):
        return f"HTMLNode(tag: {self.tag},\nvalue: {self.value},\nchildren: {self.children},\nprops: {self.props})"
