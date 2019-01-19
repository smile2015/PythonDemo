# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     XmlUtilsDemo
   Description :
   Author :       Administrator
   date：          2019/1/15 0015
-------------------------------------------------
   Change Activity:
                   2019/1/15 0015:
-------------------------------------------------
"""
from com.mosorg.common.file.XmlUtils import XmlUtils

__author__ = 'Administrator'

import sys

reload(sys)
default_encoding = "utf-8"
if (default_encoding != sys.getdefaultencoding()):
    reload(sys)
    sys.setdefaultencoding(default_encoding)

file_path="C:\\mwb.mxl"
xmlUtils=XmlUtils()

#创建XML
rootNode=xmlUtils.createRootNode("Persons")

personNode=xmlUtils.createSubElement(rootNode,"Person")
nameNode=xmlUtils.createSubElement(personNode,"name")
xmlUtils.setNodeAttr(nameNode,"id","10001")
xmlUtils.setText(nameNode,"Jone")
ageNode=xmlUtils.createSubElement(personNode,"age")
xmlUtils.setNodeAttr(ageNode,"id","20001")
xmlUtils.setText(ageNode,"43")


personNode=xmlUtils.createSubElement(rootNode,"Person")
nameNode=xmlUtils.createSubElement(personNode,"name")
xmlUtils.setNodeAttr(nameNode,"id","10002")
xmlUtils.setText(nameNode,"小李")
ageNode=xmlUtils.createSubElement(personNode,"age")
xmlUtils.setNodeAttr(ageNode,"id","20002")
xmlUtils.setText(ageNode,"23")

xmlUtils.createNewXml(rootNode)
xmlUtils.saveXml(file_path)


#读取XML
xmlUtils.loadXml(file_path)
persionList=[]
person={}
personNodes=xmlUtils.getNodesByTagName("Person")
for personNode in personNodes:
    nameNode = xmlUtils.getNodeByTagName(personNode,"name")
    value=xmlUtils.getText(nameNode)
    person["name"] = value
    ageNode= xmlUtils.getNodeByTagName(personNode,"age")
    value = xmlUtils.getText(ageNode)
    person["age"]=value
    persionList.append(person)

print persionList


'''

import xml.etree.cElementTree as ET
new_xml = ET.Element("personinfolist")
personinfo = ET.SubElement(new_xml,"personinfo",attrib={"enrolled":"yes"})
name = ET.SubElement(personinfo,"name")
name.text = "Alex Li"
age = ET.SubElement(personinfo,"age",attrib={"checked":"no"})
sex = ET.SubElement(personinfo,"sex")
age.text = '56'
et = ET.ElementTree(new_xml)
et.write("test1.xml",encoding="utf-8",xml_declaration=True)
ET.dump(new_xml)


<?xml version='1.0' encoding='utf-8'?>
<personinfolist>
　　<personinfo enrolled="yes">
　　　　<name>Alex Li</name>
　　　　<age checked="no">56</age><sex />
　　</personinfo>
</personinfolist>
'''
