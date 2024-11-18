import unittest
from to_textnodes import text_to_textnodes
from textnode import TextNode, TextType

class TestText_To_TextNodes(unittest.TestCase):

#Text to TextNode Tests

    def test_text_to_textnodes(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        result = text_to_textnodes(text)
        assert result == [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ]

    def test_empty_strings(self):
        text = ""
        result = text_to_textnodes(text)
        assert result == [
            TextNode("", TextType.TEXT)
        ]

    def test_consecutive_formatting(self):
        text = "Hi *I'm***PAUL**"
        with self.assertRaises(Exception) as context:
            result = text_to_textnodes(text)
        self.assertEqual(str(context.exception), "Invalid markdown syntax")

    def test_nested_formatting(self):
        text = "AYO! *I'm **NESTED** ova here!*"
        with self.assertRaises(Exception) as context:
            result = text_to_textnodes(text)
        self.assertEqual(str(context.exception), "Invalid markdown syntax")

    def test_incomplete_tags(self):
        text = "SNIFFS **COCAIN JR. . . . RJRJRJJRJRJRJJEjrjerijererkemrmemroiejirjeijeerejr"
        with self.assertRaises(Exception) as context:
            result = text_to_textnodes(text)
        self.assertEqual(str(context.exception), "Invalid markdown syntax")

    def test_plain_text(self):
        text = "ME MONKIEEEEEE"
        result = text_to_textnodes(text)
        assert result == [
            TextNode("ME MONKIEEEEEE", TextType.TEXT)
        ]

    def test_special_characters(self):
        text = "HOLY $#$ IM GONNA ^#(%)"
        result = text_to_textnodes(text)
        assert result == [
            TextNode("HOLY $#$ IM GONNA ^#(%)", TextType.TEXT)
        ]

    def test_long_text(self):
        text = "I'm heading back to Colorado tomorrow after being down in Santa Barbara over the weekend for the festival there. I will be making October plans once there and will try to arrange so I'm back here for the birthday if possible. I'll let you know as soon as I know the doctor's appointment schedule and my flight plans. She wanted rainbow hair. That's what she told the hairdresser. It should be deep rainbow colors, too. She wasn't interested in pastel rainbow hair. She wanted it deep and vibrant so there was no doubt that she had done this on purpose."
        result = text_to_textnodes(text)
        assert result == [
            TextNode("I'm heading back to Colorado tomorrow after being down in Santa Barbara over the weekend for the festival there. I will be making October plans once there and will try to arrange so I'm back here for the birthday if possible. I'll let you know as soon as I know the doctor's appointment schedule and my flight plans. She wanted rainbow hair. That's what she told the hairdresser. It should be deep rainbow colors, too. She wasn't interested in pastel rainbow hair. She wanted it deep and vibrant so there was no doubt that she had done this on purpose.", TextType.TEXT)
        ]

    def test_whitespace_handling(self):
        text = "          text          "
        result = text_to_textnodes(text)
        assert result == [
            TextNode("          text          ", TextType.TEXT)
        ]

    def test_invalid_images(self):
        text = "This a pic ![dog]()"
        result = text_to_textnodes(text)

    def test_invalid_images(self):
        text = "This a pic ![dog]()"
        with self.assertRaises(Exception) as context:
            result = text_to_textnodes(text)
        self.assertEqual(str(context.exception), "Invalid markdown syntax")

    def test_non_matching_ends(self):
        text = "This is the end of our **journey and*"
        with self.assertRaises(Exception) as context:
            result = text_to_textnodes(text)
        self.assertEqual(str(context.exception), "Invalid markdown syntax")


