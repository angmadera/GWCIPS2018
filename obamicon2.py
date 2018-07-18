darkBlue = (0, 51, 76)
red = (217, 26, 33)
lightBlue = (112, 150, 158)
yellow = (252, 227, 166)


from PIL import Image

im = Image.open("puppy.img")

colorpixels = list(im.getdata())
list_length=len(colorpixels)


for i in range(list_length):
	#print(i)
	redapples = colorpixels[i][0]
	blueapples = colorpixels[i][1]
	greenapples = colorpixels[i][2]
	sum = redapples + blueapples + greenapples

	print(sum)
	if sum < 182:
		colorpixels[i] = darkBlue
	elif sum >= 182 and sum < 364:
		colorpixels[i] = red
	elif sum >= 364 and sum< 546:
		colorpixels[i] = lightBlue
	else:
		colorpixels[i]= yellow


im.putdata(colorpixels)

im.show()
