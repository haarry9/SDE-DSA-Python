def selctionSort(a):
    n = len(a)
    for i in range(n-1): # i goes till second last element
        sml_idx = i # let curent element be the smallest 
        for j in range(i+1, n):
            if a[j] < a[sml_idx]:
                sml_idx = j
        # swap smallest element with current element
        a[i], a[sml_idx] = a[sml_idx], a[i]


if __name__ == "__main__":
    a = [8, 3, 7, 4, 3, 5, 2]
    selctionSort(a)
    for i in range(len(a)):
        print(a[i], end=" ")
