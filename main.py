import os
import xml.etree.ElementTree as ET

def fix_from_txt(txt_path, annotation_root):
    with open(txt_path, "r") as f:
        error_files = f.readlines()
    for file in error_files:
        file_path = os.path.join(annotation_root, file.rstrip())
        tree = ET.parse(file_path)
        root = tree.getroot()
        root.find("filename").text = file.split('/')[1]
        root.find("folder").text = file[1:9]
        tree.write(file_path)

if __name__ == "__main__":
    # Change to where you have the "Annotation" folder stored
    annotation_path = os.path.join("StanfordDogs", "Annotation") 
    fix_from_txt("corrupt_files.txt", annotation_path)
