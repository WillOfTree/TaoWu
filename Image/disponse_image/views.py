# coding=utf-8
import os
import time
import math

from PIL import Image

from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import FileResponse


def index(re):
    return render(re, "disponse/index.html")


def fixed_size(request):
    """
    处理上传文件类
    POST['width]:宽
    POST['height']:高
    """

    if request.method == "POST":

        f = request.FILES['files']  # 得到文件
        w = int(request.POST.get("width", 295))  # 得到宽
        h = int(request.POST.get("height", 413))  # 得到高

        if h > 1 and w > 1:
            if f.content_type == "image/png" or f.content_type == "image/jpeg":
                fname,  info = rename(f.name)  # 给文件重名，指定保存目录
                # 文件写入
                with open(fname, 'wb') as pic:
                    for c in f.chunks():  # 获取数据
                        pic.write(c)  # 在指定文件中写入

                # 处理照片
                fxim = FixedImage()  # 调用照片处理类
                fxim.fixed_size(fname, h, w)  # 返回文件名
            else:
                info = "我只认识jpg,png的照片哦"
        else:
            info = "宽高不能小于1"
    else:
        info = ""

    return HttpResponse(info)


def resize_weight(request):
    """
    调整文件质量
    """
    if request.method == "POST":

        f = request.FILES['files']  # 得到文件
        w = int(request.POST.get("weight"))  # 得到宽

        if w > 0 and w < 100:
            if f.content_type == "image/png" or f.content_type == "image/jpeg":
                fname,  info = rename(f.name)  # 给文件重名，指定保存目录
                # 文件写入
                with open(fname, 'wb') as pic:
                    for c in f.chunks():  # 获取数据
                        pic.write(c)  # 在指定文件中写入

                # 处理照片
                fxim = FixedImage()  # 调用照片处理类
                fxim.resize_weight(fname, w)  # 返回文件名
            else:
                info = "我只认识jpg,png的照片哦"
        else:
            info = "输入的数不符合要求哦"
    else:
        info = ""

    return HttpResponse(info)


def download(request, filename):
    """
    下载功能
    filename:下载的文件名
    """
    downpath = settings.MEDIA_ROOT + "/down/" + filename

    file = open(downpath, 'rb')
    response = FileResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="' + filename + '"'
    # response["Set-Cookie"] = "fileDownload=true; path=/"
    return response


def rename(name):
    """
    重名名
    name：名称
    return : 元组(文件目录，下载目录)
    """

    postfix = os.path.splitext(name)[1]  # 获取文件后缀
    ti = str(round(time.time() * 1000))  # 获取时间戳
    filename = ti + postfix  # 文件名
    fname = settings.MEDIA_ROOT + "/media/" + filename  # 路径加文件名
    # downfile = "image/down/" + filename
    return (fname, filename)


class FixedImage(object):

    PATH = settings.MEDIA_ROOT

    def fixed_size(self, path, height, width):
        """
        修改尺寸
        path: 路径
        height: 高（像素）
        width： 宽（像素）
        return:文件名
        """
        (width, height) = self.validate(width, height)

        im = Image.open(path)
        # 按指定尺寸缩放图片
        out = im.resize((width, height), Image.ANTIALIAS)
        save_path = self.rename(path)
        out.save(save_path, quality=45, subsampling=0)

    def resize_by_height(self, path, height):
        """
        根据高等比缩放
        height:高(像素)
        """
        (width, height) = self.validate(width=1, height=height)
        resize_auto(path, height)

    def resize_by_width(self, path, width):
        """
            根据宽等比缩放
            width:宽（像素）
        """
        (width, height) = self.validate(width=width, height=1)
        resize_auto(path, width)

    def resize_weight(self, path, weight):
        """
        修改图片占用字节大小
        weight : 字节（单位K）
        """

        im = Image.open(path)
        if weight > 95:
            percentage = 95
        elif weight < 1:
            percentage = 1
        else:
            percentage = weight

        save_name = self.rename(path)
        im.save(save_name, quality=percentage, subsampling=0)

    def resize_auto(self, path, height=1, width=1):
        """
        等比缩放
        path:路径
        height:高（百分比）
        width：宽（百分比）
        """
        (width, height) = self.validate(height, width)

        im = Image.open(path)
        (x, y) = im.size
        # 计算大小
        x_tem = math.ceil(x*width)
        y_tem = math.ceil(y*height)

        out = im.resize((x_tem, y_tem), Image.ANTIALIAS)
        save_path = self.rename(path)
        out.save(save_path, quality=45, subsampling=0)

    def rename(self, path):
        """
        重新生成文件名
        path:路径
        """
        path_tem = os.path.join(self.PATH, "down")  # 组成下载目录
        # postfix = os.path.splitext(path)[1] #后缀名
        filename = os.path.split(path)[1]  # 获取文件名
        save_path = os.path.join(path_tem, filename)  # 指向下载目录

        return save_path

    def validate(self, width, height):
        """
        验证宽高是否符合条件
        height:高（不能为0）
        width：宽（不能为0）
        """
        if height == 0 or height == "":
            height = 1
        if width == 0 or width == "":
            width = 1

        return (width, height)
