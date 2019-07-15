# -- coding: utf-8 --

from sklearn.feature_extraction import DictVectorizer
import csv
from sklearn import tree
from sklearn import preprocessing
from sklearn.externals.six import StringIO

# Read in the csv file and put features into list of dict and list of class label
allElectronicsData = open('AllElectronics.csv', 'rt')
reader = csv.reader(allElectronicsData)
##For version 3.2 and above  Change: csv_file_object.next()  To: next(csv_file_object)
#取得第一行当做头信息
headers = next(reader)
print("---this is header---"+str(headers))

featureList = []
labelList = []
#将数据一一对应存到相应的位置上
for row in reader:
    labelList.append(row[len(row)-1])
    rowDict = {}
    for i in range(1, len(row)-1):
        rowDict[headers[i]] = row[i]
    featureList.append(rowDict)
print("featureList:"+str(featureList))

# Vetorize features
# 将上面的字典数据转换成矩阵样子的数据
vec = DictVectorizer()
dummyX = vec.fit_transform(featureList) .toarray()

print("--------dummyX-------")
print(str(dummyX))
print(vec.get_feature_names())

print("labelList: " + str(labelList))

# vectorize class labels
lb = preprocessing.LabelBinarizer()
dummyY = lb.fit_transform(labelList)
print("dummyY: " + str(dummyY))

# Using decision tree for classification
# clf = tree.DecisionTreeClassifier()
clf = tree.DecisionTreeClassifier(criterion='entropy')
clf = clf.fit(dummyX, dummyY)
print("clf: " + str(clf))


# Visualize model
with open("allElectronicInformationGainOri.dot", 'w') as f:
    f = tree.export_graphviz(clf, feature_names=vec.get_feature_names(), out_file=f)

oneRowX = dummyX[0, :]
print("oneRowX: " + str(oneRowX))

newRowX = oneRowX
newRowX[0] = 1
newRowX[2] = 0
print("newRowX: " + str(newRowX))

# predictedY = clf.predict(newRowX)
# print("predictedY: " + str(predictedY))
#

