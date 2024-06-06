# Define a function to count the frequency of words in a given list of words.

def count_word_frequency(words):
    count_dict = {}
    for word in words:
        if word in count_dict:
            count_dict[word] += 1
        else:
            count_dict[word] = 1
    return count_dict


# Define a function with takes two dictionaries as parameters and merge them and
# sum the values of common keys.

def merge_dicts(dict1, dict2):
    for key in dict1:
        if key in dict2:
            dict2[key] += dict1[key]
        else:
            dict2[key] = dict1[key]
    return dict2


#Define a function which takes a dictionary as a parameter and returns the key
# with the highest value in a dictionary.

def max_value_key(my_dict):
    maxi = 0
    for key in my_dict:
        if my_dict[key] > maxi:
            maxi = my_dict[key]
    for key, value in my_dict.items():
        if value == maxi:
            return key


def max_value_key1(my_dict):
    return max(my_dict, key=my_dict.get)


#Define a function which takes as a parameter dictionary and returns a dictionary
# in which reverse the key-value pairs are reversed.

def reverse_dict(my_dict):
    reversed_dict = {}
    for key, value in my_dict.items():
        reversed_dict[value] = key
    return reversed_dict


def reverse_dict1(my_dict):
    return {v: k for k, v in my_dict.items()}


#Define a function that takes a dictionary as a parameter and returns a dictionary
# with elements based on a condition.

def filter_dict(my_dict, condition):
    return {k: v for k, v in my_dict.items() if condition(k, v)}

#Define a function which takes two lists as parameters and check if two given lists
# have the same frequency of elements.

def check_same_frequency(list1, list2):
    if len(list1) != len(list2):
        return False
    dict1 = {}
    for ele in list1:
        if ele in dict1:
            dict1[ele] += 1
        else:
            dict1[ele] = 1

    dict2 = {}
    for ele in list2:
        if ele in dict2:
            dict2[ele] += 1
        else:
            dict2[ele] = 1
    if dict1 == dict2:
        return True
    return False

def check_same_frequency1(list1, list2):
    def count_elements(lst):
        counter = {}
        for element in lst:
            counter[element] = counter.get(element, 0) + 1
        return counter

