Diameter = int(input("Diameter?"))
R = Diameter / 2 
Inhoud = 4/3*3.1415926535*R**3
Formule = ("4/3*3.14159265359*" + str(R) + "**3" )

print ("Diameter " + str(Diameter))
print ("Straal = " + str(R))
print (Formule)
print ("Volume " + str(Inhoud))