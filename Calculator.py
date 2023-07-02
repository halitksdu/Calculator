from modul_cal import *
print(""""************************
Calculator
Process;
1. Addition
2. Extraction
3. Multiplication
4. Division
5. Percentage
6. Exponentian
7. Rooting
8. Logarithm
9. Ln
10.Factorial
11.Sinus
12.Cosinus
13.Tangent
14.Cotangent

Press Q to exit.
************************
""")

while True:
    process = input("Enter the process number: ")

    if process == "1" or process == "2" or process == "3" or process == "4" or process == "5":
        a = int(input("Enter the first number : "))
        b = int(input("Enter the second number: "))
    elif process == "6":
        a = int(input("Enter the number: "))
        b = int(input("Enter the power : "))
    elif process == "7":
        a = int(input("Enter the number     : "))
        b = int(input("Enter the degree root: "))
    elif process == "8":
        a = int(input("Enter the number: "))
        b = int(input("Enter the  base : "))
    elif process == "9" or process == "10":
        a = int(input("Enter the number : "))
    elif process == "11" or process == "12" or process == "13" or process == "14":
        a = float(input("Enter the number: "))
        z = input("Degree or radian(d/r) : ")
        d = a
        if z == "d":
            a = conv(a)
    elif process == "q" or process == "Q":
        break
    else:
        print("Wrong process number!")

    if process == "1":
        print("{} + {} = {}".format(a,b,a+b))
    elif process == "2":
        print("{} - {} = {}".format(a,b,a-b))
    elif process == "3":
        print("{} x {} = {}".format(a,b,a*b))
    elif process == "4":
        print("{} : {} = {}".format(a,b,a/b))
    elif process == "5":
        print("{} / {} = {}%".format(a,b,100*a/b))
    elif process == "6":
        print("{} ^ {} = {}".format(a,b,a**b))
    elif process == "7":
        print("{} ^ (1/{}) = {}".format(a,b,a**(1/b)))
    elif process == "8":
        print("log({}) in base {} : {}".format(a,b,log(a,b)))
    elif process == "9":
        print("ln({}) = {}".format(a,ln(a)))
    elif process == "10":
        print("{}! = {}".format(a,fact(a)))
    elif process == "11":
        print("Sin({}) = {}".format(d,sin(a)))
    elif process == "12":
        print("Cos({}) = {}".format(d,cos(a)))
    elif process == "13":
        print("Tan({}) = {}".format(d,tan(a)))
    elif process == "14":
        print("Cot({}) = {}".format(d,cot(a)))
