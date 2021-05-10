class Book(object):
    def __init__(self,bname=None,price=None,bookWriter=None):
        self.bname=bname
        self.price=price
        self.bookWriter=bookWriter
    def __str__(self):
        return '书名'+self.bname+'\t价格'+self.price+"\t作者"+self.bookWriter
books = []
doc=parse('xml1.xml')
# 得到根节点
root=doc.documentElement
book=root.getElementsByTagName('book')
for b in book:
    bname=b.getElementsByTagName('bookname')[0].childNodes[0].data
    price=b.getElementsByTagName('bookPrice')[0].childNodes[0].data
    bookWriter=b.getElementsByTagName('bookWriter')[0].childNodes[0].data
    books.append(Book(bname,price,bookWriter))
print('书名：\t\t价格：\t作者')
for book in books:
    print(book)