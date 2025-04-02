from textnode import TextType, TextNode
import os
import shutil

def refresh(source:str, destination:str):

    assert os.path.exists(source), f"Source Directory does not exist: {source}"
    if os.path.exists(destination):
        print(f"Deleting directory: {destination}")
        shutil.rmtree(destination)
    else:
        print(f"Warning: Destination Directory does not exist: {destination}")
    print(f"Creating Destination Directory: {destination}\n")
    os.mkdir(destination)

    def copy_files(src:str, dst:str):
        contents = os.listdir(src)
        for content in contents:
            src_path = f"{src}/{content}"
            dst_path = f"{dst}/{content}"
            if os.path.isfile(src_path):
                print(f"copying: {src_path}")
                print(f"to: {dst_path}\n")
                shutil.copy(src_path, dst_path)
            else:
                print(f"creating directory: {dst_path}\n")
                os.mkdir(dst_path)
                copy_files(src_path, dst_path)
        return
    copy_files(source, destination)
    


def main():
    node = TextNode("example text", TextType.LINK, "http://www.boot.dev")
    print(node)

    refresh("/Users/jayrgarg/projects/static-site-generator/static", "/Users/jayrgarg/projects/static-site-generator/public")

if __name__ == "__main__":
    main()
