#!/usr/bin/env python3

import lxml.etree as ET

parser = ET.XMLParser(remove_blank_text=True)

tree = ET.parse('industry.xml', parser)

root = tree.getroot()

for elem in root.iter('interpolation-rule'):
    # print(elem)
    # print(elem.attrib)
    # print(f"Sub Elements: {list(elem.iter())}")
    to_value_sub_element = ET.Element("to-value")
    to_value_sub_element.text = "NA"
    elem.insert(1, to_value_sub_element)
    overwrite_policy_sub_element = ET.Element("overwrite-policy")
    overwrite_policy_sub_element.set("warn", "0")
    overwrite_policy_sub_element.text = "NEVER"
    elem.insert(2, overwrite_policy_sub_element)
    # ET.dump(elem)
    
tree.write('industry2.xml', pretty_print=True)