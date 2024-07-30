
from random import seed
from random import randint

seed()

A = randint(0,100)
B = randint(0,100)
C= 0
D= 0
if A==B:
    C=-A-B
    print (C)
else:
    C= randint(0,100)
if A==C:
    B = -A-C
elif B==C:
    A=-B-C
D= A+B+C
#een willekeurig integer tussen de 0 en de 100
print (A)
print(B)
print(C)
print(D)
