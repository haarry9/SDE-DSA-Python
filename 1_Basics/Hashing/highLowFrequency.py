

def countFrequency(arr):
    mp = {}
    max_freq = float('-inf')
    min_freq = float('inf')
    for i in range(len(arr)):
        if arr[i] in mp:
            mp[arr[i]] += 1
        else:
            mp[arr[i]] = 1
    for x in mp:
        freq = mp[x]
        max_freq = max(freq, max_freq)
        min_freq = min(freq, min_freq)
        
    print("Element(s) with highest frequency:")
    for x in mp:
        if mp[x] == max_freq:
            print(x)

    print("Element(s) with lowest frequency:")
    for x in mp:
        if mp[x] == min_freq:
            print(x)


if __name__ == '__main__': 
    arr = [10,15,10,5,15,10]
    countFrequency(arr)