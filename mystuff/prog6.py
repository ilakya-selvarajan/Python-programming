#a program that solves the roots of a quadratic equation
from math import sqrt
a=input ("Give a: ")
b=input ("Give b: ")
c= input ("Give c: ")
x1=(-b+sqrt(b*b-4*a*c))/(2*a)
x2=(-b-sqrt(b*b-4*a*c))/(2*a)
print "The roots are ", x1 ,"and" ,x2
