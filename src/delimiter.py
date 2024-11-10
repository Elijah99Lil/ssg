from htmlnode import *
from textnode import *

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    result = []
    for node in old_nodes:
        if node.text_type == TextType.TEXT:
            first_delim = node.text.find(delimiter)
            if first_delim != -1:
                second_delim = node.text.find(delimiter, first_delim + len(delimiter))
                if second_delim != -1:
                    before = node.text[:first_delim]
                    middle = node.text[first_delim + len(delimiter): second_delim]
                    after = node.text [second_delim + len(delimiter):]
                    result.append(TextNode(before, TextType.TEXT))
                    result.append(TextNode(middle, text_type))
                    result.append(TextNode(after, TextType.TEXT))
                else: raise Exception("Invalid markdown syntax")    
            else: result.append(node)
        else: result.append(node)
    return result