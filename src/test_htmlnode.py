import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
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

if __name__ == "__main__":
    unittest.main()
