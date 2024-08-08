# <p>$2520$ is the smallest number that can be divided by each of the numbers from $1$ to $10$ without any remainder.</p>
# <p>What is the smallest positive number that is <strong class="tooltip">evenly divisible<span class="tooltiptext">divisible with no remainder</span></strong> by all of the numbers from $1$ to $20$?</p>
from time import time

def brute_force_smallest_positive_number_evenly_divisible_by_range(lower_bound: int, upper_bound: int) -> int:
    smallest_number = upper_bound
    while True:
        for i in range(lower_bound, upper_bound + 1):
            if smallest_number % i != 0:
                break
        else:
            return smallest_number
        smallest_number += upper_bound



def smallest_positive_number_evenly_divisible_by_range(lower_bound: int, upper_bound: int) -> int:
    # Initialize result with the first number in the range
    result = lower_bound
    gcd = lambda a, b: a if not b else gcd(b, a % b) # Eucliden algorithm
    lcm = lambda a, b: a * b // gcd(a, b)
    
    # Compute the LCM of all numbers in the range
    for num in range(lower_bound + 1, upper_bound + 1):
        result = lcm(result, num)
    return result

if __name__ == "__main__":
    start = time()
    print(brute_force_smallest_positive_number_evenly_divisible_by_range(1, 20))
    end = time()
    print(f"Brute force time: {end - start}s")

    start = time()
    print(smallest_positive_number_evenly_divisible_by_range(1, 20))
    end = time()
    print(f"Optimized time: {end - start}s")


