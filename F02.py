def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

if is_prime(17):
    print("O numero é primo")
else:
    print("O numero nao é primo")