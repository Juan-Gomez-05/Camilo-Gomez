def perfecto(num):
    divi = [i for i in range(1,num) if num % i == 0]
    sum(divi) == num 
    num_perfec = [num for num in range(1, 1001) 
                    if perfecto(num)]
    return(f"Los numeros perfectos de 1 a 1000 son: {num_perfec}")