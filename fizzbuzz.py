"""Function to solve the fizzbuzz problem."""


def fizz_buzz(num: int) -> str:
    """
    This is my great and neat function to solve the famous
    Fizzbuzz problem
    :param num: That is the number we want an answer for
    :return: "fizz", "buzz", "fizzbuzz" or the number itself
    """
    if num % 15 == 0:
        return "fizzbuzz"
    if num % 5 == 0:
        return "buzz"
    if num % 3 == 0:
        return "fizz"
    return str(num)
