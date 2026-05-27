from textnode import TextNode, TextType


if __name__ == "__main__":
    textnode = TextNode("this is some anchor text", TextType.LINK, "https://boot.dev")

    print(textnode)
