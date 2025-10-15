a=int(input("nhap a"))
b=int(input("nhap b"))
for i in range(1, min(a, b)+1):
    if a%i==0 and b%i==0:
        print(f"{a} va {b} deu chia het cho {i}")