
def printAverageGrad():
    stuGrade = open("stuGrade.csv", "r")
    stuGrade.readline()
    for lines in stuGrade:
        lines = lines.strip()
        elements = lines.split(",")
        averageGrade = (float(elements[1]) + float(elements[2]) + float(elements[3])) / 3
        print(f"{elements[0]} : {averageGrade:.2f}")
    stuGrade.close()

printAverageGrad()