def prime_checker(number):
    is_prime = True
    for num in range(2,number):
        if number % num == 0:
            is_prime = False
    if is_prime:
        print("it's prime")
    else:
        print("its not prime")
        

n = int(input("enter the number"))

prime_checker(number=n)n