import os
import shutil


from_dir = "C:/Users/Admin/Downloads"
to_dir = "C:/Users/Admin/Desktop/downloaded_files"

list_of_files = os.listdir(from_dir)
print(list_of_files)