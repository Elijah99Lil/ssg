import unittest
from htmlnode import *

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(tag="a", props={"href": "https://google.com"})
        self.assertEqual(node.props_to_html(),  ' href="https://google.com"')

    def test_empty_props(self):
        node = HTMLNode(tag="p", value="hampter")
        self.assertEqual(node.props_to_html(), "")

    def test_value_only(self):
        node = HTMLNode(value="*jumps down from the top of the fridge* I'm gay!")
        self.assertEqual(node.props_to_html(), "")

    def test_to_html_value_tag(self):
        node = LeafNode(tag="p", value="PEEPEEPOOPOO")
        self.assertEqual(node.to_html(), "<p>PEEPEEPOOPOO</p>")

    def test_leafnode_rejects_children(self):
        with self.assertRaises(TypeError):
            LeafNode(tag="p", value="Some text", children=[HTMLNode()])

    def test_to_html_value_error_when_value_is_missing(self):
        node = LeafNode(tag="a", value=None)
        with self.assertRaises(ValueError):
            node.to_html()


if __name__ == "__main__":
    unittest.main()