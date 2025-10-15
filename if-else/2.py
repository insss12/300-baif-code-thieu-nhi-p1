try:
    n=int(input("enter number"))
    if n%2==0:
        print("even number")
    else:
        print("odd number")
except ValueError:
    print("invalid input")