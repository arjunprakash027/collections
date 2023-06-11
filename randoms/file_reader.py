import os
import re

def read_all_files(folder):
    """
    Reads all the files in the folder
    """
    for root,dirs,files in os.walk(folder):
        print("Root: ", root)
        print("Dirs: ", dirs)
        print("Files: ", files)
        print("=====================================")
        pattern = r"\.(exe|jpg|pyc)$"
        for file in files:
            print("File: ", file)
            match = re.search(pattern, file)
            if match:
                pass
            else:
                with open(os.path.join(root,file),"r") as f:
                    #print(f.read())
                    print(len(f.read()))
                    print("=====================================")

if __name__ == "__main__":
    path = "D:\projects\LARGE Projects\ipfs_uploader"
    read_all_files(path)