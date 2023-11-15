"""
Display all the prime numbers between 1 to 250.
Store the results in a results.txt file.
"""

def is_prime_number(number):
    if number < 2:
        return False
    for divisor in range(2, int(number**0.5) + 1):
        if number % divisor == 0:
            return False
    return True

# Find and display prime numbers
primes = [num for num in range(1, 251) if is_prime_number(num)]

# Store results in a file
with open('results.txt', 'w') as result_file:
    result_file.write("Prime numbers between 1 and 250:\n")
    for prime in primes:
        result_file.write(str(prime) + '\n')

# Display the prime numbers
print("Prime numbers between 1 and 250:")
for prime in primes:
    print(prime)

