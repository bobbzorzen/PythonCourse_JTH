def assertEqual(a, b):
    try:
        assert a == b
    except:
        print("Assert error, ", a , " not equal to ", b)
        raise


def highest(array_of_numbers):
    highest = array_of_numbers[0]
    for i in range(1, len(array_of_numbers)):
        highest = highest if array_of_numbers[i] < highest else array_of_numbers[i]
    return highest

assertEqual(highest([5, 3]), 5)
assertEqual(highest([2, 8, 4, 3]), 8)
assertEqual(highest([-2, -5]), -2)
assertEqual(highest([42]), 42)


def count(array_of_numbers):
    baseline = [0]*10
    for i in range(0, len(array_of_numbers)):
        array_value = array_of_numbers[i]
        baseline[array_value] += 1
    highest_number = highest(array_of_numbers)
    return baseline[0:highest_number+1]

assertEqual(count([0, 1, 2]), [1, 1, 1])
assertEqual(count([1, 1, 1]), [0, 3])
assertEqual(count([5, 2, 4, 7, 4]), [0, 0, 1, 0, 2, 1, 0, 1])
assertEqual(count([0]), [1])


def are_equal(array_one, array_two):
    if len(array_one) == len(array_two):
        for i in range(0, len(array_one)):
            if array_one[i] != array_two[i]:
                return False
        return True
    return False

assertEqual(are_equal([1, 2, 3], [1, 2, 3]), True)
assertEqual(are_equal([1, 2, 3], [1, 2, 2]), False)
assertEqual(are_equal([1, 2, 3], [1, 2]), False)
assertEqual(are_equal([1, 2], [1, 2, 3]), False)


def are_nested_lists_equal(list_of_lists):
    if len(list_of_lists) < 2:
        return False
    for i in range(1, len(list_of_lists)):
        if not are_equal(list_of_lists[i-1], list_of_lists[i]):
            return False
    return True

assertEqual(are_nested_lists_equal([
    [1, 2, 3],
    [1, 2, 3],
    [1, 2, 3],
]), True)
assertEqual(are_nested_lists_equal([
    [1, 2, 3],
    [1, 2, 2],
    [1, 2, 3],
]), False)
assertEqual(are_nested_lists_equal([
    [1],
    [1, 2],
]), False)


def change_to_highest(list_of_lists):
    for i in range(0, len(list_of_lists)):
        list_of_lists[i] = highest(list_of_lists[i])

the_list = [
    [1, 2, 3],
    [5, 4, 3],
    [2, 7, 6],
]
change_to_highest(the_list)
assertEqual(the_list, [3, 5, 7])
