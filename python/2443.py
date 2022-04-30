

a,b,c,d = map(int, input("insira aqq :").split())

print(a,b,c,d)

if 1<=a <=100 and 1<=b <=100 and 1<=c<=100 and 1<=d<=100:
    def soma (a,b,c,d):
        #se os denominadores forem iguais
     if b==d:
      numerador = a +b
      denominador =b
     else:
         numerador = a*d + c* d
         denominador = b*d

     def mdc(a,b):
         resto = a%b
         while resto!=0:
             a=b
             b=resto
             resto = a%b    
             return b     

     def mmc(a,b):
         return (a/mdc(a*b)) *b       


    soma(a, b, c, d)
    tmp= mdc(numerador, denominador)
     print() 