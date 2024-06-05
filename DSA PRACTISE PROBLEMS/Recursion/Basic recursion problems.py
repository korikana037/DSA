#sum of digits in a positive integer
def sumofdigits(n):
    if n == 0:
        return 0
    else:
        return n%10 + sumofdigits(n//10)

print('sum of the digits of the number is 539 is ', sumofdigits(593))


#power of a number using recursion
def powerofnumber(x,n):
    if n == 1:
        return x
    else:
        return x * powerofnumber(x, n - 1)
print('the value of 3 raised to 4 is ', powerofnumber(3,4))

#GCD of 2 numbers
def gcdoftwonum(a,b):
    if a%b == 0:
        return b
    else:
        return gcdoftwonum(b,a%b)

print('gcd of 48 and 18 is ', gcdoftwonum(48,18))

#converting a deciaml to binary
def dectobin(n):
    if n == 0:
        return 0
    else:
        return n%2 + 10*dectobin(n//2)

print('binary convertion of 10 is ', dectobin(10))