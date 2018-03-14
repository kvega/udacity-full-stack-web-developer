import os
def rename_files():
    # define the root folder
    root = r"/home/kvega/Projects/full-stack-web-developer/section-1/prank"
    # (1) get file names from a folder
    file_list = os.listdir(root)
    print(file_list)
    
    # (2) for each file, rename filename
    translation_table = str.maketrans("0123456789", "          ", "0123456789")
    for file_name in file_list:
        print("Old Filename: " + file_name)
        print("New Filename: " + file_name.translate(translation_table))
        os.rename(os.path.join(root, file_name),
                  os.path.join(root, file_name.translate(translation_table)))
       
rename_files()
