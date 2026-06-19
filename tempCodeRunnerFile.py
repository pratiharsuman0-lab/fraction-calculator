def factorial_num(num):
    sol=num*factorial_num(num-1)
    return sol

print(factorial_num(5))