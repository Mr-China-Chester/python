# -*- coding: utf-8 -*-
from PIL import Image  # 导入image
import argparse  # 导入argparse


def get_char(r, g, b, alpha=256):  # 灰度值 将像素rgb转化成灰度值 灰度值：指黑白图像中点的颜色深度，范围一般从0到255，白色为255，黑色为0，故黑白图片也称灰度图像
    if alpha == 0:  # 会有空白的地方 加判断
        return " "
    gary = (2126 * r + 7152 * g + 722 * b) / 10000  # 转换rgb成字符画 用整形运算不用浮点型运算因为比较慢 灰度值
    ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
    # ascii_char = list("~!@#$%^&*()_+qwerty{}UIO|DSA;dsf>vxc<zcz?123456789/*-+QWERTYUIOPOPHFDACXZCXzc,\"^`'. ")
    # 颜色区间256 现在有70 字符串可以自己看着加 字符串
    x = int((gary / (alpha + 1.0)) * len(ascii_char))  # 加int取整处理 将灰度值与字符串去对应  字符串与灰度值关系（（灰度值 / 256 ） = （x /字符串长度）） 加1 是为了保证附属值
    return ascii_char[x]  # 返回灰度值


def write_file(out_file_name, content):  # 创建一个文件 打开文件位置据点
    with open(out_file_name, "w") as f:  # 打开文件
        f.write(content)  # 写入文件


def main(file_name="test.jpg", width=80, height=80, out_file_name="out_file"):  # 获取图片的类型
    text = ""  # 对text进行初始化操作
    im = Image.open(file_name)  # 用image库打开这个图片 获取这个图片的对象
    im = im.resize((width, height), Image.NEAREST)  # 改变这个图片的大小 和这个质量
    for i in xrange(height):
        for j in xrange(width):
            content = im.getpixel((j, i))  # getpixel 返回一个值到xy里面去 然后这个值作为一个django ，接受一个元组类型xy 返回images对象元组 (0, 80, 116, 255) (0, 160, 233, 255)  x在前面y在后面
            text += get_char(*content)  # get_char把元组换换成字符    *解元方法
        text += "\n"  # 加上换行符 每一行都会加上
    print text
    write_file(out_file_name, text)
    # print content
    # im.save("a.jpg")


def parse_param():
    # 参数解析 解析命令行参数
    parser = argparse.ArgumentParser()
    # input_file
    parser.add_argument("input_file")  # 输入文件的名字
    parser.add_argument("out_file")  # 输出文件的名字
    parser.add_argument("--width", type=int, default=80)  # default 这个可以改变字符画的大小
    parser.add_argument("--height", type=int, default=80)
    args = parser.parse_args()  # 完成解析
    width, height, in_file, out_file = args.width, args.height, args.input_file, args.out_file  # 赋值
    return width, height, in_file, out_file


if __name__ == '__main__':
    width, height, in_f, out_f = parse_param()
    main(file_name="ascii_dora.png", width=width, height=height, out_file_name=out_f)  # 这里可以要改变图片


