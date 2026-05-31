from typing import MutableSequence
import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_props_01(self):
        node = HTMLNode(tag="url", props={"href": "https://github.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), " href=\"https://github.com\" target=\"_blank\"")

    def test_not_implemented(self):
        node = HTMLNode("p", "this is a paragraph")
        self.assertRaises(NotImplementedError, node.to_html)

    def test_repr(self):
        node = HTMLNode("p", "this is other paragraph")
        self.assertEqual(repr(node), "tag: p\nvalue: this is other paragraph\nchildren: None\nprops: None")


class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello World!")
        self.assertEqual(node.to_html(), "<p>Hello World!</p>")
        self.assertEqual(repr(node), "tag: p\nvalue: Hello World!\nprops: None")

    def test_raise_no_value(self):
        node = LeafNode("p", "")
        self.assertRaises(ValueError, node.to_html)

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div>\n  <span>child</span>\n</div>")
    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div>\n  <span>\n    <b>grandchild</b>\n  </span>\n</div>",
        )

    def test_exception_value(self):
        children: MutableSequence[HTMLNode] = [LeafNode("p", "this is a test")]
        node = ParentNode("", children)
        self.assertRaises(ValueError, node.to_html)

    def test_exception_children(self):
        node = ParentNode("", [])
        self.assertRaises(ValueError, node.to_html)


if __name__ == "__main__":
    unittest.main()
