import numpy as np
from numpy import linalg
from numpy import genfromtxt
from numpy import array
from numpy import mat


def loadDataSet(fileName):
    #numFeat = len(open(fileName).readline().split('\t')) - 1
    numFeat = len(open(fileName).readline().split(',')) - 1
    print numFeat
    dataMat = []; labelMat = []
    fr = open(fileName)
    for line in fr.readlines():
        lineArr =[]
        curLine = line.strip().split(',')
        #curLine = line.strip().split('\t')
        print "curLine is: ", curLine 
        for i in range(numFeat):
            print "curLine[-1] is: ", curLine[-1]
            print "i is: ", i
            lineArr.append(float(curLine[i]))
            print "lineArr is: ", lineArr
        dataMat.append(lineArr)
        labelMat.append(float(curLine[-1]))
    return dataMat,labelMat
	
def loadDataSet2(fileName):
    numFeat = len(open(fileName).readline().split('\t')) - 1
    #numFeat = len(open(fileName).readline().split(',')) - 1
    print numFeat
    dataMat = []; labelMat = []
    fr = open(fileName)
    for line in fr.readlines():
        lineArr =[]
        #curLine = line.strip().split(',')
        curLine = line.strip().split('\t')
        print "curLine is: ", curLine 
        for i in range(numFeat):
            print "curLine[-1] is: ", curLine[-1]
            print "i is: ", i
            lineArr.append(float(curLine[i]))
            print "lineArr is: ", lineArr
        dataMat.append(lineArr)
        labelMat.append(float(curLine[-1]))
    return dataMat,labelMat

def loadDataSet3(fileName):
    #numFeat = len(open(fileName).readline().split('\t')) - 1
    numFeat = len(open(fileName).readline().split(',')) - 1
    print numFeat
    dataMat = []; labelMat = []
    fr = open(fileName)
    row = 0
    for line in fr.readlines():
        lineArr =[]
        curLine = line.strip().split(',')
        #curLine = line.strip().split('\t')
        print "curLine is: ", curLine 
        for i in range(numFeat):
            #print "curLine[-1] is: ", curLine[-1]
            print "i is: ", i
            lineArr.append(float(curLine[i]))
            #print "lineArr is: ", lineArr
        dataMat.append(lineArr)
        print "lineArr is: ", lineArr
        labelMat.append(float(curLine[-1]))
        print "curLine[-1] is:", curLine[-1]
        row = row + 1
        print "row is: ", row
    return dataMat,labelMat
	

def standRegres(xArr,yArr):
    xMat = mat(xArr); yMat = mat(yArr).T
    xTx = xMat.T*xMat
    if linalg.det(xTx) == 0.0:
        print "This matrix is singular, cannot do inverse"
        return
    ws = xTx.I * (xMat.T*yMat)
    return ws