
def checkPalindrome(n):
    rev =0
    tmp =n
    flag = 0
    while tmp>0:
        rev = rev*10 + tmp%10
        tmp = tmp //10
    if rev == n:
        flag = 1
    return flag

if __name__ == "__main__":
    n = int(input("Enter n: "))
    if checkPalindrome(n):
        print("Number is a palindrome")
    else:
        print("Number is not a palindrome")