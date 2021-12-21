import os
from os.path import join, basename, splitext
import tkinter
from tkinter import simpledialog
from tkinter import filedialog
from PIL import Image
from datetime import datetime


def RepresentsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

#Folder Select dialog for choose images path
root = tkinter.Tk()
root.withdraw()

f_types = [('image', '*.jpg'),('image','*.png')]    
images = filedialog.askopenfilenames(parent=root,initialdir="/",title='Please select a Image', filetypes=f_types)


size = simpledialog.askstring(title="Test", prompt="please input new size of images")
if not RepresentsInt(size):
    raise Exception("Sorry, invalid input")
else:
    size = int(size)

print('\n \n')
print(images)

now = datetime.now()
current_time = now.strftime("%Y-%m-%d Time %H_%M_%S")

Imgs_Directory = join(os.path.dirname(images[0]), "new images" + str(size) + " " + str(current_time))
os.mkdir(Imgs_Directory)

for img in images:
    _img = Image.open(img)
    #_img = _img.resize((size, size), Image.ANTIALIAS)
    _img.thumbnail((size, size))
    _img.save(join(Imgs_Directory , basename(img)))

