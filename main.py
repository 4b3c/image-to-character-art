from PIL import Image
import ctypes
user32 = ctypes.windll.user32
art_size = user32.GetSystemMetrics(0) / 24

while True:
	image = Image.open(input("Type or copy-paste the path to an image: "))
	image = image.resize((int(image.size[0] / (image.size[0] / art_size)), int(image.size[1] / (image.size[0] / art_size))))
	new_image = image.convert("RGB")

	if (input("Type 'invert' to invert the image (type anything else not to): ") == "invert"):
		characters = ("@$#*!;=~-, ")
	else:
		characters = (" ,-~=;!*#$@")

	for i in range(image.size[1]):
		for j in range(image.size[0]):
			color = new_image.getpixel((j, i))
			print(characters[int((((color[0] + color[1] + color[2]) / 3) - 5) / 25)], end = " ")

		print(" ")
