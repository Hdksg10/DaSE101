import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pymysql
import csv

db = pymysql.connect(host = "cdb-r2g8flnu.bj.tencentcdb.com", port = 10209, user
= "dase2020", password = "dase2020", database = "dase_intro_2020")
cursor = db.cursor()


sql = "select * from INFORMATION_SCHEMA.COLUMNS where TABLE_NAME='SH_Grade'"
cursor.execute(sql)
results = cursor.fetchall()
col_names = []
for line in results:
    col_names.append(line[3])
# print(col_names)
col_names.insert(2, 'Class')

sql = "SELECT * FROM SH_Grade"
cursor.execute(sql)
results = cursor.fetchall()
resultsWithClass = []
for line in results:
    lineList = list(line)
    lineList.insert(2, line[1][0])
    resultsWithClass.append(lineList)

with open("SH_Grade.csv", "w") as fp:
    writer = csv.writer(fp)
    writer.writerow(col_names)
    writer.writerows(resultsWithClass)

stuData = pd.read_csv("SH_Grade.csv")


sizeB = stuData.index.size
stuData = stuData.drop_duplicates(subset=['StuId',])
sizeA = stuData.index.size
print(f"处理前行数：{sizeB}, 处理后行数：{sizeA}")
stuData = stuData.dropna(thresh = 47)
sizeB = stuData.index.size
print(f"处理前行数：{sizeA}, 处理后行数：{sizeB}")
# print(stuData.iat[127, 3])
# print(stuData.iat[128, 3])
stuData['Sex'] = stuData["Sex"].fillna(method="ffill")
# print(stuData["CHI921"].max())
# print(stuData.iat[128, 3])
for i in range(4, 59):
    stuData[col_names[i]] = stuData[col_names[i]].fillna(stuData[col_names[i]].median())

for i in range(4, 59):
    if col_names[i][-3::1] == '822' and col_names[i][0] != "P":
        stuData[col_names[i]] = stuData[col_names[i]].mul(100/120)
    elif stuData[col_names[i]].max() > 100:
        stuData[col_names[i]] = stuData[col_names[i]].mul(100/150)
    elif stuData[col_names[i]].max() <= 60:
        stuData[col_names[i]] = stuData[col_names[i]].mul(100/60)
    elif stuData[col_names[i]].max() <= 90:
        stuData[col_names[i]] = stuData[col_names[i]].mul(100/90)

# for i in range(4, 59):
#     print(f"{col_names[i]}:{stuData[col_names[i]].max()}")

sexNum = stuData.groupby(["Class", "Sex"])["id"].count()
plt.bar(["A", "B", "C", "D", "E", "F", "G"], sexNum[::2], label = "Female")
plt.bar(["A", "B", "C", "D", "E", "F", "G"], sexNum[1::2], bottom = sexNum[::2], label = "Male")
plt.legend()
plt.show()

chiScores = stuData.filter(regex="^CHI[0-9]*").loc[(stuData["StuId"] == "A13") | (stuData["StuId"] == "A15")]

plt.plot(chiScores.columns, chiScores.iloc[0], label = "A13")
plt.plot(chiScores.columns, chiScores.iloc[1], label = "A15")
plt.xticks(chiScores.columns[::2])
plt.legend()
plt.show()

stuFailedInCHI721OrENG721 = stuData.query("CHI721 < 60 or ENG721 < 60").filter(regex = "^(Class|StuId|((CHI|ENG)721))").set_index("StuId")
print(stuFailedInCHI721OrENG721)

mean = stuData.groupby("Class").mean(numeric_only = True).filter(regex="622$").loc[["A", "C"]]
print(mean)
var = stuData.groupby("Class").var(numeric_only = True).filter(regex="622$").loc[["A", "C"]]
print(var)
stuData.to_csv("task8.csv")
