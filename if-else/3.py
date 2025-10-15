a=int(input("enter number 1"))
b=int(input("enter number 2"))
c=int(input("enter number 3"))
if a>b>c:
    print(f"{a} is higher than {b} and {c}")
elif a>c>b:
    print(f"{a} is higher than {b} and {c}")
elif b>c>a:
    print(f"{b} is higher than {a} and {c}")
elif b>a>c:
    print(f"{b} is higher than {a} and {c}")
elif c>a>b:
    print(f"{c} is higher than {a} and {b}")
elif c>b>a:
    print(f"{c} is higher than {b} and {a}")
else:
    print("tie")