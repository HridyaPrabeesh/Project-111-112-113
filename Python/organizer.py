#C112
import os
import shutil

from_dir="C:/Users/Admin/Downloads/Sample Folder"
to_dir="C:/Users/Admin/Downloads/Output Folder"

#print the files in from_dir
list_of_files=os.listdir(from_dir)
print(list_of_files)

#move all the folders from from_dir to to_dir  using shutil
#step 1: create a for loop, take one file after another and split the file name and ext
for file_name in list_of_files:
    name,ext=os.path.splitext(file_name)
    print(name)
    print(ext)

#step 2:if there is no ext " ", write code to skip the file
    if ext=="":
        continue
    if ext in [".gif", ".png", ".jpeg", ".jpg", ".jfif"]:
        path1=from_dir + "/" + file_name #Sample Folder/ImageFiles
        path2=to_dir + "/" + "ImageFiles"
        path3=to_dir+"/"+"ImageFiles"+"/"+file_name #Output Folder/ImageFiles/---.png
        
#step 3: check if the folder Image_file is existing/ otherwise create a new folder
        if os.path.exists(path2):
            print("Moving Files" + file_name)
            shutil.move(path1, path3)
        else:
            os.makedirs(path2)
            print("Moving Files" + file_name)
            shutil.move(path1, path3)


