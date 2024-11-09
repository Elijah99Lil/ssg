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


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)
        if self.children is not None:
            raise TypeError("LeafNode cannot have children.")

    def to_html(self):
        if self.value is None:
            raise ValueError("Value = None")
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
    

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
        if not self.children:
            raise ValueError("ParentNode must have a child. Otherwise it gets lonely.")
        
    def to_html(self):
        if self.tag is None:
            raise ValueError("Tag = None")
        result = f"<{self.tag}"
        if self.props:
            for key, value in self.props.items():
                result += f' {key}="{value}"'
        result += ">"
        for child in self.children:
            result += child.to_html()
        result += f"</{self.tag}>"
        return result
    
