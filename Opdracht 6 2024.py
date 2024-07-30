N = int(input("N = ?"))
N = float(N / 2)
Rounded_N = int(round(N))
if N == Rounded_N :
    print ("Is even")
else:  
    print ("Is oneven")
#eigen oplossing zonder op te zoeken

num = (float(input()))
if num % 2:
    print ("odd")
else:
    print ("even")
#stack overflow oplossing
# The % sign is like division only it checks for the remainder, 
#so if the number divided by 2 has a remainder of 0 it's even otherwise odd.
#Or reverse them for a little speed improvement, (heb ik gedaan)
#since any number above 0 is also considered "True" you can skip needing to do any equality check: