# Make sure python PIL library is installed
# sudo apt install python3-pil
# python3-pil is already the newest version (6.1.0-1).

import PIL.Image
image = PIL.Image.open("image.jpg")
print(image.format)

