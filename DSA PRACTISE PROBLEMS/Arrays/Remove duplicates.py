# Write a function to remove the duplicate numbers on given integer array/list.
def remove_duplicates(lst):
    unique_lst = []
    seen = set()
    for item in lst:
        if item not in seen:
            unique_lst.append(item)
            seen.add(item)
    return unique_lst

my_list = [1, 1, 2, 2, 3, 4, 5]
print(remove_duplicates(my_list))