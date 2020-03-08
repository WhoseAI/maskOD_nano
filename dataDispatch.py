import xml.etree.ElementTree as ET
import pickle
import os
from os import listdir, getcwd
from os.path import join

classes = ["Mask","No_Mask"]		# Changes classes to meet your dataset
workFolder  = os.getcwd()
dataFolder  = workFolder+"/dataset"
trainList   = workFolder+"/train.txt"	# Output the images list for training
testList    = workFolder+"/test.txt"	# Output the images list for testing
fileCount   = 0

#################### Code belows were not changed vs voc_label.py
def convert(size, box):
    dw = 1./(size[0])
    dh = 1./(size[1])
    x = (box[0] + box[1])/2.0 - 1
    y = (box[2] + box[3])/2.0 - 1
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x,y,w,h)

def convert_annotation(imageFileName):
    in_file = open('%s.xml'%(imageFileName))
    out_file = open('%s.txt'%(imageFileName), 'w')
    tree=ET.parse(in_file)
    root = tree.getroot()
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)

    for obj in root.iter('object'):
        difficult = obj.find('difficult').text
        cls = obj.find('name').text
        if cls not in classes or int(difficult)==1:
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text), float(xmlbox.find('ymax').text))
        bb = convert((w,h), b)
        out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')

##################### Code belows were modified by GPUS
trainListFile = open(trainList, 'w')
testListFile  = open(testList, 'w')

for file in os.listdir(dataFolder):
    filename, fileExt = os.path.splitext(file)
    fileExt = fileExt.lower()

    if(fileExt==".jpg" or fileExt==".png" or fileExt==".jpeg" or fileExt==".bmp"):
        imgFileName = os.path.join(dataFolder, filename)
        xmlFileName = os.path.join(dataFolder ,filename + ".xml")
        if(os.path.isfile(xmlFileName)):
            trainListFile.write(imgFileName+'\n')
            if( fileCount % 5 == 0 ):
                testListFile.write(imgFileName+'\n')
            fileCount += 1
            convert_annotation(imgFileName)

trainListFile.close()
testListFile.close()
