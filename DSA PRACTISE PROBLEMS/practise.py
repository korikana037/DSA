def splitarr(arr,k):
        new_arr = []
        for _ in range(k):
            new_arr.append(arr[0])
            arr.remove(arr[0])
        arr.extend(new_arr)
        return arr

arr = [12, 10, 5, 6, 52, 36]
print(splitarr(arr,3))

i= 0
arr = [10,5,6,52,36]
i = 1
arr = [10, 6, 52,36]