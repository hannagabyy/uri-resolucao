
valor = input().split(" ")

A,B,C = valor
pi = 3.14159

area_tri_ret = (float(A)*float(C))/2
area_circ = float(pi) *(float(C)**2)
area_trap = ((float(A)+float(B))*float(C))/2
area_quad = float(B)*float(B)
area_ret= float(A)*float(B)

print('TRIANGULO : %.3f'%area_tri_ret)
print('CIRCULO : %.3f'%area_circ)
print('TRAPEZIO : %.3f'%area_trap)
print('QUADRADO : %.3f'%area_quad)
print('RETANGULO : %.3f'%area_ret)
