from PIL import Image
import os
import sys

def resize_p(picpath, optpath):
    image = Image.open(picpath)

    # 调整图像大小为宽度为 500 像素，高度按比例缩放
    resized_image = image.resize((1080, int(image.size[1] * 1080 / image.size[0])))
    cropim = resized_image.crop((0, 0, 1080, 1440))
    im_gray = cropim.convert('L')
    im_gray.save(optpath)

def webp2jpeg(ipt):
    image = Image.open(ipt)
    image.save(f'{ipt[:-4]}jpg')
    os.remove(ipt)


# if __name__ == '__main__':
#     for i in os.listdir('.cache/童话般的你开始恋爱猛攻'):
#         for j in os.listdir('.cache/童话般的你开始恋爱猛攻/%s' %(i)):
#             try:
#                 webp2jpeg('.cache/童话般的你开始恋爱猛攻/%s/%s' %(i, j))
#             except:
#                 print(j)