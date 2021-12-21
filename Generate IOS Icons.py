import os
from os.path import join
import tkinter
from tkinter import simpledialog
from tkinter import filedialog
from PIL import Image
from datetime import datetime



sizes = [57 ,114 ,120 ,180 ,72 ,144 ,76 ,152 ,167 ,29 ,60 ,40 ,20 ,58 ,87 ,80 ,50 ,100]

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
image_Directory = filedialog.askopenfilename(parent=root,initialdir="/",title='Please select a Image', filetypes=f_types)


now = datetime.now()
current_time = now.strftime("%Y-%m-%d Time %H_%M_%S")

Icons_Directory = join(os.path.dirname(image_Directory), 'Icons ' + str(current_time))
os.mkdir(Icons_Directory)

#create bat file to execute it for each image
for size in sizes:
    img = Image.open(image_Directory)
    img = img.resize((size, size), Image.ANTIALIAS)
    img.save(join(Icons_Directory , "Icon_" + str(size) + ".png"))
