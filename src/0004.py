# <p>A palindromic number reads the same both ways. The largest palindrome made from the product of two $2$-digit numbers is $9009 = 91 \times 99$.</p>
# <p>Find the largest palindrome made from the product of two $3$-digit numbers.</p>
from time import time

def is_palindrome(n: int) -> bool:
    return str(n) == str(n)[::-1]

def get_largest_palindrome_from_product_of_n_digit_number(n: int) -> int:
    largest_palindrome = -1
    upper_bound = 10 ** n
    lower_bound = 10 ** (n - 1) * 9
    for i in range(upper_bound - 1, lower_bound, -1):
        for j in range(upper_bound - 1, lower_bound, -1):
            product = i * j
            if product < largest_palindrome:
                break
            if is_palindrome(product):
                largest_palindrome = product
    return largest_palindrome


if __name__ == "__main__":
    start = time()
    print(get_largest_palindrome_from_product_of_n_digit_number(3))
    end = time()
    print(f"Time: {end - start}s")
