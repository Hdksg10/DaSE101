from cProfile import label
import numpy as np
import matplotlib.pyplot as plt

colors = {"setosa" : "blue", "versicolor" : "orangered", "virginica" : "g"}
labels = {"setosa" : "setosa", "versicolor" : "versicolor", "virginica" : "virginica"}
file = open("iris.csv", "r", encoding="utf8")
Sepal_Length = np.zeros(150)
Sepal_Width = np.zeros(150)
Petal_Length = np.zeros(150)
Petal_Width = np.zeros(150)
file.readline()
curLine = 0
for lines in file:
    datas = lines.split(",")
    Sepal_Length[curLine] = float(datas[0])
    Sepal_Width[curLine] = float(datas[1])
    Petal_Length[curLine] = float(datas[2])
    Petal_Width[curLine] = float(datas[3])
    curLine += 1

plt.subplot(321)
plt.xlabel("Sepal_Length")
plt.ylabel("Sepal_Width")
plt.scatter(Sepal_Length[0:50], Sepal_Width[0:50], s=5, label = labels["setosa"], c = colors["setosa"])
plt.scatter(Sepal_Length[50:100], Sepal_Width[50:100], s=5, label = labels["versicolor"], c = colors["versicolor"])
plt.scatter(Sepal_Length[100:150], Sepal_Width[100:150], s=5, label = labels["virginica"], c = colors["virginica"])
plt.legend()

plt.subplot(322)
plt.xlabel("Sepal_Length")
plt.ylabel("Petal_Length")
plt.scatter(Sepal_Length[0:50], Petal_Length[0:50], s=5, label = labels["setosa"], c = colors["setosa"])
plt.scatter(Sepal_Length[50:100], Petal_Length[50:100], s=5, label = labels["versicolor"], c = colors["versicolor"])
plt.scatter(Sepal_Length[100:150], Petal_Length[100:150], s=5, label = labels["virginica"], c = colors["virginica"])
plt.legend()

plt.subplot(323)
plt.xlabel("Sepal_Length")
plt.ylabel("Petal_Width")
plt.scatter(Sepal_Length[0:50], Petal_Width[0:50], s=5, label = labels["setosa"], c = colors["setosa"])
plt.scatter(Sepal_Length[50:100], Petal_Width[50:100], s=5, label = labels["versicolor"], c = colors["versicolor"])
plt.scatter(Sepal_Length[100:150], Petal_Width[100:150], s=5, label = labels["virginica"], c = colors["virginica"])
plt.legend()

plt.subplot(324)
plt.xlabel("Sepal_Width")
plt.ylabel("Petal_Length")
plt.scatter(Sepal_Width[0:50], Petal_Length[0:50], s=5, label = labels["setosa"], c = colors["setosa"])
plt.scatter(Sepal_Width[50:100], Petal_Length[50:100], s=5, label = labels["versicolor"], c = colors["versicolor"])
plt.scatter(Sepal_Width[100:150], Petal_Length[100:150], s=5, label = labels["virginica"], c = colors["virginica"])
plt.legend()

plt.subplot(325)
plt.xlabel("Sepal_Width")
plt.ylabel("Petal_Width")
plt.scatter(Sepal_Width[0:50], Petal_Width[0:50], s=5, label = labels["setosa"], c = colors["setosa"])
plt.scatter(Sepal_Width[50:100], Petal_Width[50:100], s=5, label = labels["versicolor"], c = colors["versicolor"])
plt.scatter(Sepal_Width[100:150], Petal_Width[100:150], s=5, label = labels["virginica"], c = colors["virginica"])
plt.legend()

plt.subplot(326)
plt.xlabel("Petal_Length")
plt.ylabel("Petal_Width")
plt.scatter(Petal_Length[0:50], Petal_Width[0:50], s=5, label = labels["setosa"], c = colors["setosa"])
plt.scatter(Petal_Length[50:100], Petal_Width[50:100], s=5, label = labels["versicolor"], c = colors["versicolor"])
plt.scatter(Petal_Length[100:150], Petal_Width[100:150], s=5, label = labels["virginica"], c = colors["virginica"])
plt.legend()


plt.show()