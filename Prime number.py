def is_prime(n):
    i = 2
    while i < n:
        if n%i == 0:
            return False
        i += 1
    return True

p = 2
while p <= 100:
    if is_prime(p):
        print (p,"is prime number"),
    p=p+1

print ("Done")