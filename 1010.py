# split() ei method er kaj hocche string data k list data te covert kore
# joto gula space thakbe toto gula alada alada item e vag korbe
line_1 = input().split(' ') [1:]
line_2 = input().split(' ') [1:]
total = int(line_1[0]) * float(line_1[1]) + int(line_2[0]) * float(line_2[1])
print("VALOR A PAGAR: R$ %0.2f"%total)