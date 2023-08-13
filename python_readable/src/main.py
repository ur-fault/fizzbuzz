divs = {
    3: "Fizz",
    5: "Buzz",
    7: "Bazz",
    # you can add more divisors here
}

for n in range(100):
    s = ''
    for div, word in divs.items(): # using `dict.items()`` so we don't have to index the dict again
        if n % div == 0: # number `n` is divisible by `div`
            s += word
            
    if s == '': # if `s` is empty, then `n` is not divisible by any of the divisors
        s = str(n)
        
    print(s)