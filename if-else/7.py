try:
    nam=int(input("enter year"))
    if nam%400==0:
        print(f"{nam} la nam nhuan")
    else:
        print(f"{nam} ko phai nam nhuan")
except ValueError:
    print("invalid inp")