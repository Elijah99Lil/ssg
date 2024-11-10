import unittest
from htmlnode import *

class TestHTMLNode(unittest.TestCase):
#HTML tests
    def test_props_to_html(self):
        node = HTMLNode(tag="a", props={"href": "https://google.com"})
        self.assertEqual(node.props_to_html(),  ' href="https://google.com"')

    def test_empty_props(self):
        node = HTMLNode(tag="p", value="hampter")
        self.assertEqual(node.props_to_html(), "")

    def test_value_only(self):
        node = HTMLNode(value="*jumps down from the top of the fridge* I'm gay!")
        self.assertEqual(node.props_to_html(), "")

#LeafNode tests
    def test_to_html_value_tag(self):
        node = LeafNode(tag="p", value="PEEPEEPOOPOO")
        self.assertEqual(node.to_html(), "<p>PEEPEEPOOPOO</p>")

    def test_leafnode_rejects_children(self):
        with self.assertRaises(TypeError):
            LeafNode(tag="p", value="Some text", children=[HTMLNode()])

    def test_to_html_missing_value(self):
        node = LeafNode(tag="a", value=None)
        with self.assertRaises(ValueError):
            node.to_html()

#ParentNode tests
    def test_multiple_children(self):
        node = ParentNode("div", 
            [LeafNode("p", "Child 1"),
            LeafNode("p", "Child 2")])
        self.assertGreater(len(node.children), 1)

    def test_nested_parents(self):
        inner_node = ParentNode("div", [
            LeafNode("p", "Inner child")
        ])
    
        outer_node = ParentNode("section", [
            LeafNode("span", "First child"),
            inner_node, 
            LeafNode("span", "Last child")
        ])

        result = outer_node.to_html()
        expected = "<section><span>First child</span><div><p>Inner child</p></div><span>Last child</span></section>"
        self.assertEqual(result, expected)

    def test_empty_list_of_children(self):
        with self.assertRaises(ValueError):
            node = ParentNode("tag", [])

    def test_none_tag(self):
        with self.assertRaises(ValueError):
            node = ParentNode(None, [LeafNode("p", "some text")])
            node.to_html()

    def test_with_props(self):
        node = ParentNode("a", [LeafNode("p", "some text")], props={"href": "https://google.com"})
        result = node.to_html()
        expected = '<a href="https://google.com"><p>some text</p></a>'
        assert result == expected

if __name__ == "__main__":
    unittest.main()