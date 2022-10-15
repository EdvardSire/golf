def fizzbuzz(n):
    a = not bool(n % 5)
    b = not bool(n % 3)
    return ("Fizz"*b + "buzz"*a)*(a or b) + str(n)*(not(a+b))

for i in range(30):
    print(fizzbuzz(i))

