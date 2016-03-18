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

# Grabbing background color and cell frame
backgroundColor = tableCellContentView.find('color')
frame = tableCell.find('rect')
# Setting them on collection view cell
collectionCell.append(backgroundColor)
collectionCell.append(frame)

# Adding 'size' tag to collection view cell, with dimensions based on 'rect' tag
size = Element('size', { 'key' : 'customSize', 'width' : frame.get('width'), 'height' : frame.get('height') })
collectionCell.append(size)

# Directly copying over some tags from tableCell to collectionCell
for tag in [ 'autoresizingMask', 'connections', 'point' ]:
	node = tableCell.find(tag)
	collectionCell.append(node)
	
# Copying constraints over
collectionCell.append(constraints)

# Adding 'view' tag under collectionViewCell, which will hold subviews
collectionCellContentView = etree.XML('<view key="contentView" opaque="NO" clipsSubviews="YES" multipleTouchEnabled="YES" contentMode="center"/>')

# Putting all custom subviews under the 'view' tag
collectionCellContentView.append(subviews)

# Setting the 'rect' tag under 'view' tag, thus making frame identical to that of collection view cell.
collectionCellContentView.append(frame)

# Setting autoresizing mask tag under 'view'
SubElement(collectionCellContentView, 'autoresizingMask', { 'key' : 'autoresizingMask' })

# Setting 'color' tag under 'view'
viewColor = etree.XML('<color key="backgroundColor" white="0.0" alpha="0.0" colorSpace="calibratedWhite"/>')
collectionCellContentView.append(viewColor)


print prettify(outputRoot)
