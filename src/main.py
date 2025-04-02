from textnode import TextType, TextNode
from markdown import markdown_to_html_node, extract_title
import os
import shutil

def main():

    root = "/Users/jayrgarg/projects/static-site-generator"
    static = f"{root}/static"
    public = f"{root}/public"
    index_md = f"{root}/content/index.md"
    template = f"{root}/template.html"
    destination = f"{root}/public/index.html"

    refresh(static, public)
    generate_page(index_md, template, destination)

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

def generate_page(from_path:str, template_path:str, dest_path:str) -> None:
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, 'r') as from_file:
        from_txt = from_file.read()

    with open(template_path, 'r') as template_file:
        template_txt = template_file.read()

    title_str = extract_title(from_txt)
    content_str = markdown_to_html_node(from_txt).to_html()

    full_page_str = template_txt.replace("{{ Title }}", title_str).replace("{{ Content }}", content_str)

    with open(dest_path, 'w') as dest_file:
        dest_file.write(full_page_str)
    
    return


if __name__ == "__main__":
    main()
