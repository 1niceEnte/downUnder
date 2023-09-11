import glob
from PIL import Image

# read all jpeg
for filename in glob.glob("*.jpeg"):
    print(filename)

    # crop to 16/9
    width = 1024
    height = 1024 * 9 / 16
    offset = (width - height) / 2
    img = Image.open(filename)
    img = img.crop((0, offset, width, height + offset))

    # save
    img.save(filename + ".png")

