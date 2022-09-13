#判断BMI指数


print("请输入您的身高（单位：米）")
height = float(input("身高："))
print("请输入您的体重（单位：千克）")
weight = float(input("体重："))
bmi = weight / (height * height)

print(f"你的BMI是{bmi}")
if bmi < 18.5 :
    print("您的体重过轻")
elif bmi < 24:
    print("您的体重正常")
elif bmi < 28:
    print("您的体重过重")
else:
    print("您的bmi属于肥胖")