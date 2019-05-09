import math


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


class Feature:
    def __init__(self, name):
        self.name = name
        self.visited = -1
        self.infoGain = -1

# incomplete
class Node:
    def __init__(self, name, value):
        self.name = name
        self.right = None
        self.left = None

class ID3:
    def __init__(self, features):
        self.features = features
        self.data0 = dataset
        self.data1 = []
        self.tree_root = None

    def info_gain(self, column_name, current_items):
        #  total entropy
        total = len(current_items)
        need = 0
        noNeed = 0
        for item in current_items:
            if item.needLense == 0:
                noNeed += 1
            elif item.needLense == 1:
                need += 1
        total_entropy = ((-need / total) * math.log((need / total), 2)) + (
                (-noNeed / total) * math.log((noNeed / total), 2))

        if column_name == "age":
            lense_young = 0
            lense_old = 0
            no_lense_young = 0
            no_lense_old = 0
            for item in current_items:
                if item.needLense:
                    if item.age == 0:
                        lense_young += 1
                    else:
                        lense_old += 1
                else:
                    if item.age == 0:
                        no_lense_young += 1
                    else:
                        no_lense_old += 1

            total_young = lense_young + no_lense_young
            p_young_lense = lense_young / total_young
            p_young_no_lense = no_lense_young / total_young
            young_entropy = -p_young_lense * math.log(p_young_lense, 2) - p_young_no_lense * math.log(p_young_no_lense, 2)

            total_old = lense_old + no_lense_old
            p_old_lense = lense_old / total_old
            p_old_no_lense = no_lense_old / total_old
            old_entropy = -p_old_lense * math.log(p_old_lense, 2) - p_old_no_lense * math.log(p_old_no_lense, 2)

            return total_entropy - (total_young/total * young_entropy + total_old/total * old_entropy)

        if column_name == "prescription":
            lense_myope = 0
            lense_hyper = 0
            no_lense_myope = 0
            no_lense_hyper = 0
            for item in current_items:
                if item.needLense:
                    if item.prescription == 0:
                        lense_myope += 1
                    else:
                        lense_hyper += 1
                else:
                    if item.prescription == 0:
                        no_lense_myope += 1
                    else:
                        no_lense_hyper += 1

            total_myope = lense_myope + no_lense_myope
            p_myope_lense = lense_myope / total_myope
            p_myope_no_lense = no_lense_myope / total_myope
            myope_entropy = -p_myope_lense * math.log(p_myope_lense, 2) - p_myope_no_lense * math.log(p_myope_no_lense, 2)

            total_hyper = lense_hyper + no_lense_hyper
            p_hyper_lense = lense_hyper / total_hyper
            p_hyper_no_lense = no_lense_hyper / total_hyper
            hyper_entropy = -p_hyper_lense * math.log(p_hyper_lense, 2) - p_hyper_no_lense * math.log(p_myope_no_lense, 2)

            return total_entropy - (total_myope / total * myope_entropy + total_hyper / total * hyper_entropy)

        if column_name == "astigmatic":
            lense_not_ast = 0
            lense_ast = 0
            no_lense_not_ast = 0
            no_lense_ast = 0
            for item in current_items:
                if item.needLense:
                    if item.astigmatic == 0:
                        lense_not_ast += 1
                    else:
                        lense_ast += 1
                else:
                    if item.astigmatic == 0:
                        no_lense_not_ast += 1
                    else:
                        no_lense_ast += 1

            total_not_ast = lense_not_ast + no_lense_not_ast
            p_not_ast_lense = lense_not_ast / total_not_ast
            p_not_ast_no_lense = no_lense_not_ast / total_not_ast
            not_ast_entropy = -p_not_ast_lense * math.log(p_not_ast_lense, 2) - p_not_ast_no_lense * math.log(p_not_ast_no_lense, 2)

            total_ast = lense_ast + no_lense_ast
            p_ast_lense = lense_ast / total_ast
            p_ast_no_lense = no_lense_ast / total_ast
            ast_entropy = -p_ast_lense * math.log(p_ast_lense, 2) - p_ast_no_lense * math.log(p_ast_no_lense, 2)

            return total_entropy - (total_not_ast / total * not_ast_entropy + total_ast / total * ast_entropy)

        if column_name == "tearRate":
            lense_normal = 0
            lense_reduced = 0
            no_lense_normal = 0
            no_lense_reduced = 0
            for item in current_items:
                if item.needLense:
                    if item.tearRate == 0:
                        lense_normal += 1
                    else:
                        lense_reduced += 1
                else:
                    if item.prescription == 0:
                        no_lense_normal += 1
                    else:
                        no_lense_reduced += 1

            total_normal = lense_normal + no_lense_normal
            p_normal_lense = lense_normal / total_normal
            p_normal_no_lense = no_lense_normal / total_normal
            normal_entropy = -p_normal_lense * math.log(p_normal_lense, 2) - p_normal_no_lense * math.log(p_normal_no_lense, 2)

            total_reduced = lense_reduced + no_lense_reduced
            p_reduced_lense = lense_reduced / total_reduced
            p_reduced_no_lense = no_lense_reduced / total_reduced
            reduced_entropy = -p_reduced_lense * math.log(p_reduced_lense, 2) - p_reduced_no_lense * math.log(p_reduced_no_lense, 2)

            return total_entropy - (total_normal / total * normal_entropy + total_reduced / total * reduced_entropy)

    def split(self, column_name):
        if column_name == 'age':
            for item in self.data0:
                if item.age:
                    self.data0.remove(item)
                    self.data1.append(item)
            return

        if column_name == 'prescription':
            for item in self.data0:
                if item.prescription:
                    self.data0.remove(item)
                    self.data1.append(item)
            return

        if column_name == 'astigmatic':
            for item in self.data0:
                if item.astigmatic:
                    self.data0.remove(item)
                    self.data1.append(item)
            return

        if column_name == 'tearRate':
            for item in self.data0:
                if item.tearRate:
                    self.data0.remove(item)
                    self.data1.append(item)
            return

    # incomplete
    def build_decision_tree(self):
        max_gain = 0
        max_feature = Feature
        for feature in self.features:
            if feature.visited:
                continue
            if self.data0 is None:
                feature.infoGain = self.info_gain(feature.name, dataset)
            else:
                feature.infoGain = self.info_gain(feature.name, self.data0)
            if feature.infoGain > max_gain:
                max_gain = feature.infoGain
                max_feature = feature

        self.split(max_feature.name)
        max_feature.visited = 1;

    def classify(self, input):
        # takes an array for the features ex. [0, 0, 1, 1]
        # should return 0 or 1 based on the classification
        pass


dataset = getDataset()
features = [Feature('age'), Feature('prescription'), Feature('astigmatic'), Feature('tearRate')]
id3 = ID3(features)
cls = id3.classify([0, 0, 1, 1]) # should print 1
print('testcase 1: ', cls)
cls = id3.classify([1, 1, 0, 0]) # should print 0
print('testcase 2: ', cls)
cls = id3.classify([1, 1, 1, 0]) # should print 0
print('testcase 3: ', cls)
cls = id3.classify([1, 1, 0, 1]) # should print 1
print('testcase 4: ', cls)
