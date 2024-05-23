""" This calculator will find the vale of gravitational force between two objects"""

# M and m is the mass of two objects 
# R is the distance between the centre of two masses
# F is the gravitational force 
# G ( universal gravitational constant) = 6.67*10^-11
# N is the newton

M = float(input("Enter the mass of first object "))
m = float(input("Enter the mass of second object"))

R = float(input("Enter the distance between the center of two masses"))

G = 6.67*(10** -11)

F = (G*M*m) / (R**2)

print("the gravitational force between objects is:",round(F,2),"N" )

a =77
