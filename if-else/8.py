list=[1,6,7,4,2,5]
so_chan=0
so_le=0
for num in list:
    if num%2==0:
        so_chan+=1
    elif num%2!=0:
        so_le+=1

print(f"trong day so tren co tat ca {so_chan} so chan va {so_le} so le")

