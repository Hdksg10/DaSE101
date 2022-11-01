import pymysql
import numpy as np

def excuteAndReturnTuple(cursor, sql):
    cursor.execute(sql)
    result = cursor.fetchall()
    return result


def excuteAndPrintAll(cursor, sql):
    cursor.execute(sql)
    result = cursor.fetchall()
    for lines in result:
        print(lines)

def excuteAndReturnNumber(cursor, sql):
    cursor.execute(sql)
    result = cursor.fetchall()
    return result[0][0]

def excuteAndReturnArray(cursor, sql):
    cursor.execute(sql)
    result = cursor.fetchall()
    sz = len(result)
    res = np.zeros(sz)
    for index in range(0, sz):
        res[index] = result[index][0]
    return res



db = pymysql.connect(host = "cdb-r2g8flnu.bj.tencentcdb.com", port = 10209, user
= "dase2020", password = "dase2020", database = "dase_intro_2020")
cursor = db.cursor()

sql1 = """SELECT * FROM bicycle_train LIMIT 17,5"""
print(excuteAndReturnTuple(cursor, sql1))

sql2_1 = "SELECT MAX(wind) FROM bicycle_train "
sql2_2 = "SELECT MIN(wind) FROM bicycle_train "
print(f"{excuteAndReturnNumber(cursor, sql2_1)}, {excuteAndReturnNumber(cursor, sql2_2)}")

sql3 = "SELECT AVG(temp_air) FROM bicycle_train WHERE hour=10 AND city=0 AND wind<2 AND y>=100 AND weather=1"
avg = excuteAndReturnNumber(cursor, sql3)
print(avg)

sql4 = "SELECT temp_air FROM bicycle_train WHERE hour=10 AND city=0 AND wind<2 AND y>=100 AND weather=1"
print(np.var(excuteAndReturnArray(cursor, sql4)))

sql5 = "SELECT city, SUM(y) FROM bicycle_train WHERE is_workday=1 AND weather=3 GROUP BY city ORDER BY SUM(y) DESC"
excuteAndPrintAll(cursor, sql5)

sql6 = "SELECT hour, AVG(y) FROM bicycle_train WHERE city=1 AND temp_body<=10 and is_workday=1 GROUP BY hour HAVING hour>=17 AND hour<=19 ORDER BY AVG(y)"
excuteAndPrintAll(cursor, sql6)