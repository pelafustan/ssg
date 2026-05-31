from __future__ import annotations
from collections.abc import MutableSequence
from typing import override


class HTMLNode:
    def __init__(
            self, 
            tag: str | None = None,
            value: str | None = None,
            children: MutableSequence[HTMLNode] | None = None,
            props: dict[str, str | int] | None = None
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
                attr_string += f" {attr}=\"{val}\""

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
            tag: str,
            value: str,
            props: dict[str, str | int] | None = None
            ):
        super().__init__(tag, value, None, props)

    @override
    def to_html(self) -> str:
        if not self.value:
            raise ValueError("value is mandatory in LeafNode!")
        
        if not self.tag:
            return self.value

        return f"<{self.tag}>{self.value}</{self.tag}>"

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
            children: MutableSequence[HTMLNode],
            props: dict[str, str | int] | None = None
            ):
        super().__init__(tag, None, children, props)

    def to_html(self, level: int = 0) -> str:
        if not self.tag:
            raise ValueError("tag is mandatory in ParentNode!")

        if not self.children:
            raise ValueError("ParentNode cannot be parent without children!")

        # opening tag
        html_string = f"{' ' * 2 * level}<{self.tag}>"

        for child in self.children:
            if isinstance(child, LeafNode):
                html_string += f"\n{' ' * 2 * (level + 1)}" + child.to_html()

            if isinstance(child, ParentNode):
                html_string += "\n" + child.to_html(level + 1)
        
        html_string += f"\n{' ' * 2 * level}</{self.tag}>"
        return html_string

if __name__ == "__main__":
    children: MutableSequence[HTMLNode] = [LeafNode("li", f"subitem {x}") for x in range(1, 11)]
    parent = ParentNode("ul", children)
    sibling: MutableSequence[HTMLNode] = [LeafNode("li", f"item {x}") for x in range (1, 5)]
    sibling.append(parent)
    grandparent = ParentNode("ol", sibling)

    print(grandparent.to_html())
