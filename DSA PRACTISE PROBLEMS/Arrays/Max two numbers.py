# Given a list, write a function to get first, second best scores from the list.
# List may contain duplicates.

def first_second(my_list):
    first = 0
    second = 0
    for i in range(len(my_list)):
        if my_list[i] >= first:
            second = first
            first = my_list[i]
        elif my_list[i] > second:
            second = my_list[i]
    return first, second


my_list = [84, 85, 86, 87, 85, 90, 85, 83, 23, 45, 84, 1, 2, 0]
print(first_second(my_list))