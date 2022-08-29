"""Given an integer number n, return the difference between the product of its digits and the sum of its digits."""

def main(num: int) -> int:
    product = 1
    sum = 0
    
    while num > 0:
        digit = num % 10
        product *= digit
        sum += digit
        num = int(num / 10)

    return product - sum

from functools import reduce

def main_new(num: int) -> int:
    num_list = list(str(num))

    print(num_list)

    result = reduce(lambda result,next: [result[0] * int(next), result[1]+int(next)], num_list, [1, 0])

    print(result)

    # product = 1
    # sum = 0
    
    # while num > 0:
    #     digit = num % 10
    #     product *= digit
    #     sum += digit
    #     num = int(num / 10)

    # return product - sum


print(main_new(234))
