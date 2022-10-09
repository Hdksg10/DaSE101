import re
pattern = "(13[0-3][0-9]|134[^9]|13[5-9][0-9]|147[0-9]|15[^4][0-9]|166[0-9]|17[2-3][0-9]|17[5-8][0-9]|18[0-9][0-9]|191[0-9]|193[0-9]|198[0-9]|199[0-9])[0-9]{7}$"
str = input()
reObject = re.match(pattern, str)
if  reObject != None:
    print("True")
else:
    print("False")