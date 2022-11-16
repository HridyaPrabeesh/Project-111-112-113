#C113
import sys
import time
import random

import os
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir="C:/Users/Admin/Downloads/Sample Folder"
to_dir="C:/Users/Admin/Downloads/Output Folder"

#segregate the extensions
dir_tree={
    "Image_Files":[".gif",".png",".jpg",".jpeg",".jfif"],
    "Doc_Files":[".pdf",".ppt",".doc",".pptx",".docx"],
    "Coding_Files":[".html",".js",".py",".css",".md"],
}

class FileMovementHandler(FileSystemEventHandler):
    def on_created(self, event):
        name, extension = os.path.splitext(event.src_path)
       
        time.sleep(1)

        for key, value in dir_tree.items():
            time.sleep(1)

            if extension in value:

                file_name = os.path.basename(event.src_path)
               
                print("Downloaded " + file_name)

                path1 = from_dir + '/' + file_name
                path2 = to_dir + '/' + key
                path3 = to_dir + '/' + key + '/' + file_name

                if os.path.exists(path2):

                    print("Directory Exists...")
                    print("Moving " + file_name + "....")
                    shutil.move(path1, path3)
                    time.sleep(1)

                else:
                    print("Making Directory...")
                    os.makedirs(path2)
                    print("Moving " + file_name + "....")
                    shutil.move(path1, path3)
                    time.sleep(1)

#initialize event handler/create an object of the class
event_handler=FileMovementHandler()

#initialize the observer
observer=Observer()

#scheduling then observer
observer.schedule(event_handler,from_dir,recursive=True)

#start the observer
observer.start()

try:
    while True:
        time.sleep(2)
        print("running...")

except KeyboardInterrupt:
    print("stopped")
    observer.stop()