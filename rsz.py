from PIL import Image
import os

def resize_p(picpath, optpath):
    image = Image.open(picpath)

    # 调整图像大小为宽度为 500 像素，高度按比例缩放
    resized_image = image.resize((800, int(image.size[1] * 800 / image.size[0])))
    resized_image.save(optpath)


if __name__ == '__main__':
    t = []
    for i in range(len(os.listdir('童話般的你開始了戀愛猛攻'))):
        t2 = []
        for j in range(len(os.listdir(f'童話般的你開始了戀愛猛攻/第{i+1:02}话'))):
            t2.append(f'{j}.jpg')
        t.append((f'第{i+1:02}话', t2))

    for i in t:
        if os.path.exists(f'.chche/童話般的你開始了戀愛猛攻/{i[0]}'):
            pass
        else:
            os.makedirs(f'.chche/童話般的你開始了戀愛猛攻/{i[0]}')
        for j in i[1]:
            resize_p(f'童話般的你開始了戀愛猛攻/{i[0]}/{j}', f'.chche/童話般的你開始了戀愛猛攻/{i[0]}/{j}')