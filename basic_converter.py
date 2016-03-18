#!/usr/bin/python

from xml.etree.ElementTree import Element, SubElement, tostring
import xml.etree.ElementTree as etree
from ElementTree_pretty import prettify

with open('xib/TableViewCell.xib', 'rt') as f:
    inputTree = etree.parse(f)

inputRoot = inputTree.getroot()
outputRoot = Element(inputRoot.tag, inputRoot.attrib)

dependencies = inputRoot.find('./dependencies')
outputRoot.append(dependencies)

print prettify(outputRoot)
