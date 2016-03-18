from xml.etree import ElementTree
from xml.dom import minidom

def prettify(elem):
    """Return a pretty-printed XML string for the Element.
    """
    rough_string = ElementTree.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string).toprettyxml(indent="  ")
    nonEmptyLines = [line for line in reparsed.split('\n') if line.strip()]
    
    # Discarding the first line, which is '<?xml version="1.0" ?>
    if len(nonEmptyLines) > 0:
    	del nonEmptyLines[0]
    	
    return '\n'.join(nonEmptyLines)
    
def nibStyleXml(elem):
	xmlHeaderLine = '<?xml version="1.0" encoding="UTF-8" standalone="no"?>'
	return xmlHeaderLine + '\n' + prettify(elem)