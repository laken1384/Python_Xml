import xml.etree.ElementTree as ET
import re
tree = ET.parse("/Users/laken/Desktop/python/main/20210810_CFE RTUs.xml")
root = tree.getroot()
rootNode=tree.getroot()
for i in root[0][0][0][0]:
    print(i.Name)