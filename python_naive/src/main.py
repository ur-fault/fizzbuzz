for n in range(100):
    if n % 3 == 0 and n % 5 == 0:
        print("FizzBuzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n)
        
    # It's naive because it's not scalable.
    # If we want to add more conditions, we have to add more if-else statements.
