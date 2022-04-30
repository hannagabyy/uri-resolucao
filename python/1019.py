n=int(input())
horas=0
minutos=0
resto=0
if n>=3600 :
    horas=n/3600
    resto = n-horas
if n>=60 or resto>=60:
        minutos = horas/60
        resto = n-minutos
        segundos=resto
else:
    segundos=n        

print('%d h' %horas)
print('%d m' %minutos)
print('%d s' %segundos)

