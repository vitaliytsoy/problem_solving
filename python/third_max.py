from typing import List

def main(nums: List[int]):
    unique = sorted(set(nums))

    if len(unique) <= 2:
        return unique[-1]

    return unique[-3];


print(main([5,5,6,3,3,4,5,9,6,4,3,3]))