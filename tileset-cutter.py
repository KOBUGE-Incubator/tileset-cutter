import os
import easygui as eg
from PIL import Image

image_file = eg.fileopenbox("Select Image")
image=Image.open(image_file)

file_dir = os.path.dirname(image_file)
file_name = os.path.splitext(os.path.basename(image_file))[0]

print file_name

tile_width = int(eg.enterbox("Tile Width in PX"))
tile_height = int(eg.enterbox("Tile Height in PX"))

tiles_x = image.size[0]/tile_width
tiles_y = image.size[1]/tile_height

count = 0

for y in range(tiles_y):
  for x in range(tiles_x):
    count += 1
    image.crop((x*tile_width,y*tile_height,x*tile_width+tile_width,y*tile_height+tile_height)).save(file_dir+"/"+file_name+"_tile_"+str(count)+".png")
