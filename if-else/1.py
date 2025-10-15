try:
    n=int(input("enter number"))
    if n>0:
        print("this number is positive")
    else:
        print("this number is negative")
except ValueError:
    print("invalid input")
