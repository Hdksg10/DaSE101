import time

pid = input("Your student id:")
name = input("Your name:")
grades = input("Your grades, splited by \",\":")
stuGrade = grades.split(",")
averageGrade = (float(stuGrade[0]) + float(stuGrade[1]) + float(stuGrade[2])) / 3
strAverageGrade = str(averageGrade)

fp = open("my.txt", "w")
fp.write(pid + " " + name + "\n")
fp.write(strAverageGrade + "\n")
fp.write(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + "\n")
time.sleep(2)
fp.write(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
fp.close()