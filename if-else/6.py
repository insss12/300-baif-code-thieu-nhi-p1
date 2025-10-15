try:
    input=int(input("enter number"))
    for i in range(1, 11):
        print(f"{input} * {i} = {input*i}")
except ValueError:
    print("invalid input")