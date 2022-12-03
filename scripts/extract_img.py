import sys 
from PIL import Image, ImageColor

if (len(sys.argv) <= 1):
  print("[?] Usage: " + sys.argv[0] + " file.bin offset")
  sys.exit(-1)

file_path = sys.argv[1]
offset = int(sys.argv[2],base=16)

with open(file_path,"rb") as reader:
  file = reader.read()

h = 1024
w = 160

file = file[offset:]
img = Image.new('RGBA', (w,h))

for y in range(0,h):
  for x in range(0,w):
    try:
      img.putpixel((x,y) , (file[0], file[1], file[2], 255))
    except: 
      img.putpixel((x,y) , (0, 0, 0, 255))
    file = file[3:]

img.show()