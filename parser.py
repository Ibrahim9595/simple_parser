import xml.etree.ElementTree as ET
from sys import argv
from os import mkdir, path
from shutil import rmtree
import json


def writeFile(path, val):
    """
    the function handles writing to a file 
    path:str (path to the o/p file)
    val: str (the value to be written in this file)
    """
    with open(path, 'w') as r:
        r.write(val)
        print('Created File ' + path)


def parseJson(path):
    """
    the function takes the path to ECU.json file and
    convert it to a list of files with name and type in each of them

    path: str (the path to teh ECU.json)
    """
    with open(path) as f:
        content = f.read()
        ecus = json.loads(content)
        for index, ecu in enumerate(ecus):
            buffer = ''
            for k in ecu:
                buffer += ecu[k] + '\n'

            writeFile('dist/ECU_' + str(index + 1) + '.txt', buffer)


def parseXML(path):
    """
    the function takes the path to ECU.xml file and
    convert it to a list of files with name and type in each of them

    path: str (the path to teh ECU.xml)
    """
    root = ET.parse(path).getroot()

    for index, children in enumerate(root):
        values = list(children)
        buffer = ''

        for val in values:
            buffer += val.text + '\n'

        writeFile('dist/ECU_' + str(index + 1) + '.txt', buffer)


if __name__ == "__main__":
    """
    the file takes the file path as cli argument
    """
    if len(argv) >= 2:
        temp = argv[1].split('.')
        if path.exists('dist'):
            rmtree('dist')

        mkdir('dist')

        if (len(temp) == 2 and temp[1] == 'json'):
            parseJson(argv[1])
        elif (len(temp) == 2 and temp[1] == 'xml'):
            parseXML(argv[1])
        else:
            print("Invalid arguments")
    else:
        print("Invalid arguments")
