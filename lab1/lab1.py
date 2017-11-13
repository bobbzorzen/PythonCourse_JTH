def assertEqual(a, b):
    try:
        assert a == b
    except:
        print("Assert error, ", a , " not equal to ", b)
        raise

def factorial(factorial_number):
    #Calculate factorial for given number
    factorial_result = 1
    for x in range(1, factorial_number+1):
        factorial_result = factorial_result*x
    return factorial_result
assertEqual(factorial(7), 5040)
assertEqual(factorial(1), 1)


def sum(sum_number):
    sum_result = 0
    for x in range(1, sum_number+1):
        sum_result = sum_result + x
    return sum_result

assertEqual(sum(0), 0)
assertEqual(sum(1), 1)
assertEqual(sum(9), 45)

def exp(base, pow):
    exp_result = 1
    for x in range(0, pow):
        exp_result = exp_result*base
    return exp_result

assertEqual(exp(2,1), 2)
assertEqual(exp(2,2), 4)
assertEqual(exp(5,6), 15625)


def average(first, second, third):
    return (first + second + third)/3


assertEqual(average(4, 4, 4), 4)
assertEqual(average(4, 10, 7), 7)
assertEqual(average(99, 100, 101), 100)
assertEqual(average(-5, 9, 5), 3)


def sum_of_ints(first_in_range, last_in_range):
    sum_result = first_in_range;
    while first_in_range < last_in_range:
        first_in_range = first_in_range + 1
        sum_result = sum_result + first_in_range
    return sum_result
    

assertEqual(sum_of_ints(0, 4), 10)
assertEqual(sum_of_ints(10, 11), 21)
assertEqual(sum_of_ints(7, 7), 7)
assertEqual(sum_of_ints(-2, 2), 0)
assertEqual(sum_of_ints(-4, 0), -10)


def xxx(amount_of_sums):
    sum_result = 0;
    while amount_of_sums > 0:
        counter = amount_of_sums
        while counter > 0:
            sum_result = sum_result + amount_of_sums
            counter = counter-1
        amount_of_sums = amount_of_sums-1
    return sum_result

assertEqual(xxx(1), 1)
assertEqual(xxx(2), 5)
assertEqual(xxx(3), 14)
assertEqual(xxx(4), 30)




