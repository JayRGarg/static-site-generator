import unittest

from htmlnode import HTMLNode
from leafnode import LeafNode
from parentnode import ParentNode
from textnode import TextNode, TextType, text_node_to_html_node
from inline import split_nodes_delimiter, extract_markdown_images, extract_markdown_links, split_nodes_image, split_nodes_link, text_to_textnodes
from block import markdown_to_blocks, BlockType, block_to_block_type

class TestBlocks(unittest.TestCase):

    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )
        
    def test_markdown_to_blocks2(self):
        md = """
This is **bolded** paragraph




This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    #Block to Block tests
    def test_block_to_block_type_heading(self):
        cases = [
                    ("# This is a heading", BlockType.HEADING),
                    ("## This is a heading", BlockType.HEADING),
                    ("### This is a heading", BlockType.HEADING),
                    ("#### This is a heading", BlockType.HEADING),
                    ("##### This is a heading", BlockType.HEADING),
                    ("###### This is a heading", BlockType.HEADING),
                    ("###### This is a heading", BlockType.HEADING),
                    ("# This is a heading\nstill the same heading\nstill heading", BlockType.HEADING),
                    ("#not a heading", BlockType.PARAGRAPH),
                ]
        for input, expected in cases:
            self.assertEqual(block_to_block_type(input), expected)

    def test_block_to_block_type_code(self):
        cases = [
                    ("```# This is a code```", BlockType.CODE),
                    ("```# This is\na \ncode```", BlockType.CODE),
                    ("`````````", BlockType.CODE),
                    ("```#not a heading```", BlockType.CODE),
                    ("```\nasdfasf", BlockType.PARAGRAPH),
                    ("``````\nasdfasf", BlockType.PARAGRAPH),
                ]
        for input, expected in cases:
            self.assertEqual(block_to_block_type(input), expected)

    def test_block_to_block_type_quote(self):
        cases = [
                    ("> This is a quote", BlockType.QUOTE),
                    ("> This is a quote\n>Q\n>", BlockType.QUOTE),
                    (">Not\n> \nc", BlockType.PARAGRAPH),
                ]
        for input, expected in cases:
            self.assertEqual(block_to_block_type(input), expected)

    def test_block_to_block_type_uo_list(self):
        cases = [
                    ("- This is an unordered list", BlockType.UNORDERED_LIST),
                    ("- This is \n- still an\n- unordered list", BlockType.UNORDERED_LIST),
                    ("- This is \n- still an\n- unordered list\n- ", BlockType.UNORDERED_LIST),
                    ("- This is \n- still an\n- unordered list\n- \n- test", BlockType.UNORDERED_LIST),
                    ("- This is \n-not an\n- unordered list\n- \n- test", BlockType.PARAGRAPH),
                ]
        for input, expected in cases:
            self.assertEqual(block_to_block_type(input), expected)

    def test_block_to_block_type_o_list(self):
        cases = [
                    ("1. This is an ordered list", BlockType.ORDERED_LIST),
                    ("1. This is \n2. still an\n3. ordered list", BlockType.ORDERED_LIST),
                    ("1. This is \n2. still an\n3. ordered list\n4. ", BlockType.ORDERED_LIST),
                    ("1. This is \n2.not an\n3. ordered list\n4. \n5. test", BlockType.PARAGRAPH),
                    ("1. This is \n2 not an\n3. ordered list\n4. \n5. test", BlockType.PARAGRAPH),
                    ("1. This is \n\n not an\n3. ordered list\n4. \n5. test", BlockType.PARAGRAPH),
                    ("1. This is \n. not an\n3. ordered list\n4. \n5. test", BlockType.PARAGRAPH),
                ]
        for input, expected in cases:
            self.assertEqual(block_to_block_type(input), expected)

    def test_block_to_block_type_paragraph(self):
        cases = [
                    ("This is a paragraph ", BlockType.PARAGRAPH),
                    ("This \nis a paragraph ", BlockType.PARAGRAPH),
                    ("This is a paragraph ", BlockType.PARAGRAPH),
                    ("", BlockType.PARAGRAPH),
                    (" ", BlockType.PARAGRAPH),
                    ("\n\n", BlockType.PARAGRAPH),
                ]
        
        for input, expected in cases:
            self.assertEqual(block_to_block_type(input), expected)

    def test_block_to_block_types(self):
        block = "# heading"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)
        block = "```\ncode\n```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)
        block = "> quote\n> more quote"
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)
        block = "- list\n- items"
        self.assertEqual(block_to_block_type(block), BlockType.UNORDERED_LIST)
        block = "1. list\n2. items"
        self.assertEqual(block_to_block_type(block), BlockType.ORDERED_LIST)
        block = "paragraph"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

if __name__ == "__main__":
    _ = unittest.main()
