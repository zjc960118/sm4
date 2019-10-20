from PIL import Image

pku = Image.open('pku.jpg')

pku_rgba = pku.convert('RGBA')

pku_rgba.save('pku.rgba')

width1 = pku.size[0]
height1 = pku.size[1]

print(width1)
print(height1)

pku_rgb = pku_rgba.convert('RGB')

pku_rgb.save('pku_rgb.jpg')
