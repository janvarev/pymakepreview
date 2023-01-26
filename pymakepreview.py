from PIL import ImageGrab

import sys
import os

version = "1.0"

def end_err(err:str):
    print("Error: ", err)
    sys.stdin.readline()
    exit(-1)

print("Running pymakepreview v{0}...".format(version))
print("Original author: Janvarev Vladislav, 2023")
print("*"*60)

res = sys.argv[1:]

print("Arguments:", res)
if len(res) < 2:
    end_err("No input file or no template - where to save, and what template apply?")

template = res[0]
filepath = res[1]

img = ImageGrab.grabclipboard()

if img is None:
    end_err("No image in clipboard")

#print(os.path.splitext("/path/to/some/file.txt")[0])
file_without_ext = os.path.splitext(filepath)[0]
resfilepath = template.format(f=filepath,fnoext=file_without_ext)

img_format = ""
if resfilepath.lower().endswith(".png"):
    img_format = "PNG"
if resfilepath.lower().endswith(".jpg"):
    img_format = "JPG"


if img_format == "":
    #end_err("Can't detect if PNG or JPG file must be")
    img_format = "PNG"

print("Res file: ",resfilepath)
print("Res format: ",img_format)
#sys.stdin.readline()

# Save the image to disk
img.save(resfilepath, img_format)

