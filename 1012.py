# List is a collection which is ordered and changeable. Allows duplicate members.
#The map() function executes a specified function for each item in an iterable. The item is sent to the function as a parameter.
#map(function, iterables)

A,B,C = list(map(float,input().split()))
pi = 3.14159
area_rectangle_triangle = (1/2)*A*C
area_raidus_circle = pi*pow(C,2)
area_trapezium = (A+B)*C/2
area_square = pow(B,2)
area_rectangle =  A*B
print("TRIANGULO: %0.3f"%area_rectangle_triangle)
print("CIRCULO: %0.3f"%area_raidus_circle)
print("TRAPEZIO: %0.3f"%area_trapezium)
print("QUADRADO: %0.3f"%area_square)
print("RETANGULO: %0.3f"%area_rectangle)