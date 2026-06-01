from htmlnode import LeafNode
from enum import Enum
from typing import override


class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"


class TextNode:
    def __init__(self, text: str | None, text_type: TextType, url: str | None = None):
        self.text: str | None = text
        self.text_type: TextType = text_type
        self.url: str | None = url

    @override
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, TextNode):
            return NotImplemented

        return (
            self.text == other.text
            and self.text_type == other.text_type
            and self.url == other.url
        )

    @override
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"


def text_node_to_html_node(text_node: TextNode) -> LeafNode:
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(None, text_node.text)
        case TextType.BOLD:
            return LeafNode("b", text_node.text)
        case TextType.ITALIC:
            return LeafNode("i", text_node.text)
        case TextType.CODE:
            return LeafNode("code", text_node.text)
        case TextType.LINK:
            return LeafNode("a", text_node.text, {"href": text_node.url or ""})
        case TextType.IMAGE:
            return LeafNode(
                "img", "", {"src": text_node.url or "", "alt": text_node.text or ""}
            )

    raise ValueError("Not a valid TextType!")  # pyright: ignore[reportUnreachable]
