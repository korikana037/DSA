# Program tom find all the pair of integers whose sum is equal to target

def findPairs(arr, target):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] != arr[j] and arr[i]+arr[j] == target:
                return [i,j]


def findpairs(arr,target):
    t_dict = {}
    for i, num in enumerate(arr):
        compliment = target - num
        if compliment in t_dict:
            return [t_dict[compliment], i]
        t_dict[num] = i

arr = [2, 7, 11, 15]
target = 9

print(findPairs(arr, target))
print(findpairs(arr,target))