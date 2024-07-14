

def countFrequency(arr):
    mp = {}
    for i in range(len(arr)):
        if arr[i] in mp:
            mp[arr[i]] += 1
        else:
            mp[arr[i]] = 1
    for x in mp:
        print(x, mp[x])



if __name__ == '__main__': 
    arr = [10,15,10,5,15,10]
    countFrequency(arr)