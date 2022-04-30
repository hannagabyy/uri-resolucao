valor = input().split(" ")
valor2 = input().split(" ")

cod,num,valor = valor
cod2,num2,valor2 = valor2


total = (int(num)*float(valor)) + (int(num2)*float(valor2))
print('VALOR A PAGAR = R$ %.2f'%total)
