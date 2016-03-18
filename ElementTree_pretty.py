from xml.etree import ElementTree
from xml.dom import minidom

def prettify(elem):
    """Return a pretty-printed XML string for the Element.
    """
    rough_string = ElementTree.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string).toprettyxml(indent="  ")
    return '\n'.join([line for line in reparsed.split('\n') if line.strip()])