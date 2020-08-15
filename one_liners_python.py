

#Swap numebrs
a =10
b =20
print("Before swapping, a =",a,"b =",b)
a,b = b,a
print("After swapping, a =",a,"b =",b)
 
 
#String paildrome 
str1 = input("Enter a string:") 
if str1 == str1[::-1]:
    print("Paildrome string")    
else :
    print("Not a Paildrome string")
    

#fibonacci series
fib = lambda x:x if x<=1 else fib(x-1) + fib(x-2)
# to print fibonacci sereis from 0 to 10:
for x in range (0,11):
    print(fib(x))
    
# Factorial 
fact = lambda n:[1,0][n>1] or fact(n-1) * n
# to print Factorail sereis from 0 to 10:
for x in range (0,11):
    print(fact(x))