from inline import text_to_textnodes
from enum import Enum
import re

def markdown_to_blocks(markdown:str) -> list[str]:
    blocks = markdown.split('\n\n')
    blocks = list(map(lambda block: block.strip(), blocks))
    blocks = list(filter(lambda block: block != "", blocks))
    return blocks

class BlockType(Enum):
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"
    PARAGRAPH = "paragraph"

def block_to_block_type(block_md:str) -> BlockType:
    heading_pattern = r"^#{1,6} [^\s].*$"
    code_pattern = r"^```.*?```$"
    quote_line_pattern = r"^>.*$"
    uo_list_line_pattern = r"^- .*$"
    lines = block_md.split('\n')
    if bool(re.match(heading_pattern, block_md, re.DOTALL)):
        return BlockType.HEADING
    elif bool(re.fullmatch(code_pattern, block_md, re.DOTALL)):
        return BlockType.CODE
    elif all(re.fullmatch(quote_line_pattern, line) for line in lines):
        return BlockType.QUOTE
    elif all(re.fullmatch(uo_list_line_pattern, line) for line in lines):
        return BlockType.UNORDERED_LIST
    elif all(re.match(rf"^{i+1}\. .*$", line) for i, line in enumerate(lines)):
        return BlockType.ORDERED_LIST
    else:
        return BlockType.PARAGRAPH
