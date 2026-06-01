from typing import override


class HTMLNode:
    def __init__(
        self,
        tag: str | None = None,
        value: str | None = None,
        children: list["HTMLNode"] | None = None,
        props: dict[str, str | int] | None = None,
    ):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self) -> str:
        raise NotImplementedError("This must be implemented by derived classes!")

    def props_to_html(self) -> str:
        attr_string = ""
        if self.props:
            for attr, val in self.props.items():
                attr_string += f' {attr}="{val}"'

        return attr_string

    @override
    def __repr__(self):
        return (
            f"tag: {self.tag if self.tag else 'None'}\n"
            f"value: {self.value if self.value else 'None'}\n"
            f"children: {len(self.children) if self.children else 'None'}\n"
            f"props: {len(self.props) if self.props else 'None'}"
        )


class LeafNode(HTMLNode):
    def __init__(
        self,
        tag: str | None,
        value: str | None,
        props: dict[str, str | int] | None = None,
    ):
        super().__init__(tag, value, None, props)

    @override
    def to_html(self) -> str:
        if not self.value:
            raise ValueError("value is mandatory in LeafNode!")

        if not self.tag:
            return self.value

        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    @override
    def __repr__(self):
        return (
            f"tag: {self.tag if self.tag else 'None'}\n"
            f"value: {self.value if self.value else 'None'}\n"
            f"props: {len(self.props) if self.props else 'None'}"
        )


class ParentNode(HTMLNode):
    def __init__(
        self,
        tag: str,
        children: list["HTMLNode"],
        props: dict[str, str | int] | None = None,
    ):
        super().__init__(tag, None, children, props)

    def to_html(self) -> str:
        if not self.tag:
            raise ValueError("tag is mandatory in ParentNode!")

        if not self.children:
            raise ValueError("ParentNode cannot be parent without children!")

        # opening tag
        html_string = f"<{self.tag}{self.props_to_html()}>"

        for child in self.children:
            # leaf nodes are simply added to the final string
            if isinstance(child, LeafNode):
                html_string += child.to_html()

            # parent nodes use recursion to add its entries to final string
            if isinstance(child, ParentNode):
                html_string += child.to_html()

        # closing tag
        html_string += f"</{self.tag}>"
        return html_string
