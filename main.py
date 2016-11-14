#PyArt
from PIL import Image
import math

im = []
for i in range(0, 512):
    ii = []
    for j in range(0, 512):
        ii.append(int(j/(i+1))) #int(i*j/100) + int((i%(j+1))) + 10
    im.append(ii)

img = Image.new('RGB', (512, 512), "black")
pixels = img.load()

for i in range(img.size[0]):
    for j in range(img.size[1]):
        pixels[i,j] = (im[i][j], im[j][i], int(math.sin(i*j)*j))

img.show()
