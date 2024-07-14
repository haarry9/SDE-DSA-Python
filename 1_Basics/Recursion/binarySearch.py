
def binarySearch(arr, key, l, h):
    # base case:
    if l > h:
        return -1
    else:
        mid = (l+h)//2
        if arr[mid] == key:
            return mid
        elif key >arr[mid]:
            return binarySearch(arr,key, mid+1, h)
        else:
            return binarySearch(arr, key, l, mid-1)


if __name__ == "__main__":
    arr = list(map(int, input("Enter the sorted array elements: ").split()))
    key = int(input("Enter the key to search: "))
    low, high = 0, len(arr)-1
    if(binarySearch(arr, key, low, high) == -1):
        print(f"{key} not found in array")
    else:
        print(f"{key} found at index {binarySearch(arr, key, low, high)}")
