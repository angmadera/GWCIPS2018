darkBlue = (0, 51, 76)
red = (217, 26, 33)
lightBlue = (112, 150, 158)
yellow = (252, 227, 166)

from PIL import Image, ImageDraw, ImageFont

filename = input("Enter filename:  ")
im = Image.open(filename)

def load_img(filename):
  im = Image.open(filename)
  show_img(im)

def show_img(im):
  im.show()
  save_img(filename, im)

def save_img(filename, im):
  im.save(filename, "jpeg")

load_img(filename)

for i in pixels:
    print(i)

color_pixels = list(im.getdata())
list_length = len(color_pixels)

for i in range(list_length):
	red = color_pixels[i][0]
	blue = color_pixels[i][1]
	green = color_pixels[i][2]
	sum = red + blue + green

	print(sum)
	if sum < 182:
		color_pixels[i] = darkBlue
	elif sum >= 182 and sum < 364:
		color_pixels[i] = red
	elif sum >= 364 and sum < 546:
		color_pixels[i] = lightBlue
	else:
		color_pixels[i]= yellow

im.putdata(color_pixels)

im.show()
