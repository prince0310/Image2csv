from PIL import Image
import numpy as np
import sys
import os
import csv
import cv2 as cv

def createfilelist(mydir, fotmat = ".jpg" ):
    filelist = []
    print(mydir)
    for root,dirs,files in os.walk(mydir,topdown= False):
        for name in files :
            if name.endswith(fotmat):
                fullName = os.path.join(root,name)
                filelist.append(fullName)
        
    return filelist

myFilelist = createfilelist("/home/prince/dataset/AbNormal")              #path of files 

for file in myFilelist:
    print(file)
    img_file = Image.open(file)
    width,height = img_file.size
    format = img_file.format
    mode = img_file.mode
    img_grey = img_file.convert('L')

    value = np.asarray(img_grey.getdata(),dtype=np.int).reshape((img_grey.size[1],img_grey.size[0]))
    value = value.flatten()
    print(value)
    with open("image_to_csv.csv","a") as f :               #name of csv file
        writer = csv.writer(f)
        writer.writerow(value)

