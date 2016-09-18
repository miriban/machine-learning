from sklearn import tree
fruits = {0:"apple",1:"orange"}
# 0 for bumpy and 1 for smooth
features = [[140,1],[130,1],[150,0],[170, 0]] # inputs of classifier
# 0 for apple and 1 for orange
labels = [0,0,1,1] # output that we want
# our classifier is called Decision Tree
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features,labels) # find patterns in data
print "It could be => ",fruits[clf.predict([[150,0]])[0]]
