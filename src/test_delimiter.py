from delimiter import *
from htmlnode import *
from textnode import *
import unittest

class TestDelimiter(unittest.TestCase):

#TextNode Delimiter tests
    def test_no_delimiter(self):
        node = TextNode("This is text with a regular word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        assert len(new_nodes) == 1
        assert new_nodes[0].text == "This is text with a regular word"
        assert new_nodes[0].text_type == TextType.TEXT

    def test_code_delimiter(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        assert len(new_nodes) == 3
        assert new_nodes[0].text == "This is text with a "
        assert new_nodes[1].text == "code block"
        assert new_nodes[2].text == " word"

    def test_bold_delimiter(self):
        node = TextNode("This is text with a **bold** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        assert len(new_nodes) == 3
        assert new_nodes[0].text == "This is text with a "
        assert new_nodes[1].text == "bold"
        assert new_nodes[2].text == " word"

    def test_italic_delimiter(self):
        node = TextNode("This is text with a *italic* word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "*", TextType.ITALIC)
        assert len(new_nodes) == 3
        assert new_nodes[0].text == "This is text with a "
        assert new_nodes[1].text == "italic"
        assert new_nodes[2].text == " word"

    def test_incorrect_markdown_syntax(self):
        node = TextNode("This is text with a *bad word", TextType.TEXT)
        with self.assertRaises(Exception):
            split_nodes_delimiter([node], "*", TextType.ITALIC)