from PIL import Image


# 打开一个jpeg图像文件，注意路径要改成你自己的:
im = Image.open('./图像处理/样例.jpeg')
# 获得图像尺寸:
w, h = im.size
# 缩放到50%:
im.thumbnail((w//2, h//2))
# 把缩放后的图像用jpeg格式保存！:
im.save('./图像处理/PIL缩放结果.jpeg', 'jpeg')
