#shuttle is used to move, copy, rename folders etc
#os module - operating system
import os

#checking what tasks can be assessed using os module
#print(dir(os))

#working directory (directory - folder, current folder in which the program is running)
#print(os.getcwd())

#creating a folder 
#os.mkdir("Sample Folder") 

#list the files/folders in a directory/folder
#path="C:/Users/Admin/OneDrive/Desktop"
#print(os.listdir(path))

#check if a file path exists or not
#path="C:/Users/Admin/OneDrive/Desktop/Python/Sample Folder/test2.txt"
#a=os.path.exists(path)
#print(a)

#split the file name and extension 
#path="C:/Users/Admin/OneDrive/Desktop/Python/Sample Folder/test.txt"
#file_name,ext=os.path.splitext(path)
#print("File name is : ",file_name)
#print("Extension of the file is : ",ext)
