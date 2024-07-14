# Brute-Fore approch: Time complexity: O(log_(10)N + 1)
import math
def countDigits(n):
    cnt = 0
    while n>0:
        n = n//10
        cnt += 1
    return cnt

#Optimal Solution: Time complexity: O(1)
def countDigits1(n):
    cnt = int(math.log10(n)) + 1
    return cnt


if __name__ == "__main__":
    n = int(input("Enter the number: "))
    print(f"The number of digits is: {countDigits1(n)}")