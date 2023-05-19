import time

import requests
import datetime
import json
import hashlib
import xml.dom.minidom
import os
import sys
from collections import defaultdict
import shutil
import requests
import cv2
import requests
from PIL import Image
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element

from common import common_file

def getPkgname(xmlpath):
    try:
        dom = xml.dom.minidom.parse(xmlpath)
        root = dom.documentElement

        elementLists = root.childNodes
        print(elementLists)

    except Exception as e:
        print("[ERROR] Fail to parse xml : " + xmlpath)
        return None

    for node in elementLists:
        if isinstance(node, xml.dom.minidom.Element):
            pkgname = node.getAttribute('package')
            if pkgname != 'com.android.systemui':
                return pkgname

    return None

def parseXmlFile(xmlpath):
    tree = ET.parse(xmlpath)
    root = tree.getroot()
    stack = []
    for child in root:
        print(child.tag, child.attrib)
        for c in child:
            print("----", c.tag, c.attrib)


class EventNode(object):
    def __init__(self, element, depth, node_id):
        self.element = element
        self.depth = depth
        self.node_id = node_id


def parseXmlFile2(xmlpath):
    tree = ET.parse(xmlpath)
    root = tree.getroot()
    queue = []
    idx = 1
    for child in root:
        queue.append([child, str(idx), 1])
        idx += 1

    clickable_nodes = {}
    editable_nodes = {}

    while queue:
        element, node_id, depth = queue.pop(0)
        child_count = 0
        idx = 1
        for child in element:
            queue.append([child, node_id + "-" + str(idx), depth + 1])
            child_count += 1
            idx += 1
        print("-" * 4 * depth, element.tag, child_count, node_id, element.attrib)

        if element.attrib.get("clickable", "").lower() == "true":
            node_class = element.attrib.get("class", "").lower()
            if "edittext" in node_class:
                editable_nodes[node_id] = EventNode(element=element, node_id=node_id, depth=depth)
            elif "button" in node_class:
                clickable_nodes[node_id] = EventNode(element=element, node_id=node_id, depth=depth)
            elif "imageview" in node_class:
                clickable_nodes[node_id] = EventNode(element=element, node_id=node_id, depth=depth)


    #for node_id, node in clickable_nodes.items():
    #    print(node_id, node.tag, node.attrib)

    return {
        "click": clickable_nodes,
        "edit": editable_nodes
        }


def parseXmlFile3(xmlstring):
    root = ET.fromstring(xmlstring)

    queue = []
    idx = 1
    for child in root:
        queue.append([child, str(idx), 1])
        idx += 1

    clickable_nodes = {}
    editable_nodes = {}

    while queue:
        element, node_id, depth = queue.pop(0)
        child_count = 0
        idx = 1
        for child in element:
            queue.append([child, node_id + "-" + str(idx), depth + 1])
            child_count += 1
            idx += 1
        print("-" * 4 * depth, element.tag, child_count, node_id, element.attrib)

        if element.attrib.get("clickable", "").lower() == "true":
            node_class = element.attrib.get("class", "").lower()
            if "edittext" in node_class:
                editable_nodes[node_id] = EventNode(element=element, node_id=node_id, depth=depth)
            elif "button" in node_class:
                clickable_nodes[node_id] = EventNode(element=element, node_id=node_id, depth=depth)
            elif "imageview" in node_class:
                clickable_nodes[node_id] = EventNode(element=element, node_id=node_id, depth=depth)
            else:
                clickable_nodes[node_id] = EventNode(element=element, node_id=node_id, depth=depth)


    #for node_id, node in clickable_nodes.items():
    #    print(node_id, node.tag, node.attrib)

    return {
        "click": clickable_nodes,
        "edit": editable_nodes
        }



if __name__ == '__main__':
    print('----------dataDealer----------')
    print(sys.path)
    print(common_file.FileType)

    #dirpath = "D:/code/data/droidbot_output/神庙逃亡2/u2"
    #xmlfile = "20230424_195618.xml"
    #xmlpath = os.path.join(dirpath, xmlfile)

    #getPkgname(xmlpath)

    #with open(xmlpath, "rb") as f:
    #    xml_string = f.read()
    #print(parseXmlFile3(xml_string))





