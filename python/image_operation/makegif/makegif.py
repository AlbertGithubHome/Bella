# -*- encoding: utf-8 -*-
 
import imageio
import PIL
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw

standard_scale = 0.34
standard_crop = (0, 180, 1080, 1880)
input_image = [
    [(255,0,0),     100, (720, 900), "Screenshot_20190303-111401.jpg", "干啥呢？", standard_crop],
    [(255,255,0),   100, (10, 900), "Screenshot_20190303-111528.jpg", "欺负人！", standard_crop],
    [(255,0,255),   100, (10, 700), "Screenshot_20190303-163015.jpg", "我美吗？", standard_crop]
]

 
def create_gif(image_list, gif_name):
 
    frames = []
    for image_name in image_list:
        frames.append(imageio.imread(image_name))
    # Save them as frames into a gif 
    imageio.mimsave(gif_name, frames, 'GIF', duration = 3)
 
    return
 
def main():
    image_list = ['test_gif-0.png', 'test_gif-2.png', 'test_gif-4.png', 
                  'test_gif-6.png', 'test_gif-8.png', 'test_gif-10.png']
    gif_name = 'created_gif.gif'
    create_gif(image_list, gif_name)


def make_gif(gif_name):
    frames = []
    for x in range(len(input_image)):
        #for j in range(3):
        frames.append(imageio.imread('{0}.jpg'.format(x)))
    # Save them as frames into a gif 
    imageio.mimsave(gif_name, frames, 'GIF', duration = 1.2)


def add_text():

    count = 0;
    for text_info in input_image:
        #打开底版图片
        im1 = Image.open(text_info[3])

        # 在图片上添加文字 1
        font = ImageFont.truetype("C:\Windows\Fonts\STXINGKA.TTF", text_info[1])
        draw = ImageDraw.Draw(im1)
        draw.text(text_info[2], text_info[4], text_info[0], font = font)
        draw = ImageDraw.Draw(im1)
        if text_info[5]:
            im1 = im1.crop(text_info[5])  # (left, upper, right, lower)

        # 保存
        w, h = im1.size
        dImg = im1.resize((int(w * standard_scale),int(h * standard_scale)), Image.ANTIALIAS)  #设置压缩尺寸和选项，注意尺寸要用括号
        dImg.save("{0}.jpg".format(count)) #, quality=50
        count += 1

 
if __name__ == "__main__":
    add_text()
    make_gif('zyy.gif')
