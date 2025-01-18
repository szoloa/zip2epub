from PIL import Image, ImageDraw, ImageFont
import time

title = '日思录第001篇'

# 图片名称
img = './img/cover.jpg'  # 图片模板
new_img = 'output.png'  # 生成的图片

# 设置字体样式
font_type = 'simsun.ttc'
font_medium_type = 'simsun.ttc'
header_font = ImageFont.truetype(font_medium_type, 55)
title_font = ImageFont.truetype(font_medium_type, 45)
font = ImageFont.truetype(font_type, 24)
color = "#000000"
width, height = (1080, 1440)

image = Image.new("RGB", (width, height), '#ffffff')
draw = ImageDraw.Draw(image)

length = draw.textlength(text=title, font=title_font)
# 标题
title_x = 300
title_y = 80
draw.text((540-length/2, title_y), u'%s' % title, color, title_font)

im_gray = cropim.convert('L')

# 生成图片
im_gray.save(new_img, 'png')
