# coding=utf-8
import requests
from lxml import etree
import threading
import queue
import time
import os
# 长度为100的对列
q = queue.Queue(maxsize=100)


class ReqThread(threading.Thread):
    def __init__(self, file_queue, save_path, data_type):
        threading.Thread.__init__(self)
        self.file_queue = file_queue
        self.save_path = save_path
        self.data_type = data_type

    def run(self):
        if self.data_type == "xml":
            get_file = self.file_queue.get()
            html = get_html_xml(get_file)
            save_file_xml(html, self.save_path, get_file)

        if self.data_type == "img":
            get_file = self.file_queue.get()
            html = get_html_img(get_file)
            save_file_img(html, self.save_path, get_file)


def get_html_xml(get_file):
    html = requests.get(
        os.path.join("http://192.168.10.156/taskban/%e6%95%b0%e6%8d%ae%e9%9b%86/annos-chanche/", get_file)).text
    return html


def request_xml_list():
    xml_req = requests.get("http://192.168.10.156/taskban/%e6%95%b0%e6%8d%ae%e9%9b%86/annos-chanche/")
    if xml_req.status_code:
        element = etree.HTML(xml_req.text, etree.HTMLParser())
        text = element.xpath('/html/body/table/tr/td/a/text()')
        text.pop(0)
        return text
    else:
        print("连接失败")
        return 0


def save_file_xml(html, save_path, get_file):
    try:
        with open(os.path.join(save_path, get_file), 'w+') as f:
            f.write(html)
            f.flush()
            f.close()
            print(get_file + "保存成功！！！！")
    except IOError as e:
        print(e)


def get_html_img(get_file):
    html = requests.get(
        os.path.join("http://192.168.10.156/taskban/%e6%95%b0%e6%8d%ae%e9%9b%86/images-chanche/", get_file)).content
    return html


def request_img_list():
    img_req = requests.get("http://192.168.10.156/taskban/%e6%95%b0%e6%8d%ae%e9%9b%86/images-chanche/")
    if img_req.status_code:
        element = etree.HTML(img_req.text, etree.HTMLParser())
        text = element.xpath('/html/body/table/tr/td/a/text()')
        text.pop(0)
        return text
    else:
        print("连接失败")
        return 0


def save_file_img(html, save_path, get_file):
    try:
        with open(os.path.join(save_path, get_file), 'wb') as f:
            f.write(html)
            f.flush()
            f.close()
            print(get_file + "保存成功！！！！")
    except IOError as e:
        print(e)


def xml_main():
    xml_list = request_xml_list()
    for i in xml_list:
        try:
            # 阻塞put队列数据 阻塞超时时间
            q.put(i, block=True, timeout=60)
            my_req = ReqThread(q, r"G:\光谷公司\shuuji\annos-chanche\\", "xml")
            # 不需要守护线程
            my_req.setDaemon(False)
            my_req.start()
        except queue.Full:
            print("队列已满,超时输出异常")
    while 1:
        if q.empty():
            time.sleep(3)
            print("xml执行完毕")
            break


def img_main():
    img_list = request_img_list()
    for i in img_list:
        try:
            # 阻塞put队列数据 阻塞超时时间
            q.put(i, block=True, timeout=60)
            my_req = ReqThread(q, r"G:\光谷公司\shuuji\images-chanche\\", "img")
            # 不需要守护线程
            my_req.setDaemon(False)
            my_req.start()
        except queue.Full:
            print("队列已满,超时输出异常")
    while 1:
        if q.empty():
            print("img执行完毕")
            break


if __name__ == '__main__':
    xml_main()
    img_main()
