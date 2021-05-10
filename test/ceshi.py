# import yaml
#
# obj1 = {"name": "river", "age": 2019}
# obj2 = ["Lily", 1956]
# obj3 = {"gang": "ben", "age": 1963}
# obj4 = ["Zhuqiyu", 1994]
#
# y = yaml.dump([obj1, obj2, obj3, obj4])
# print(y)

import xml.sax
import xml.sax.handler


class XMLHandler(xml.sax.handler.ContentHandler):
    def __init__(self):
        self.buffer = ""
        self.mapping = {}

    def startElement(self, name, attributes):
        self.buffer = ""

    def characters(self, data):
        self.buffer += data

    def endElement(self, name):
        self.mapping[name] = self.buffer

    def getDict(self):
        return self.mapping


data = '<xml><return_code><![CDATA[SUCCESS]]></return_code><return_msg><![CDATA[OK]]></return_msg></xml>'

xh = XMLHandler()
xml.sax.parseString(data, xh)
ret = xh.getDict()
print(type(ret))
print(ret)
print(ret['return_code'])

