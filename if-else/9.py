def isprime(n):
    if n<2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            return False
        else:
            return True
result=[]
for i in range(1,101):
    if isprime(i):
        result.append(i)

print(result)


