#!/usr/bin/python

import sys
from xml.etree.ElementTree import Element, SubElement, tostring
import xml.etree.ElementTree as etree
from ElementTree_pretty import nibStyleXml

# Dealing with command-line arguments
if len(sys.argv) < 2 or len(sys.argv) > 3:
	print 'This script requires input file name as the first argument'
	print 'You can also provide output file name as the second argument. Otherwise output will default to "CollectionViewCell.xib"'
	sys.exit()

inputFileName = sys.argv[1]

# Setting the output file name to second argument or to the default value
if len(sys.argv) == 3:
	outputFileName = sys.argv[2]
else:
	outputFileName = 'CollectionViewCell.xib'

# Making sure that we can open the input file
try:
	inputFile = open(inputFileName, 'rt')
except:
	print 'Could not open the file ' + inputFileName
	sys.exit()

# Making sure that we can open the output file
try:
	outputFile = open(outputFileName, 'wt')
except:
	print 'Could not open the file ' + outputFileName
	sys.exit()


# Everything is good. Proceeding with actual functionality.
inputTree = etree.parse(inputFile)
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

# Directly copying over 'connections' and 'point' tags from tableCell to collectionCell
collectionCell.append(tableCell.find('connections'))
collectionCell.append(tableCell.find('point'))
	
# Adding 'autoresizingMask' tag typical of collection view cell
mask = etree.XML('<autoresizingMask key="autoresizingMask" flexibleMaxX="YES" flexibleMaxY="YES"/>')
collectionCell.append(mask)

# Copying constraints over
collectionCell.append(constraints)

# Adding 'view' tag under collectionViewCell, which will hold subviews
collectionCellContentView = etree.XML('<view key="contentView" opaque="NO" clipsSubviews="YES" multipleTouchEnabled="YES" contentMode="center"/>')
collectionCell.append(collectionCellContentView)

# Putting all custom subviews under the 'view' tag
collectionCellContentView.append(subviews)

# Setting the 'rect' tag under 'view' tag, thus making frame identical to that of collection view cell.
collectionCellContentView.append(frame)

# Setting autoresizing mask tag under 'view'
SubElement(collectionCellContentView, 'autoresizingMask', { 'key' : 'autoresizingMask' })

# Setting 'color' tag under 'view'
viewColor = etree.XML('<color key="backgroundColor" white="0.0" alpha="0.0" colorSpace="calibratedWhite"/>')
collectionCellContentView.append(viewColor)

# Updating UI elements actions to connect to collection view cell correctly
actions = subviews.findall('.//action')
for action in actions:
	if action.get('destination') == cellId:
		action.set('destination', cellContentViewId)
	
# Updating UI elements delegate outlets to connect to collection view cell correctly
outlets = subviews.findall('.//outlet')
for outlet in outlets:
	if outlet.get('destination') == cellId:
		outlet.set('destination', cellContentViewId)


outputFile.write(nibStyleXml(outputRoot))
outputFile.close()