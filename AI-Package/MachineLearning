import math
import numpy


class item:
    def __init__(self, age, prescription, astigmatic, tearRate, needLense):
        self.age = age
        self.prescription = prescription
        self.astigmatic = astigmatic
        self.tearRate = tearRate
        self.needLense = needLense


def getDataset():
    data = []
    labels = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0]
    data.append(item(0, 0, 0, 0,	labels[0]))
    data.append(item(0, 0, 0, 1,	labels[1]))
    data.append(item(0, 0, 1, 0,	labels[2]))
    data.append(item(0, 0, 1, 1,	labels[3]))
    data.append(item(0, 1, 0, 0,	labels[4]))
    data.append(item(0, 1, 0, 1,	labels[5]))
    data.append(item(0, 1, 1, 0,	labels[6]))
    data.append(item(0, 1, 1, 1,	labels[7]))
    data.append(item(1, 0, 0, 0,	labels[8]))
    data.append(item(1, 0, 0, 1,	labels[9]))
    data.append(item(1, 0, 1, 0,	labels[10]))
    data.append(item(1, 0, 1, 1,	labels[11]))
    data.append(item(1, 1, 0, 0,	labels[12]))
    data.append(item(1, 1, 0, 1,	labels[13]))
    data.append(item(1, 1, 1, 0,	labels[14]))
    data.append(item(1, 1, 1, 1,	labels[15]))
    data.append(item(1, 0, 0, 0,	labels[16]))
    data.append(item(1, 0, 0, 1,	labels[17]))
    data.append(item(1, 0, 1, 0,	labels[18]))
    data.append(item(1, 0, 1, 1,	labels[19]))
    data.append(item(1, 1, 0, 0,	labels[20]))
    return data


Total = 21
def Intropy(columnName):
    if columnName == "needLense":
        need = 0
        noNeed = 0
        for item in dataset:
            if item.needLense == 0:
                noNeed += 1
            elif item.needLense == 1:
                need += 1
        intropy = ((-need / Total) * math.log((need / Total), 2)) + ((-noNeed / Total) * math.log((noNeed / Total), 2))

    elif columnName == "age":
        young = 0
        adult = 0
        for item in dataset:
            if item.age == 0:
                young += 1
            elif item.needLense == 1:
                adult += 1
        intropy = ((-adult / Total) * math.log((adult / Total), 2)) + ((-young / Total) * math.log((young / Total), 2))

    elif columnName == "prescription":
        myope = 0
        hypermetrope = 0
        for item in dataset:
            if item.prescription == 0:
                hypermetrope += 1
            elif item.prescription == 1:
                myope += 1
        intropy = ((-myope / Total) * math.log((myope / Total), 2)) + ((-hypermetrope / Total) * math.log((hypermetrope / Total), 2))

    elif columnName == "astigmatic":
        no = 0
        yes = 0
        for item in dataset:
            if item.astigmatic == 0:
                yes += 1
            elif item.astigmatic == 1:
                no += 1
        intropy = ((-no / Total) * math.log((no / Total), 2)) + ((-yes / Total) * math.log((yes / Total), 2))

    elif columnName == "tearRate":
        normal = 0
        reduced = 0
        for item in dataset:
            if item.tearRate == 0:
                reduced += 1
            elif item.tearRate == 1:
                normal += 1
        intropy = ((-normal / Total) * math.log((normal / Total), 2)) + ((-reduced / Total) * math.log((reduced / Total), 2))

    return intropy

class Feature:
    def __init__(self, name):
        self.name = name
        self.visited = -1
        self.infoGain = -1




class ID3:
    def __init__(self, features):
        self.features = features


    def classify(self, input):
        totalIntropy = Intropy("")


        #takes an array for the features ex. [0, 0, 1, 1]
		#should return 0 or 1 based on the classification
		#pass


dataset = getDataset()
features = [Feature('age'),Feature('prescription'),Feature('astigmatic'),Feature('tearRate')]
id3 = ID3(features)
cls = id3.classify([0, 0, 1, 1]) # should print 1
print('testcase 1: ', cls)
cls = id3.classify([1, 1, 0, 0]) # should print 0
print('testcase 2: ', cls)
cls = id3.classify([1, 1, 1, 0]) # should print 0
print('testcase 3: ', cls)
cls = id3.classify([1, 1, 0, 1]) # should print 1
print('testcase 4: ', cls)





