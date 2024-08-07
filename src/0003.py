# <p>The prime factors of $13195$ are $5, 7, 13$ and $29$.</p>
# <p>What is the largest prime factor of the number $600851475143$?</p>

def trial_division(n: int) -> list:
    # https://en.wikipedia.org/wiki/Trial_division
    a = []
    f = 2 # Start at smallest prime number
    while f * f <= n: # While less than sqrt of n
        if n % f == 0: # If n is divisible by f
            a.append(f)
            n //= f # Divide n by f to find next factor
        else:
            f += 1 # If not divisible, increment f
    if n != 1:
        a.append(n)
    return a



if __name__ == "__main__":
    print(max(trial_division(600851475143)))
