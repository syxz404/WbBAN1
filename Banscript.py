#Hi for everyone, i am wb.py
import os
import time

print("Olá, bem vindo ao script de dar ban em números :)")
num=int(input("Digite o número que você deseja dar ban: "))
print('\n')
resp=int(input(f"O número digitado foi {num}, está correto?[1=Y/2=N] "))
if resp==1:
    os.system("cmatrix")
else:
    os.system("clear")
