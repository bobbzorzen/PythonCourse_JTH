
def assertEqual(a, b):
    try:
        assert a == b
    except:
        print("Assert error, ", a , " not equal to ", b)
        raise



def abs(number):
    return number if number >= 0 else number*-1

assertEqual(abs(5), 5)
assertEqual(abs(-5), 5)
assertEqual(abs(0), 0)

def closest_to_zero(number1, number2):
    return number1 if abs(number1) < abs(number2) else number2

assertEqual(closest_to_zero(5, 9), 5)
assertEqual(closest_to_zero(3, -2), -2)
assertEqual(closest_to_zero(2, 2), 2)
assertEqual(closest_to_zero(-2, 2), 2) #Will return the second number since that's how i wrote the return statement

def closest_to_zero_4(number1, number2, number3, number4):
    return closest_to_zero(closest_to_zero(number1, number2), closest_to_zero(number3, number4))

assertEqual(closest_to_zero_4(5, 9, 2, 11), 2)
assertEqual(closest_to_zero_4(0, 3, -2, 4), 0)
assertEqual(closest_to_zero_4(2, 2, -2, 1), 1)

def string_with_numbers(amount_of_numbers):
    string_of_numbers = "1"
    for i in range(2, amount_of_numbers+1):
        string_of_numbers = string_of_numbers + "_" + str(i)
    return string_of_numbers

assertEqual(string_with_numbers(1), "1")
assertEqual(string_with_numbers(2), "1_2")
assertEqual(string_with_numbers(3), "1_2_3")
assertEqual(string_with_numbers(5), "1_2_3_4_5")

