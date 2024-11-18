from delimiter import split_nodes_delimiter, split_nodes_image, split_nodes_link, extract_markdown_images, extract_markdown_links
from textnode import TextNode, TextType
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

#Extract Markdown for Images and Links Tests
    def test_extract_markdown_for_images(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        result = extract_markdown_images(text)
        assert result == [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]

    def test_extract_markdown_for_a_singular_image(self):
        text = "![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        result = extract_markdown_images(text)
        assert result == [("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]

    def test_extract_markdown_for_links(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        result = extract_markdown_links(text)
        assert result == [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]

    def test_extract_markdown_for_a_singular_link(self):
        text = "[to boot dev](https://www.boot.dev)"
        result = extract_markdown_links(text)
        assert result == [("to boot dev", "https://www.boot.dev")]

    def test_empty_text_images(self):
        text = ""
        result = extract_markdown_images(text)
        assert result == []

    def test_empty_text_links(self):
        text = ""
        result = extract_markdown_links(text)
        assert result == []

#Split Nodes Tests for Images and Links

    def test_multi_images(self):
        text = "Here is ![bear](bear.jpg) walking and ![cat](cat.jpg) sleeping"
        node = TextNode(text, TextType.TEXT)
        result = split_nodes_image([node])
        assert result == [
                TextNode("Here is ", TextType.TEXT),
                TextNode("bear", TextType.IMAGE, "bear.jpg"),
                TextNode(" walking and ", TextType.TEXT),
                TextNode("cat", TextType.IMAGE, "cat.jpg"),
                TextNode(" sleeping", TextType.TEXT)
            ]

    def test_no_images(self):
        text = "This is text with no images."
        node = TextNode(text, TextType.TEXT)
        result = split_nodes_image([node])
        assert result == [node]

    def test_special_characters(self):
        text = "This is a FRICKIN!!!!!! HECKIN!!! DOGGO!!!! ![doggo](doggo.jpg) HOLY HECK!!***^%&%$^$&"
        node = TextNode(text, TextType.TEXT)
        result = split_nodes_image([node])
        assert result == [
            TextNode("This is a FRICKIN!!!!!! HECKIN!!! DOGGO!!!! ", TextType.TEXT, None),
            TextNode("doggo", TextType.IMAGE, "doggo.jpg"),
            TextNode(" HOLY HECK!!***^%&%$^$&", TextType.TEXT, None)
        ]

    def test_beginning_empty_node(self):
        text = "![doggydoggodoog](dog.jpg) a doggo ! yay !"
        node = TextNode(text, TextType.TEXT)
        result = split_nodes_image([node])
        assert result == [
            TextNode("doggydoggodoog", TextType.IMAGE, "dog.jpg"),
            TextNode(" a doggo ! yay !", TextType.TEXT, None)
        ]

    
    def test_ending_empty_node(self):
        text = "a doggo ! yay ! ![doggydoggodoog](dog.jpg)"
        node = TextNode(text, TextType.TEXT)
        result = split_nodes_image([node])
        assert result == [
            TextNode("a doggo ! yay ! ", TextType.TEXT, None),
            TextNode("doggydoggodoog", TextType.IMAGE, "dog.jpg")
        ]

    def test_no_links(self):
        text = "This is a basic text string with no links. Get fucked loser!"
        node = TextNode(text, TextType.TEXT)
        result = split_nodes_link([node])
        assert result == [node]


    def test_multi_links(self):
        text = "Here is a [bear](bear.com) walking and a [cat](cat.com) sleeping"
        node = TextNode(text, TextType.TEXT)
        result = split_nodes_link([node])
        assert result == [
            TextNode("Here is a ", TextType.TEXT),
            TextNode("bear", TextType.LINK, "bear.com"),
            TextNode(" walking and a ", TextType.TEXT),
            TextNode("cat", TextType.LINK, "cat.com"),
            TextNode(" sleeping", TextType.TEXT)
        ]

    def test_both_images_and_links(self):
        text = "Here is a text string with a ![doggo](doggo.jpg) image and a [catto](cat.com)."
        node = TextNode(text, TextType.TEXT)
        split_images = split_nodes_image([node])
        result = split_nodes_link(split_images)
        assert result == [
            TextNode("Here is a text string with a ", TextType.TEXT),
            TextNode("doggo", TextType.IMAGE, "doggo.jpg"),
            TextNode(" image and a ", TextType.TEXT),
            TextNode("catto", TextType.LINK, "cat.com"),
            TextNode(".", TextType.TEXT)
        ]

    def test_links_at_beginning(self):
        text = "[Website of Turtwig, our God.](turtwig.com) the end of times is nigh."
        node = TextNode(text, TextType.TEXT)
        result = split_nodes_link([node])
        assert result == [
            TextNode("Website of Turtwig, our God.", TextType.LINK, "turtwig.com"),
            TextNode(" the end of times is nigh.", TextType.TEXT)
        ]

    def test_links_at_end(self):
        text = "This is the BRAND NEW 2006 HONDA CIVIC NOW AVAILABLE AT TOYOTATHON!! TOYOTATHON4EVER!! [TOYOTATHON IS ON!](https://www.mountainstatestoyota.com/toyotathon.htm)"
        node = TextNode(text, TextType.TEXT)
        result = split_nodes_link([node])
        assert result == [
            TextNode("This is the BRAND NEW 2006 HONDA CIVIC NOW AVAILABLE AT TOYOTATHON!! TOYOTATHON4EVER!! ", TextType.TEXT),
            TextNode("TOYOTATHON IS ON!", TextType.LINK, "https://www.mountainstatestoyota.com/toyotathon.htm")
        ] 


    def test_invalid_links(self):
        text = "Watch T1 ruin the LPL players' salary LIVE here![T1 FIGHTING(T1.T1.T1.PeepeePooPoo!)"
        node = TextNode(text, TextType.TEXT)
        result = split_nodes_link([node])
        assert result == [
            TextNode("Watch T1 ruin the LPL players' salary LIVE here![T1 FIGHTING(T1.T1.T1.PeepeePooPoo!)", TextType.TEXT)
        ]

