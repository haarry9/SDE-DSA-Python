
# Time Complexity: log10(n) + 1
def revNum(n):
    tmp = n
    rev =0
    while tmp >0:
        rev = rev * 10 + tmp%10
        tmp = tmp //10
    return rev

if __name__ == "__main__":
    n = int(input("Enter n: "))
    print(f"The reversed number is: {revNum(n)}")