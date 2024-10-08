# <p>If we list all the natural numbers below $10$ that are multiples of $3$ or $5$, we get $3, 5, 6$ and $9$. The sum of these multiples is $23$.</p>
# <p>Find the sum of all the multiples of $3$ or $5$ below $1000$.</p>
from time import time

def get_sum_multiples_below_num(nums: tuple, upper_bound: int) -> int:
    multiple_sum = 0
    for i in range(upper_bound):
        if any(i % num == 0 for num in nums):
            multiple_sum += i
    return multiple_sum

if __name__ == "__main__":
    start = time()
    print(get_sum_multiples_below_num((3, 5), 1000))
    end = time()
    print(f"Time elapsed: {end - start}s")
