# Write a function to find all pairs of an integer array whose sum is equal to a given number.
# Do not consider commutative pairs.

def pair_sum(myList, sum):
    outputlist = []
    for i in range(len(myList)-1):
        for j in range(i+1, len(myList)):
            if myList[i]+myList[j]==sum:
                a=str(myList[i])
                b=str(myList[j])
                outputlist.append(f"{a}+{b}")
    return outputlist

arr = [2, 4, 3, 5, 6, -2, 4, 7, 8, 9]
target_sum = 7

print(pair_sum(arr, target_sum))