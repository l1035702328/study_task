import requests
import os
from lxml import etree

img_req = requests.get("http://192.168.10.156/taskban/%e6%95%b0%e6%8d%ae%e9%9b%86/annos-chanche/")
if img_req.status_code:
    element = etree.HTML(img_req.text, etree.HTMLParser())
    text = element.xpath('/html/body/table/tr/td/a/text()')
    text.pop(0)
    print(text[0])
    print(os.path.join("http://192.168.10.156/taskban/%e6%95%b0%e6%8d%ae%e9%9b%86/annos-chanche/", text[0]))
asd_req = requests.get(os.path.join("http://192.168.10.156/taskban/%e6%95%b0%e6%8d%ae%e9%9b%86/annos-chanche/", text[0]))
asd_req = asd_req.text
print(asd_req)

with open(text[0], 'w') as f:
    f.write(asd_req)
    f.flush()
    f.close()
    print( "保存成功！！！！")

