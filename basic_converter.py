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
cellId = tableCell.get('id')
cellClass = tableCell.get('customClass')
cellContentViewId = tableCellContentView.get('id')

#print cellId, cellContentViewId, cellClass

# Preparing attributes dictionary for collection view cell with a few generic settings, and important 'id' and 'customClass' settings
# Using 'id' matching that of tableViewCellContentView, so that constraints can work without alterations
# Using the same 'customClass' that we pick up from table view cell
collectionCellAttribs = {
	'opaque' : 'NO', 'clipsSubviews' : 'YES', 'multipleTouchEnabled' : 'YES', 'contentMode' : 'center',
	'id' : cellContentViewId, 'customClass' : cellClass
}
# Creating collection view cell element, to be built up later
collectionCell = Element('collectionViewCell', collectionCellAttribs)
outputObjects.append(collectionCell)

# Directly copying over some tags from tableCell to collectionCell
for tag in [ 'rect', 'autoresizingMask', 'color', 'connections', 'point' ]:
	node = tableCell.find(tag)
	collectionCell.append(node)
	
print prettify(outputRoot)
