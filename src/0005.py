# <p>$2520$ is the smallest number that can be divided by each of the numbers from $1$ to $10$ without any remainder.</p>
# <p>What is the smallest positive number that is <strong class="tooltip">evenly divisible<span class="tooltiptext">divisible with no remainder</span></strong> by all of the numbers from $1$ to $20$?</p>
from time import time

def smallest_positive_number_evenly_divisible_by_range(lower_bound: int, upper_bound: int) -> int:
    smallest_number = upper_bound
    while True:
        for i in range(lower_bound, upper_bound + 1):
            if smallest_number % i != 0:
                break
        else:
            return smallest_number
        smallest_number += upper_bound



if __name__ == "__main__":
    start = time()
    print(smallest_positive_number_evenly_divisible_by_range(1, 20))
    end = time()
    print(f"Time: {end - start}s")
