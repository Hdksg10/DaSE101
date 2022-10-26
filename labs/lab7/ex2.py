import numpy as np
import matplotlib.pyplot as plt

file = open("daily_KP_SUN_2020.csv", "r", encoding="utf8")
curMonth = 1
curDays = 0
sumSun = np.zeros(9)
averageSun = np.zeros(9)
for lines in file:
    datas = lines.split(",")
    if int(datas[1]) != curMonth:
        averageSun[curMonth - 1] = sumSun[curMonth - 1] / curDays
        curMonth += 1
        curDays = 0
        sumSun[curMonth - 1] = 0
    sumSun[curMonth - 1] += float(datas[3]) 
    curDays += 1
averageSun[curMonth - 1] = sumSun[curMonth - 1] / curDays        
    
x = np.arange(1, 10)
	
plt.subplot(121)
plt.xlabel("month")
plt.ylabel("hours")
plt.title("Total Sunshine Time")
plt.bar(x, sumSun)

plt.subplot(122)
plt.title("Average Sunshine Time")
plt.xlabel("month")
plt.ylabel("hours")
plt.bar(x, averageSun)

plt.show()