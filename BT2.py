import math
a = float(input(" nhập hệ số a: "))
b = float(input("nhập hệ số b: "))
if a == 0:
    if b == 0:
        print("vô số nghiệm")
    else:
        print("vô nghiệm")
else:
    print("phương trình có 1 nghiệm x=-a/b: x= ",(-a)/b)