list=list(range(1, 101))
remover=int(input("enter to remove"))
if remover in list:
    list.pop(remover)

print(list)