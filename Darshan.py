""" This calculator will find the vale of gravity of a objects"""

# M is the mass of  object 
# R is the radius
# g is the gravity  
# G ( universal gravitational constant) = 6.67*10^-11
# m/s**2 is the unit 

M = float(input("Enter the mass of first object "))

R = float(input("Enter the distance between the center of two masses"))

G = 6.67*(10** -11)

g= (G*M) / (R**2)

print("the gravity of a objects is:",round(g,2),"m/s**2")

a=10
 
