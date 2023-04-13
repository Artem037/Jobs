from PIL import Image, ImageChops


def im_crop(image):
    a = Image.new(image.mode, image.size, image.getpixel((0, 0)))
    d = ImageChops.difference(image, a)
    d = ImageChops.add(d, d, 2.0, -100)
    b = d.getbbox()
    if b:
        return image.crop(b)


im = Image.open('image.png')
im = im_crop(im)
im.save('res.png')
