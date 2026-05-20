# assign. A letter grade based on a student's scpre:a(90-100),B(80-90),C(70-79),
# d(60-7=),f below 60
score=int(input("enter your score"))
if score>=101:
    print("input valid score")
    exit()
if score>=90:
    print("a")
elif score>=80:
    print("b")
elif score>=70:
    print("c")
elif score>=60:
    print("d")
else:
    print("f")                