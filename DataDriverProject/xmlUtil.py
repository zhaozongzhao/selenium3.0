from xml.etree import ElementTree

class ParseXML(object):
    def __init__(self,xmlpath):
        #指定输入文件路径
        self.xmlpath = xmlpath

    def getRoot(self):
        #打开要解析的xml文件
        tree = ElementTree.parse(self.xmlpath)
        #获取xml文件的根节点对象
        return tree.getroot()

    def findNodeByname(self,parentNode,nodeName):
        #通过界面名称返回节点对象
        nodes = parentNode.findall(nodeName)
        return nodes

    def getNodeOfChildText(self,node):
        #获取当前节点下所有子节点的节点名做key

       childenTextdict = {i.tag:i.text for i in list(node.iter())[1:] }
       return childenTextdict

    def getDataFromXml(self):
        root = self.getRoot()
        books = self.findNodeByname(root,'book')
        datalist = []
        for book in books:
            chlidrenText = self.getNodeOfChildText(book)
            datalist.append(chlidrenText)
        return  datalist

if __name__ == '__main__':
    xmlparh = ParseXML('F:\gitstorehouse\selenium3.0\DataDriverProject\TestData.xml')
    datas = xmlparh.getDataFromXml()
    for i in datas:
        print(i['name'],i['author'])
