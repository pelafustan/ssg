import unittest
from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_no_equal(self):
        node = TextNode("This is a text node", TextType.CODE)
        node2 = TextNode("This a link node", TextType.LINK, "https://github.com")
        self.assertNotEqual(node, node2)

    def test_none(self):
        node = TextNode("this is a image", TextType.IMAGE)
        node2 = TextNode(
            "this is a image", TextType.IMAGE, "https://placekittens.com/g/300/300"
        )
        self.assertNotEqual(node, node2)

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node = TextNode("This text is bold", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This text is bold")

    def test_text_type_raise(self):
        node = TextNode("This doesn't have type", None)  # pyright: ignore[reportArgumentType]
        self.assertRaises(ValueError, text_node_to_html_node, node)


if __name__ == "__main__":
    unittest.main()
