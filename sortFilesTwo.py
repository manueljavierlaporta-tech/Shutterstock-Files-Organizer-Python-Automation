import os
import shutil
from tkinter import Tk, filedialog, messagebox

window = Tk()
window.withdraw()

counter = 0
#--- Folder route
route = filedialog.askdirectory(title="Select destination folder")
filesRoute = filedialog.askdirectory(title="Select source folder")

os.chdir(route)

#--- If needed, create Shutterstock folder
fatherFolder = "Shutterstock"

if not os.path.exists(fatherFolder):
    os.makedirs(fatherFolder)
else:
    print("This folder already exists")

newFolderRoute = route + "/" + fatherFolder + "/"
#--- If needed, create Images and Videos folders
extensions = {
    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".svg": "Images",
    ".mov": "Videos",
    ".mp4": "Videos"
}

for folder in set(extensions.values()):
    folderRoute = os.path.join(newFolderRoute, folder)

    if not os.path.exists(folderRoute):
        os.makedirs(folderRoute)
    else:
        print(folder + " already exists")

for file in os.listdir(filesRoute):
    fileRoute = os.path.join(filesRoute, file)

    if os.path.isfile(fileRoute):
        name,ext = os.path.splitext(fileRoute)
        name = os.path.basename(name)
        ext = ext.lower()

        if ext in extensions and name.startswith("shutterstock"):
            counter += 1
            destination = os.path.join(newFolderRoute, extensions[ext], file)
            shutil.move(fileRoute, destination)

if counter != 0:
    messagebox.showinfo("Finished", "Files organized successfully!")
else:
    messagebox.showinfo("Finished", "You don't have any file to be organized")

