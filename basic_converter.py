#!/usr/bin/python

from xml.etree.ElementTree import Element, SubElement, tostring
import xml.etree.ElementTree as etree
from ElementTree_pretty import prettify

with open('xib/TableViewCell.xib', 'rt') as f:
    inputTree = etree.parse(f)
inputRoot = inputTree.getroot()

# Several things can be simply copied over
# The root "document" tag
outputRoot = Element(inputRoot.tag, inputRoot.attrib)

# "dependencies" tag
dependencies = inputRoot.find('dependencies')
outputRoot.append(dependencies)

# "objects" tag with only "placeholder" tags under it
outputObjects = SubElement(outputRoot, 'objects')
objects = inputRoot.find('objects')
for node in objects:
	if node.tag == 'placeholder':
		outputObjects.append(node)

# Grabbing objects that we'll need to modify / reshuffle to create collection view cell XIB
tableCell = objects.find('tableViewCell')
tableCellContentView = tableCell.find('tableViewCellContentView')
subviews = tableCellContentView.find('subviews')
constraints = tableCellContentView.find('constraints')

# Creating collection view cell element, to be built up later
collectionCell = Element('collectionViewCell')
outputObjects.append(collectionCell)

# Directly copying over some tags from tableCell to collectionCell
for tag in [ 'rect', 'autoresizingMask', 'color', 'connections', 'point' ]:
	node = tableCell.find(tag)
	collectionCell.append(node)
	
print prettify(outputRoot)
