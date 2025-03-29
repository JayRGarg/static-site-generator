import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
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


if __name__ == "__main__":
    unittest.main()
