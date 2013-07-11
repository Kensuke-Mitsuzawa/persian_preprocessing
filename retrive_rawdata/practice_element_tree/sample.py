#encoding: utf-8
import codecs;
from xml.etree import ElementTree;
#f=codecs.open('sample.xml', 'r', 'utf-8');
dom=ElementTree.parse('sample.xml');
print dom.findtext(u'//段');
items=dom.findall(u'//アイテム');
for item in items:
    print item.attrib['title']
