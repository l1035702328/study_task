# coding = utf-8'
# 读取XML文档
from PIL import Image
import os
import xml.dom.minidom
import yaml
from lxml import etree
path = r"G:\光谷公司\shuuji\annos-chanche\\"
xml_name_list = os.listdir(path)
print(xml_name_list)
# 打开xml文档
dom = xml.dom.minidom.parse(os.path.join(path, xml_name_list[1]))
dom_obj = dom.documentElement
file_name = dom_obj.getElementsByTagName("filename")[0].childNodes[0].data
# source
sources = dom_obj.getElementsByTagName("source")[0]
print(sources.getElementsByTagName("sourceImage")[0].childNodes[0].data)
print(sources.getElementsByTagName("sourceAnnotation")[0].childNodes[0].data)

#
dom_object = dom_obj.getElementsByTagName("object")[0]
print(dom_object.getElementsByTagName("name")[0].childNodes[0].data)
print(dom_object.getElementsByTagName("deleted")[0].childNodes[0].data)
print(dom_object.getElementsByTagName("verified")[0].childNodes[0].data)
try:
    print(dom_object.getElementsByTagName("occluded")[0].childNodes[0].data)
except:
    dom_object.getElementsByTagName("occluded")[0].nodeName
    print("None")













# p_img = Image.open(r'G:\光谷公司\shuuji\images-chanche\Bing_0000.jpg')
# w, h = p_img.size
# print(w,h)
