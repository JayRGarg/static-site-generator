import unittest

from htmlnode import HTMLNode
from leafnode import LeafNode
from parentnode import ParentNode

class TestHTMLNode(unittest.TestCase):
    #HTMLNode Tests
    def test_props(self):
        props = {
                    "href": "https://www.google.com",
                    "target": "_blank",
                }
        node = HTMLNode(props=props)
        output_props = node.props_to_html()
        expected_props = ' href="https://www.google.com" target="_blank"'
        """
        print("output_props:")
        print(output_props)
        print("expected_props:")
        print(expected_props)
        """
        self.assertEqual(output_props, expected_props)

    def test_tag(self):
        node = HTMLNode(tag="p", value="this is a paragraph", children=[HTMLNode(tag="a")], props={"href":"https://www.google.com"})
        self.assertEqual(node.tag, "p")
    
    def test_value(self):
        node = HTMLNode(tag="p", value="this is a paragraph", children=[HTMLNode(tag="a")], props={"href":"https://www.google.com"})
        self.assertEqual(node.value, "this is a paragraph")
    
    def test_children(self):
        node = HTMLNode(tag="p", value="this is a paragraph", children=[HTMLNode(tag="a")], props={"href":"https://www.google.com"})
        self.assertEqual(repr(node.children), repr([HTMLNode(tag="a")]))

    def test_repr(self):
        node = HTMLNode(tag="p", value="this is a paragraph", children=[HTMLNode(tag="a")], props={"href":"https://www.google.com"})
        self.assertEqual(str(repr(node)), f"HTMLNode(tag: {node.tag},\nvalue: {node.value},\nchildren: {node.children},\nprops: {node.props})")

    #LeafNode Tests
    def test_leaf_to_html_p1(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    
    def test_leaf_to_html_p2(self):
        node = LeafNode("p", "This is a paragraph of text.") 
        self.assertEqual(node.to_html(), "<p>This is a paragraph of text.</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"}) 
        self.assertEqual(node.to_html(), f'<a href="https://www.google.com">Click me!</a>')

    #ParentNode Tests
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_grandchildren_with_props(self):
        grandchild_node = LeafNode("b", "grandchild", {"color": "red"})
        grandchild_node_2 = LeafNode("b", "grandchild 2", {"color": "blue"})
        child_node = ParentNode("span", [grandchild_node, grandchild_node_2], {"href":"https://www.google.com"})
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            '<div><span href="https://www.google.com"><b color="red">grandchild</b><b color="blue">grandchild 2</b></span></div>'
            )

if __name__ == "__main__":
    unittest.main()
