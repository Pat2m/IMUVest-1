#!/usr/bin/env python3

import time
from sensorClass import *
from kneelingAlgorithm import *
from userinput import *
import sys

#1: import data from file
#2: get file number of rows
#3: start loop
#4: put data from line into objects
#5: angle calcs
#6: knee calcs
#Time step .02

NMKG = 0.15

objRThigh = sensorObject("RT")
objRShank = sensorObject("RS")
objLThigh = sensorObject("LT")
objLShank = sensorObject("LS")
objLoBack = sensorObject("LB")

kneelingDetect = kneelingDetection(NMKG, mass, height, alpha, torqueCutoff)

rFile = open('standaloneKneelingData2.txt')
data = rFile.readlines()
count = len(data)
rFile.close()


wFile = open('algDump.txt', 'w+')



for i in range(count):
    outputStr = ''
    y = data[i].split()
    objLThigh.gyX = float(y[0])
    objLThigh.gyY = float(y[1])
    objLThigh.gyZ = float(y[2])
    objLThigh.acX = float(y[3])
    objLThigh.acY = float(y[4])
    objLThigh.acZ = float(y[5])

    objRThigh.gyX = float(y[6])
    objRThigh.gyY = float(y[7])
    objRThigh.gyZ = float(y[8])
    objRThigh.acX = float(y[9])
    objRThigh.acY = float(y[10])
    objRThigh.acZ = float(y[11])

    objLShank.gyX = float(y[12])
    objLShank.gyY = float(y[13])
    objLShank.gyZ = float(y[14])
    objLShank.acX = float(y[15])
    objLShank.acY = float(y[16])
    objLShank.acZ = float(y[17])

    objRShank.gyX = float(y[18])
    objRShank.gyY = float(y[19])
    objRShank.gyZ = float(y[20])
    objRShank.acX = float(y[21])
    objRShank.acY = float(y[22])
    objRShank.acZ = float(y[23])
    
    objLoBack.gyX = float(y[24])
    objLoBack.gyY = float(y[25])
    objLoBack.gyZ = float(y[26])
    objLoBack.acX = float(y[27])
    objLoBack.acY = float(y[28])
    objLoBack.acZ = float(y[29])
    
    timestep = float(y[30])
        
    if i < 50:
        objRThigh.getCalib()
        objRShank.getCalib()

        objLThigh.getCalib()
        objLShank.getCalib()
        
        objLoBack.getCalib()

    else:

        objRThigh.angleCalc()
        objRShank.angleCalc()

        objLThigh.angleCalc()
        objLShank.angleCalc()
        
        objLoBack.angleCalc()



    kneelingTorqueEstimationR, kneelingTorqueEstimationL, kneeAngleR, kneeAngleL, legForward = kneelingDetect.getTorque(objRThigh, objRShank, objLThigh, objLShank, objLoBack)
    outputStr = f"{objLThigh.zAngle}\t{objRThigh.zAngle}\t{objLoBack.zAngle}\t{kneeAngleL}\t{kneeAngleR}\t{kneelingTorqueEstimationL}\t{kneelingTorqueEstimationR}\n"
    wFile.write(outputStr)
    print(outputStr)
    time.sleep(.02)
wFile.close()
