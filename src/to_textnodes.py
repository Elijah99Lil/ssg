from textnode import TextNode, TextType
from delimiter import split_nodes_delimiter, split_nodes_image, split_nodes_link

def text_to_textnodes(text):
    if not text:
         return [TextNode("", TextType.TEXT)]
    node = TextNode(text, TextType.TEXT)
    bold_delim = split_nodes_delimiter([node], "**", TextType.BOLD)
    italic_delim = split_nodes_delimiter(bold_delim, "*", TextType.ITALIC)
    code_delim = split_nodes_delimiter(italic_delim, "`", TextType.CODE)
    image_delim = split_nodes_image(code_delim)
    final_delim = split_nodes_link(image_delim)
    return final_delim

