def giai_thua(n):
    S=1
    for i in range(1, n+1):
        S*=i
    print(f"giai thua cua {n} la {S}")

giai_thua(4)