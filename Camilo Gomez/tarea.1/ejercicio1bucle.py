numero=int(input("ingrese un numero:"))

def divisores(numero):
 for x in range(1,numero+1):
    if numero%x==0:
        print(x)
        
print(divisores(numero))
