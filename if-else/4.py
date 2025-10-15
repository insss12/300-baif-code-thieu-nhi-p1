km=0
try:
    n=int(input("enter km"))
    if n>0:
        km=n*5
        print(f"for {n} km, the price is {km} $")
except ValueError:
    print("invalid input")
