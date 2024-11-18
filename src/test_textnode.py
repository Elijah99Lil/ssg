import unittest
from textnode import TextNode, TextType, text_node_to_html_node
import pytest

class TestTextNode(unittest.TestCase):
#TextNode class tests
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_true(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)
    
    def test_false(self):
        node = TextNode("This is a text node", TextType.CODE)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertFalse(node == node2)

    def test_is_none(self):
        node = TextNode("This is a text node", TextType.LINK, url=None)
        self.assertIsNone(node.url)

#Handling different text type method tests
    def test_text(self):
        text_node = TextNode("This is a text test.", TextType.TEXT)
        html_node = text_node_to_html_node(text_node)
        assert html_node.tag == ""
        assert html_node.value == "This is a text test."

    def test_bold(self):
        text_node = TextNode("Bold text test.", TextType.BOLD)
        html_node = text_node_to_html_node(text_node)
        assert html_node.tag == "b"
        assert html_node.value == "Bold text test."

    def test_italic(self):
        text_node = TextNode("Italic text test.", TextType.ITALIC)
        html_node = text_node_to_html_node(text_node)
        assert html_node.tag == "i"
        assert html_node.value == "Italic text test."

    def test_code(self):
        text_node = TextNode("Code text test.", TextType.CODE)
        html_node = text_node_to_html_node(text_node)
        assert html_node.tag == "code"
        assert html_node.value == "Code text test."

    def test_link(self):
        text_node = TextNode("Link", TextType.LINK, "https://www.boot.dev")
        html_node = text_node_to_html_node(text_node)
        assert html_node.tag == "a"
        assert html_node.value == "Link"
        assert html_node.props == {"href": "https://www.boot.dev"}

    def test_image(self):
        text_node = TextNode("", TextType.IMAGE, "https://example.com/image.png")
        html_node = text_node_to_html_node(text_node)
        assert html_node.tag == "img"
        assert html_node.value == ""
        assert html_node.props == {"src": "https://example.com/image.png", "alt": ""}

    def test_invalid_text_type(self):
        text_node = TextNode("Hello", "not_a_valid_type")
        with pytest.raises(Exception):
            html_node = text_node_to_html_node(text_node)

if __name__ == "__main__":
    unittest.main()