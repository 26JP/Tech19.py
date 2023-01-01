#zad 1
 n = int(input())
 for i in range(1,32):
   print(i)

#zad 2
n = int(input())
for i in range(1,n):
    if i%2==1:
        print(i**2, end=" ")

#zad 3
for i in range(1000,10000):
    if i % 379 == 0:
        print(i)

#zad 4
n = int(input())
for i in range(100,1000):
  if i % 5 ==0 or i % 6 ==0 or i % 11 ==0:
    print(i)

#zad 5
suma = 0
n = int(input())
for i in range(0,n):
  x = int(input())
  suma+=x
print(suma)

#zad 6
k = int(input())
suma = 0
for i in range(0,k*2+1,2):
  suma = suma + i
print(suma)

#zad 7
k = int(input())
suma = 0
for i in range(11,k*2+11,2):
  suma = suma + i
print(suma)


#zad 8
W0 = int(input())
L = int(input())
WX = 0
suma = W0
for i in range(0, L * 12):
    WX = suma * 0.06 * (1/12)
    suma = suma + WX
print(round(suma))

#zad 9
from math import sqrt
a = int(input())
b = 21
suma = 0 
for i in range(0, a+1):
    for o in range(0, i, b):
        suma = suma + o
        o = o + 100
print(f"Suma to: {suma}")

#zad 10
from math import sqrt
for i in range(1,1001):
  if i%10 ==sqrt(i) or i%100 == sqrt(i) or i%1000 == sqrt(i):
    print(i)
