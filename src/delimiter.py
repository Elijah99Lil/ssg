from htmlnode import HTMLNode
from textnode import TextNode, TextType
import re

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

def extract_markdown_images(text):
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    for alt_text, url in matches:
        if not url:
            raise Exception("Invalid markdown syntax")
    return matches

def extract_markdown_links(text):
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches

def split_nodes_image(old_nodes):
    result = []
    for node in old_nodes:
        if node.text_type == TextType.TEXT:
            images = extract_markdown_images(node.text)
            remaining_text = node.text
            for image_alt, image_url in images:
                sections = remaining_text.split(f"![{image_alt}]({image_url})", 1)
                if sections[0]:
                    result.append(TextNode(sections[0], TextType.TEXT))
                result.append(TextNode(image_alt, TextType.IMAGE, image_url))
                remaining_text = sections[1]
            if remaining_text:
                result.append(TextNode(remaining_text, TextType.TEXT))
        else:
            result.append(node)
    return result

def split_nodes_link(old_nodes):
    result = []
    for node in old_nodes:
        if node.text_type == TextType.TEXT:
            links = extract_markdown_links(node.text)
            remaining_text = node.text
            for link_text, link_url in links:
                sections = remaining_text.split(f"[{link_text}]({link_url})", 1)
                if sections[0]:
                    result.append(TextNode(sections[0], TextType.TEXT))
                result.append(TextNode(link_text, TextType.LINK, link_url))
                remaining_text = sections[1]
            if remaining_text:
                result.append(TextNode(remaining_text, TextType.TEXT))
        else:
            result.append(node)
    return result

