import re


import re

def main(s: str):
    filtered = re.sub(r"[\W_]+", '', s).lower()
    i = 0
    j = len(filtered) - 1
    result = True

    while (i <= j):
        if (filtered[i] != filtered[j]):
            result = False
            break

        i += 1
        j -= 1
        

    return result


print(main("A man, a plan, a canal: Panama"))
