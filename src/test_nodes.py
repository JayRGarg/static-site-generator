import unittest

from htmlnode import HTMLNode
from leafnode import LeafNode
from parentnode import ParentNode
from textnode import TextNode, TextType, text_node_to_html_node

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

    #TextNode Tests
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_url(self):
        node = TextNode("this is a link node", TextType.LINK, "https://www.google.com")
        node2 = TextNode("this is a link node", TextType.LINK, "https://www.google.com")
        self.assertEqual(node, node2)

    def test_noteq_url(self):
        node = TextNode("this is a link node", TextType.LINK, "https://google.com")
        node2 = TextNode("this is a link node", TextType.LINK, "https://www.google.com")
        self.assertNotEqual(node, node2)
    #text to html
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
        self.assertEqual(html_node.to_html(), "This is a text node")
        assert html_node.children is None
        assert html_node.props is None

    def test_text_bold(self):
        node = TextNode("This is a bold node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, 'b')
        self.assertEqual(html_node.value, "This is a bold node")
        self.assertEqual(html_node.to_html(), "<b>This is a bold node</b>")
        assert html_node.children is None
        assert html_node.props is None

    def test_text_italic(self):
        node = TextNode("This is an italic node", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, 'i')
        self.assertEqual(html_node.value, "This is an italic node")
        self.assertEqual(html_node.to_html(), "<i>This is an italic node</i>")
        assert html_node.children is None
        assert html_node.props is None

    def test_text_code(self):
        node = TextNode("This is a code node", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, 'code')
        self.assertEqual(html_node.value, "This is a code node")
        self.assertEqual(html_node.to_html(), "<code>This is a code node</code>")
        assert html_node.children is None
        assert html_node.props is None

    def test_text_link(self):
        node = TextNode("This is a link node", TextType.LINK, url="https://www.google.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, 'a')
        self.assertEqual(html_node.value, "This is a link node")
        self.assertEqual(html_node.props, {"href": "https://www.google.com"})
        self.assertEqual(html_node.to_html(), f'<a href="https://www.google.com">This is a link node</a>')
        assert html_node.children is None

    def test_text_image(self):
        node = TextNode("This is an image node", TextType.IMAGE, url="./test.png")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, 'img')
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props, {"src": "./test.png", "alt": "This is an image node"})
        self.assertEqual(html_node.to_html(), '<img src="./test.png" alt="This is an image node"></img>')
        assert html_node.children is None


if __name__ == "__main__":
    unittest.main()
