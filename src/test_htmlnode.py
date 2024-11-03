import unittest
from htmlnode import *

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(tag="a", props={"href": "https://google.com"})
        self.assertEqual(node.props_to_html(),  ' href="https://google.com"')

    def test_empty_props(self):
        node = HTMLNode(tag="p", value="hampter")
        self.assertEqual(node.props_to_html(), "")

    def test(self):
        node = HTMLNode(value="*jumps down from the top of the fridge* I'm gay!")
        self.assertEqual(node.props_to_html(), "")

if __name__ == "__main__":
    unittest.main()