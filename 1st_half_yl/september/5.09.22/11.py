from PIL import Image

im = Image.open("image.bmp")
pixels = im.load()
x, y = im.size
k = x // 4
for i in range(1, 5):
    for j in range(1, 5):
        x1 = k * j - k
        y1 = k * i - k
        x2 = j * k
        y2 = i * k
        if i == j == 4:
            break
        im2 = im.crop((x1, y1, x2, y2))
        im2.save(f'image{i}{j}.bmp')
