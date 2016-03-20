def bi_root(x):
    epsilon = .001
    high = x
    low = 0
    guess = (high + low)/2
    while abs(guess**2 - x) > epsilon:
        guess = (high + low)/2
        if abs(guess**2) > x:
            high = guess
        elif abs(guess**2) < x:
            low = guess
    if guess**2 == x or (abs(guess**2 - x) <= epsilon):
        return abs(guess)

print bi_root(144)