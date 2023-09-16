import os
from PIL import Image

cwd = os.path.split(os.getcwd())[1]
parent_dir = os.path.dirname(os.path.realpath(__file__))

# mode
mode = 0o666

fileList = os.listdir()

for file in fileList:
    originalFile = os.path.join(parent_dir, file)

    if file == os.path.basename(__file__):
        continue
    else:
        # Remove Metadata
        image = Image.open(originalFile)
        data = list(image.getdata())
        image_without_exif = Image.new(image.mode, image.size)
        image_without_exif.putdata(data)
        image_without_exif.save(os.path.join(parent_dir, file))
        image_without_exif.close()

        # Handle transparency
        im = Image.open(originalFile)
        bg = Image.new('RGB', im.size, 'white')
        bg.paste(im)
        bg.save(file.replace(".webp",".jpg"))
        os.remove(originalFile)
