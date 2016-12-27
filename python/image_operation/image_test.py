# image thumbnail
from PIL import Image

im = Image.open('test.jpg')

w,h = im.size
print('Original image size: %s:%s' % (w, h))

im.thumbnail((w//2, h//2))

im.save('thumbanil.jpg', 'jpeg')