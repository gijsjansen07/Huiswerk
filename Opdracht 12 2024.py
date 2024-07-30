N = str(input("optel som "))
Seperate= [int(X) for X in str(N)]
som = int(0)
N = 0
formule = "0 = "
print ("lenght " + str(len(Seperate)))
while N < len(Seperate):
    som = Seperate[N] + som
    formule = str(Seperate[N]) + " + " + formule 
    N = N + 1
print (formule + str(som))
