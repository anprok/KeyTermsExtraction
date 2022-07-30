#  write your code here
from lxml import etree

xml_file = "data/dataset/input.txt"
root = etree.parse(xml_file).getroot()
print(" ".join([member.get('name') for member in root[0]]))