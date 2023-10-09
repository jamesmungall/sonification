from PIL import Image, ImageOps

filename = "solar SDO 193A 2023-10-09.jpg"
with Image.open(filename) as img:
     img.load()
img = ImageOps.grayscale(img)
pix_vals = list(img.getdata())

# find frequency of dark areas
n_dark_pixels = 0
for i in range(0, len(pix_vals)):
    if pix_vals[i] < 4:
        n_dark_pixels = n_dark_pixels + 1
print('number of black pixels is ', n_dark_pixels)
