class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props is None:
            return ""
        else:
            result = ""
            for key, value in self.props.items():
                result += f' {key}="{value}"'
        return result
    
    def __repr__(self):
        return f"Tag = {self.tag}, Value = {self.value}, Children = {self.children}, and Props = {self.props}"
    
example_node = HTMLNode(tag="p", value="hampter")
print(example_node)

text_node = HTMLNode(value="*jumps down from the top of the fridge* I'm gay!")
print(text_node)

link_node = HTMLNode(tag="a", props={"href": "https://google.com"})
print(link_node)
            