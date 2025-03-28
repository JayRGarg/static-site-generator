from textnode import TextType, TextNode

def main():
    node = TextNode("example text", TextType.LINK, "http://www.boot.dev")
    print(node)

if __name__ == "__main__":
    main()
