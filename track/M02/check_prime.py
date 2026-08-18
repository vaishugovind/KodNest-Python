# write a function to check whether the given number is prime or not.accept input and will return True if number is prime and false if the given number is nit a prime
def is_prime(number):
    for i in range(2,number):
        if number % i==0:
            return False
        else:
            return True
print(is_prime(100))
    