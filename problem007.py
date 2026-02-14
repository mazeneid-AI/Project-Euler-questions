#10 001st Prime
#Problem 7

#By listing the first six prime numbers 2,3,5,7,11 and 13
#: , and 13 , we can see that the th6 prime is 13 .
#What is the 10001st prime number?
limit = 150000
""" we know the limit from the equation
nth prime≈nlogn
nth prime≈n(logn+loglogn)
 the prime 10001 is 104743 """


primes = []
"""create array for primes"""

for num in range(2, limit + 1):
    is_prime = True
    
    for i in range(2, int(num**0.5) + 1):
        """ this loop for primes"""
        if num % i == 0:
            """ if num%i==0 this is not prime """
            is_prime = False
            break
    
    if is_prime:
        primes.append(num)

print(primes[10000])
