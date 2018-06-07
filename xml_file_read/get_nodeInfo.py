from xml.dom import  minidom

#parse xml file
dom=minidom.parse('Class_info.xml')

root=dom.documentElement

print(root.nodeName)
print(root.nodeValue)
print(root.nodeType)


