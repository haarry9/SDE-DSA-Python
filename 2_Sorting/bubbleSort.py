def bubbleSort(a):
    n = len(a)
    # bubble sort reuires n-1 passes to sort an array of n elements
    # outer loop tracks the number of passes
    for i in range(1,n):
        # inner loop is to compare and swap
        for j in range(0,n-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
        

def optimizedBubbleSort(a):
    n = len(a)
    for i in range(1,n):
        #if the array is sorted, there will ne no swaps in the 1st pass
        flag = 0

        for j in range(0,n-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                flag = 1
        if flag == 0:
            break


if __name__ == "__main__":
    a = [8, 3, 7, 4, 1, 5, 2]
    b = [1, 2, 3, 4, 9, 10, 11]
    # bubbleSort(a)
    optimizedBubbleSort(b)
    for i in range(len(b)):
        print(b[i], end=" ")
