import unittest
from textnode import TextNode, TextType


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
        node2= TextNode("this is a image", TextType.IMAGE, "https://placekittens.com/g/300/300")
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()
