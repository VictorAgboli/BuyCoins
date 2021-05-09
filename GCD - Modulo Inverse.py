

"""
In modular arithmetic, the modular multiplicative inverse of an integer "a" modulo n is an integer such that;
                ax ≡ 1(mod n), or in other words, ax = kn + 1 , where k is an integer.

Such an inverse only exist when a and n are co-primes, or relatively primes, ie. there's no common factors between a and n, except 1. 

        ∴ gcd(a, n) = 1

Therefore, ax = kn + 1 => ax + (-k)n = 1. Replacing b = -k,

We have:
                ax + bn = 1.

Hence, x is the modulo multiplicative inverse of a.
"""


"""
Euclidean Algorithm is a technique used to find the GCD of two integers. 
"""
def gcd(a,b):
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        return gcd(b, a%b)




"""
The Extended Euclidean Algorithm can also be used to compute the GCD of two integers

            ax + by = gcd(a,b), where a and b are integers.

It can also be used to find the modulo multiplicative inverse of an integer.

The equation above is a Diophatine linear equation, with solution (x and y), where x is the multiplicative inverse. 

Since GCD(a,b) = 1, the equation is a Non-homogenous Diophatine Linear Equation
"""
def signcheck(u,v):
    if u >= 0:
        return u
    else:
        return signcheck(u+v, v) #ensures the answer is a positive equivalent.  
        
    
def diophantine(a,b,c):
    for y in range(pow(1000,10000) + 1):
        x = (c - b*y)/ a
        if int(x) == x:
            return int(x), y #the solutions to the diophantine equation
    

def modulo_inverse(a,b):
    if gcd(a,b) != 1:
        return "\nThere is no Modulo Multiplicative Inverse for {a1} (mod {m1})".format(a1 = a, m1 = b)
    else:
        inv, v = diophantine(a,b, gcd(a,b))
        return "\nModulo Multiplicative Inverse of {a1} (mod {m1}), is {ans}".format(a1 = a, m1 = b, ans = signcheck(inv, b))

print("This program gives the Modulo multiplcative inverse of a(mod N)\n")   
a = int(input("Integer a:"))
b = int(input("Modulo N:"))

print(modulo_inverse(a,b))
