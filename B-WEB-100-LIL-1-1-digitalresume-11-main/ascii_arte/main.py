from PIL import Image

ascii_char = ' .:-=+*#%@'

image = Image.open("mateo.jpg")
image = image.resize((100, 100)).convert("L")

for y in range(image.height):
    line = ""
    for x in range(image.width):
        grey = image.getpixel((x, y))
        index = grey * (len(ascii_char) - 1) // 255
        line += ascii_char[index] * 2
    print(line)