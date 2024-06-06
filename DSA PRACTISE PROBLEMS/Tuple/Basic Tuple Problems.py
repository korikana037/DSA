# Write a function that calculates the sum and product of all elements in a tuple of numbers.

def sum_product(input_tuple):
    sum_result = 0
    product_result = 1
    for i in input_tuple:
        sum_result += i
        product_result *= i

    return sum_result, product_result


# Create a function that takes two tuples and returns a tuple containing the element-wise
# sum of the input tuples

def tuple_elementwise_sum(tuple1, tuple2):
    return tuple(map(sum, zip(tuple1, tuple2)))


def tuple_elementwise_sum1(t1, t2):
    if len(t1) != len(t2):
        raise ValueError("Input tuples must have the same length.")

    result = tuple(a + b for a, b in zip(t1, t2))
    return result

# Write a function that takes a tuple and a value, and returns a new tuple with the
# value inserted at the beginning of the original tuple.


def insert_value_at_beginning(input_tuple, value_to_insert):
    return (value_to_insert,) + input_tuple


def insert_value_front(input_tuple, value_to_insert):
    new_list = [value_to_insert]
    lst1 = list(input_tuple)
    new_list.extend(lst1)
    return tuple(new_list)


# Write a function that takes a tuple of strings and concatenates them, separating
# each string with a space.

def concatenate_strings(input_tuple):
    return ' '.join(input_tuple)


def concatenate_strings1(input_tuple):
    result = ''
    for i in input_tuple:
        if result == '':
            result += i
        else:
            result = result + ' ' + i
    return result


# Create a function that takes a tuple of tuples and returns a tuple containing
# the diagonal elements of the input.

def get_diagonal(input_tuple):
    return tuple(input_tuple[i][i] for i in range(len(input_tuple)))


def get_diagonal1(tup):
    output_tup = ()
    for i in range(len(tup)):
        output_tup += (tup[i][i],)
    return output_tup


# Write a function that takes two tuples and returns a tuple containing the common
# elements of the input tuples.

def common_elements(tuple1, tuple2):
    return tuple(set(tuple1) & set(tuple2))




