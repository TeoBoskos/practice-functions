# !!!Number 1: Find the largest item in a list.


def list_largest(lyst: list) -> str:
    """
    This function takes a parameter, `lyst`, which is a list and loops
    through it and returns the largest item.

    :param lyst: The list that the user inputs.
    :return: The largest item in the list in the form of a string.
    """

    largest = lyst[0]
    for item in lyst:
        if len(item) > len(largest):
            largest = item

    return largest


# Uncomment to test:
# answer = list_largest(['a', 'bb', 'ccc'])
# print(answer)

# !!!Number 2: Find the smallest item in the list.


def list_smallest(lyst: list) -> str:
    """
    This function takes a parameter, `lyst`, which is a list and loops
    through it and returns the smallest item.

    :param lyst: The list that the user inputs.
    :return: The smallest item in the list in the form of a string.
    """

    smallest = lyst[0]
    for item in lyst:
        if len(item) < len(smallest):
            smallest = item

    return smallest


# Uncomment to test:
# answer = list_smallest(['a', 'bb', 'ccc'])
# print(answer)

# !!!Number 3: Find the square of a number:


def find_square(numb: int) -> int:
    """
    This function takes a parameter, `numb`, which is an integer and
    returns the squared up version of that integer.

    :param numb: The integer that the user inputs.
    :return: The squared up version of the integer that the user gave.
    """

    squared = numb * numb
    return squared


# Uncomment to test:
# answer = find_square(2)
# print(answer)

# !!!Number 4: Find the cube of a number.


def find_cube(numb: int) -> int:
    """
    This function takes a parameter, `numb`, which is an integer and
    returns the cubed up version of that integer.

    :param numb: The integer that the user inputs.
    :return: The cubed up version of the integer that the user gave.
    """

    cubed = numb * numb * numb
    return cubed


# Uncomment to test:
# answer = find_cube(2)
# print(answer)

# !!!Number 5: Check if a given number is prime.


def is_prime(numb: int) -> bool:
    """
    This function takes a parameter, `numb`, which is an integer and
    checks if it is a prime number or not.

    :param numb: The integer that the user inputs.
    :return: A boolean value, depending on whether the given integer
        is prime or not.
    """

    if numb <= 1:
        return False
    for i in range(2, int(numb ** 0.5) + 1):
        if numb % i == 0:
            return False
    return True


# Uncomment to test.
# print(is_prime(7))

# !!!Number 6: Find the sum of all even numbers in the range 1-100.


def sum_of_even_100() -> int:
    """
    This function calculates and returns the sum of all the even
    numbers within the range 1-100.

    :return: The sum of all the even numbers within the range 1-100.
    """

    summ = 0
    for i in range(2, 101, 2):
        summ += i

    return summ


# Uncomment to test.
# answer = sum_of_even_100()
# print(answer)

# !!!Number 7: Find the sum of all the odd numbers in the range 1-100.


def sum_of_odd_100() -> int:
    """
    This function calculates and returns the sum of all the odd
    numbers withing within the range 1-100.

    :return: The sum of all the odd numbers withing the range 1-100.
    """

    summ = 0
    for i in range(1, 101, 2):
        summ += i

    return summ


# Uncomment to test.
# answer = sum_of_odd_100()
# print(answer)

# !!!Number 8: Find the length of a string.


def length_of_str(string: str) -> int:
    """
    This function takes a parameter, `string`, which is a string. Then,
    it finds and returns the length of that string.

    :param string:
    :return:
    """

    length = 0
    for char in string:
        length += 1

    return length


# Uncomment to test.
# answer = length_of_str('Hello world!')
# print(answer)

# !!!Number 9: Concatenate two strings.


def concatenate_two_strings(str1: str, str2: str) -> str:
    """
    This function takes two parameters that are strings, `str1` and
    `str1` and concatenates them into a single string. Then it returns
    this value.

    :param str1: The first string that the user inputs.
    :param str2: The second string that the user inputs.
    :return: The combined string that the user inputs.
    """

    new_str = str1 + str2
    return new_str


# Uncomment to test.
# answer = concatenate_two_strings('Hello ', 'world!')
# print(answer)

# !!!Number 10: Convert a string to uppercase.


def convert_to_uppercase(string: str) -> str:
    """
    This function converts a given string to uppercase.

    :param string: The string that the user inputs that will be
        converted to uppercase.
    :return: The uppercase version of the string that the user
        inputs.
    """

    upper_cased = string.upper()
    return upper_cased


# Uncomment to test.
# answer = convert_to_uppercase('hello')
# print(answer)

# !!!Number 11: Convert a string to lowercase.


def convert_to_lowercase(string: str) -> str:
    """
    This string converts a string to lowercase.

    :param string: The string that the user inputs.
    :return: The lowercased version of the string.
    """

    lower_cased = string.lower()
    return lower_cased


# Uncomment to test.
# answer = convert_to_lowercase('HELLO')
# print(answer)

# !!!Number 12: Remove whitespace from a string.


def remove_space_from_string(string: str) -> str:
    """
    This function removes all whitespaces from the given
    string.

    :param string: The string that the user inputs.
    :return: The string without any whitespaces.
    """

    without_space = ''
    for char in string:
        if char != ' ':
            without_space += char

    return without_space


# Uncomment to test.
# answer = remove_space_from_string('Hello world')
# print(answer)

# !!!Number 13: Find the area of a rectangle.


def find_area_of_rectangle(length: int, width: int) -> int:
    """
    This function takes two parameter that are both integers,
    `length` and `width`. Then, with these two, it calculates
    the area of a rectangle.

    :param length: The length of the rectangle.
    :param width: The width of the rectangle.
    :return: The area of the rectangle.
    """

    area = length * width
    return area


# Uncomment to test.
# answer = find_area_of_rectangle(8, 2)
# print(answer)

# !!!Number 14: Find the area of a circle.


def find_area_of_circle(radius: int) -> float:
    """
    This function takes the radius of a circle and
    calculates its area.

    :param radius: The integer that the user inputs.
    :return: The area of the circle.
    """

    area = 3.14 * radius * radius
    return area


# Uncomment to test.
# answer = find_area_of_circle(1)
# print(answer)

# !!!Number 15: Find the volume of a sphere.


def find_volume_of_sphere(radius: int) -> float:
    """
    This program calculates the volume of a sphere.

    :param radius: The radius of the sphere.
    :return: The volume of the sphere.
    """

    volume = 4/3 * 3.14 * radius * radius * radius
    return volume


# Uncomment to test.
# answer = find_volume_of_sphere(1)
# print(answer)

# !!!Number 16: Convert Celsius to Fahrenheit.


def celsius_to_fahrenheit(cel: int) -> float:
    """
    This function takes a parameter, `cel`, which is an integer.
    It stands for the amount of degrees Celsius. Then it proceeds
    to convert it to degrees Fahrenheit.

    :param cel: The degrees Celsius that the user inputs.
    :return: The degrees Fahrenheit.
    """

    far = cel * 1.8 + 32
    return far


# Uncomment to test.
# answer = celsius_to_fahrenheit(40)
# print(answer)

# !!!Number 17: Convert Fahrenheit to Celsius.


def fahrenheit_to_celsius(far: int) -> float:
    """
    This function takes a parameter, far, which is an integer.
    It stands for the amount of degrees Fahrenheit. Then it proceeds
    to convert it to degrees Celsius.

    :param far: The degrees Fahrenheit that the user inputs.
    :return: The degrees Celsius.
    """

    cel = (far - 32) * 5 / 9
    return cel


# Uncomment to test.
# answer = fahrenheit_to_celsius(104)
# print(answer)

# !!! Number 18: Find the sum of the digits of a number.


def sum_digits_of_num(numb: int) -> int:
    """
    This function takes one parameter, `numb` which is an integer.
    It converts it into a string in order to loop through it and add
    every single one of its digits, after converting them back to
    integers, into a variable called `summ`. Then, it returns `summ`.

    :param numb: The integer that the user inputs.
    :return: The sum of all the digits of the integer.
    """

    summ = 0

    str_num = str(numb)
    for digit in str_num:
        summ += int(digit)

    return summ


# Uncomment to test.
# answer = sum_digits_of_num(5)
# print(answer)

# !!!Number 19: Find the product of the digits of a number.


def product_digits_of_num(numb: int) -> int:
    """
    This function takes an integer as a parameter, `numb`. It
    converts `numb` to a string before looping through every
    single one of its digits, converting them back to integers
    and multiplying them with the variable `summ`.

    :param numb: The integer that the user inputs.
    :return: The product of the digits of the integer.
    """

    summ = 1

    str_num = str(numb)
    for digit in str_num:
        summ *= int(digit)

    return summ


# Uncomment to test.
# answer = product_digits_of_num(1234)
# print(answer)

# !!!Number 20: Check if a number is a palindrome.


def num_palindrome(num: int) -> bool:
    """
    This function checks if a given number
    is a palindrome.

    :param num: The integer that the user inputs.
    :return: A boolean value, depending on if the
    number is a palindrome.
    """

    num_str = str(num)
    rev_num_str = num_str[::-1]

    if num_str == rev_num_str:
        return True
    else:
        return False


# Uncomment to test.
# answer = num_palindrome(32123)
# print(answer)


# !!!Number 21: Find the factorial of a number using recursion.


def factorial_recursion(num: int, fact: int) -> int:
    """
    This function takes two parameter, `num` and `fact`, which are
    both integers. It uses recursion in order to calculate the factorial
    of `num`.

    :param num: The integer whose factorial is going to be calculated.
    :param fact: The factorial of `num`.
    :return: `fact`.
    """

    if num == 0:
        return fact
    else:
        if num == 1:
            return factorial_recursion(0, fact)
        else:
            fact *= num
            return factorial_recursion(num -  1, fact)


# Uncomment to test.
# answer = factorial_recursion(4, 1)
# print(answer)

# !!!Number 22: Use recursion to find a specific fibonacci number.


def fibonacci(n: int) -> int:
    """
    This function takes one parameter, `n`, which is an integer.
    `n` represents the `n` th fibonacci number which the function
    is going to calculate.

    :param n: The `n` th fibonacci number.
    :return: The `n` th fibonacci number.
    """

    if n == 1 or n == 2:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)


# Uncomment to test.
# answer = fibonacci(7)
# print(answer)

# !!!Number 23: Find the GCD of two numbers.


def gcd(num1: int, num2: int) -> int:
    """
    This function calculates the GCD ( ΜΚΔ ) of two numbers.
    These numbers are represented by the parameters `num1` and
    `num2`.

    :param num1: The first number.
    :param num2: The second number.
    :return: The GCD of the two numbers.
    """

    if num2 == 0:
        return num1
    else:
        return gcd(num2, num1 % num2)


# Uncomment to test.
# answer = gcd(12, 54)
# print(answer)

# !!!Number 24: Find the LCM of two numbers.


def lcm(num1: int, num2: int) -> int:
    """
    This function takes two integer parameters, `num1` and `num2`.
    Then it proceeds to calculate their LCM ( ΕΚΠ ).

    :param num1: The first integer that the user inputs.
    :param num2: The second integer that the user inputs.
    :return: The LCM of the two numbers.
    """

    if num1 > num2:
        num1, num2 = num2, num1
    for i in range(num2, num1 * num2 + 1, num2):
        if i % num1 == 0:
            return i


# Uncomment to test.
# answer = lcm(3, 4)
# print(answer)

# !!!Number 25: Check if a given number is a perfect number.


def is_perfect(n: int) -> bool:
    """
    This function takes a given number and returns true if
    it is a perfect number and false if it's not.

    :param n: The given number.
    :return: A boolean value indicating whether the given
        number is perfect or not.
    """

    list_of_div = []
    final = 0

    if n == 0:
        return False

    for i in range(1, n):
        if n % i == 0:
            list_of_div.append(i)

    for digit in list_of_div:
        final += digit

    if final == n:
        return True
    else:
        return False


# Uncomment to test.
# answer = is_perfect(28)
# print(answer)

# !!!Number 26: Find the factors of a given number.


def find_factors(n: int) -> list:
    """
    This function calculates the factors of a given number
    and returns them in a list.

    :param n: The given number whose factors are going to be
        calculated.
    :return: The list `factors` were the factors of the given
        number are.
    """

    factors = []

    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)

    return factors


# Uncomment to test.
# answer = find_factors(117)
# print(answer)

# !!!Number 27: Find the sum of digits of a number until it becomes a single digit number.


def sum_of_digits(n: int) -> int:  # FURTHER WORK NEEDED!!!
    """
    This function calculates the sum of the digits of a number until
    it becomes a single digit number.

    :param n:
    :return:
    """

    summ = 0

    if n < 10:
        return n

    n_str = str(n)
    n_list = list(n_str)

    while len(n_list) > 1:
        for digit in n_list:
            summ += int(digit)
        n_str = str(summ)
        n_list = list(n_str)

    return summ


# Uncomment to test.
# answer = sum_of_digits(12)
# print(answer)

# !!!Number 28: Find the square root of a given number.


def square_root(n: int) -> int:
    """
    This function takes a given number as a parameter
    and calculates its square root.

    :param n: The given number whose square root is
        going to be calculated.
    :return: The square root of the given number.
    """

    root = None

    if n == 1:
        root = n

    for i in range(1, n):
        if i * i == n:
            root = i
            break

    return root


# Uncomment to test.
# answer = square_root(16)
# print(answer)

# !!!Number 29: Find the cube root of a given number.


def cube_root(n: int) -> int:
    """
    This function takes a given number as a parameter
    and calculated its cube root.

    :param n: The given number whose cube root is going
        to be calculated.
    :return: The cube root of the number.
    """

    root = None

    if n == 1:
        root = n

    for i in range(1, n):
        if i * i * i == n:
            root = i
            break

    return root


# Uncomment to test.
# answer = cube_root(64)
# print(answer)

# !!!Number 30: Find the sum of all prime numbers between 1 and 100.


def sum_of_prime() -> int:
    """
    This function calculates and returns the sum of all the
    prime numbers in the range 1 to 100, which is 1060.

    :return: The sum of all the prime numbers in the range
        1 to 100.
    """

    summ = 0

    for i in range(2, 101):
        is_prime_flag = True
        for numb in range(2, i):
            if i % numb == 0:  # If `i` is divisible by `numb`, it's not a prime number
                is_prime_flag = False
                break

        if is_prime_flag:
            summ += i

    return summ


# Uncomment to test.
# answer = sum_of_prime()
# print(answer)

# !!!Number 31: Find the sum of all composite numbers between 1 and 100.


def sum_of_comp() -> int:
    """
    This function calculates and returns the sum of all the
    composite numbers in the range 1 to 100, which is 4317.

    :return: The sum of all the composite numbers in the range
        1 to 100.
    """

    summ = 0

    for i in range(1, 101):
        if not is_prime(i):
            summ += i

    return summ


# Uncomment to test.
# answer = sum_of_comp()
# print(answer)

# !!!Number 32: Find the area of a triangle given its base and height.


def area_of_triangle(base: int, height: int) -> float:
    """
    This function takes two int parameters, `base` and `height`,
    which are the base and height of a triangle accordingly.
    It uses these to calculate the area of this given triangle.

    :param base: The base of the triangle.
    :param height: The height of the triangle.
    :return: The area of the triangle.
    """

    area = (base * height) / 2
    return area


# Uncomment to test.
# answer = area_of_triangle(7, 2)
# print(answer)

# !!!Number 33: Find the volume of a cylinder given its radius and height.


def volume_of_cylinder(radius: int, height: int) -> float:
    """
    This function takes two int parameters, `radius` and `height`.
    They are the radius and the height of a cylinder accordingly.
    It uses these to calculate the volume of this given cylinder.

    :param radius: The radius of the cylinder.
    :param height: The height of the cylinder.
    :return: The volume of the cylinder.
    """

    pi = 3.14
    volume = pi * radius * radius * height
    return volume


# Uncomment to test.
# answer = volume_of_cylinder(7, 7)
# print(answer)

# !!!Number 34: Find the volume of a cone given its radius and height.


def volume_of_cone(radius: int, height: int) -> float:
    """
    This function calculates the volume of a cone using
    its radius and height.

    :param radius: The radius of the given cone.
    :param height: The height of the given cone.
    :return: The volume of the given cone.
    """

    pi = 3.14
    volume = 1 / 3 * pi * radius * radius * height
    return volume


# Uncomment to test.
# answer = volume_of_cone(7, 7)
# print(answer)

# !!!Number 35: Find the volume of a cube given its side length.


def volume_of_cube(side: int) -> int:
    """
    This function calculates the volume of a given cube
    using its side length.

    :param side: The side length of the given cube.
    :return: The volume of the given cube.
    """

    volume = side ** 3
    return volume


# Uncomment to test.
# answer = volume_of_cube(7)
# print(answer)

# !!!Number 36: Find the volume of a rectangular prism given its length, width and height.


def volume_rect_prism(length: int, width: int, height: int) -> int:
    """
    This function calculates the volume of a given rectangular prism
    using its length, width, and height.

    :param length: The length of the given rectangular prism.
    :param width: The width of the given rectangular prism.
    :param height: The height of the given rectangular prism.
    :return: The volume of the given rectangular prism.
    """

    volume = length * width * height
    return volume


# Uncomment to test.
# answer = volume_rect_prism(1, 1, 7)
# print(answer)

# !!!Number 37: Find the volume of a pyramid given its base area and height.


def volume_pyramid(base_area: int, height: int) -> float:
    """
    This function calculates the volume of a given pyramid using
    its base area and its height.

    :param base_area: The base area of the given pyramid.
    :param height: The height of the given pyramid.
    :return: The volume of the given pyramid.
    """

    volume = 1 / 3 * base_area ** 2 * height
    return volume


# Uncomment to test
# answer = volume_pyramid(7, 9)
# print(answer)

# !!!Number 38: Find the volume of a sphere given its radius.


def volume_sphere(radius: int) -> float:
    """
    This function calculates the volume of a given sphere
    using its radius.

    :param radius: The radius of the given sphere.
    :return: The volume of the given sphere.
    """

    pi = 3.14
    volume = 4 / 3 * pi * radius ** 3
    return volume


# Uncomment to test.
# answer = volume_sphere(7)
# print(answer)

# !!!Number 39: Check if a given number is a perfect square.


def check_for_perfect_square(n: int) -> bool:
    """
    This function takes a number and checks if it
    is a perfect square.

    :param n: The given number.
    :return: A boolean value indicating whether
        the given number is a perfect square.
    """

    square_it_is = False

    for i in range(1, n):
        if i * i == n:
            square_it_is = True
            break
        else:
            square_it_is = False

    return square_it_is


# Uncomment to test.
# answer = check_for_perfect_square(25)
# print(answer)

# !!!Number 40: Count the digits of a number.


def count_digits(n: int) -> int:
    """
    This function counts the digits of a given
    number.

    :param n: The given number.
    :return: The number of digits of the given
        number.
    """

    number_of_digits = 0

    while n != 0:
        n = n // 10
        number_of_digits += 1

    return number_of_digits


# Uncomment to test.
# answer = count_digits(117)
# print(answer)

# !!!Number 41: Check if a given number is an Armstrong number.


def is_armstrong(n: int) -> bool:
    """
    This function takes a given number, and with the help
    of another function ( `count_digits` ) it tells us
    whether this number is an Armstrong number.

    :param n: The given number.
    :return: A boolean value indicating whether the given
        number is an Armstrong number.
    """

    if n == 0:
        return False

    digits = count_digits(n)
    temp = n
    summ = 0

    while temp != 0:
        digit = temp % 10  # That gives us the remainder.
        temp = temp // 10
        summ += digit ** digits

    return summ == n


# Uncomment to test.
# answer = is_armstrong(7)
# print(answer)

# !!!Number 42: Find the sum of all the Armstrong numbers between 1 and 1000.


def armstrong_1000() -> int:
    """
    This function calculates the sum of all the Armstrong
    numbers from 1 to 1000 with the help of two other
    function: `count_digits` and `is_armstrong`.

    :return: The sum of all the Armstrong numbers from 1
        to 1000.
    """

    summ = 0

    for number in range(1, 1001):
        check = is_armstrong(number)
        if check:
            summ += number

    return summ


# Uncomment to test.
# answer = armstrong_1000()
# print(answer)

# !!!Number 43: Check if a given number is a Harshad number.


def check_harsh(n: int) -> bool:
    """
    This function checks if a given number is a Harshad
    number. In other words it checks if the sum of its
    digits is a perfect divisor of the original number.

    :param n: The given number.
    :return: A boolean value indicating whether the given
        number is a Harshad number.
    """

    summ = 0
    n_str = str(n)

    for digit in n_str:
        summ += int(digit)

    if n % summ == 0:
        return True
    else:
        return False


# Uncomment to test.
# answer = check_harsh(117)
# print(answer)

# !!!Number 44: Find the sum of all Harshad numbers between 1 and 1000.


def harsh_1000() -> int:
    """
    This function calculates the sum of all the Harshad
    numbers from 1 to 1000 with the help of another
    function called `check_harsh`.

    :return: The sum of all the Harshad numbers from 1
        to 1000.
    """

    summ = 0

    for number in range(1, 1001):
        check = check_harsh(number)
        if check:
            summ += number

    return summ


# Uncomment to test.
# answer = harsh_1000()
# print(answer)

# !!!Number 45: Find the sum of all even Fibonacci numbers up to 1000.


def even_fibonacci() -> int:
    """
    This function calculates the sum of all the even
    Fibonacci numbers up to 1000 with the help of the
    function `fibonacci`. The final result is 798.
    P.S. I know this is not the most effective way of
    solving such a problem. I am open to criticism.

    :return: The sum of all the even Fibonacci numbers
        up to 1000.
    """

    fib_list = []
    summ = 0

    if not fibonacci(1) % 2 != 0:
        fib_list.append(fibonacci(1))
    if not fibonacci(2) % 2 != 0:
        fib_list.append(fibonacci(2))
    if not fibonacci(3) % 2 != 0:
        fib_list.append(fibonacci(3))
    if not fibonacci(4) % 2 != 0:
        fib_list.append(fibonacci(4))
    if not fibonacci(5) % 2 != 0:
        fib_list.append(fibonacci(5))
    if not fibonacci(6) % 2 != 0:
        fib_list.append(fibonacci(6))
    if not fibonacci(7) % 2 != 0:
        fib_list.append(fibonacci(7))
    if not fibonacci(8) % 2 != 0:
        fib_list.append(fibonacci(8))
    if not fibonacci(9) % 2 != 0:
        fib_list.append(fibonacci(9))
    if not fibonacci(10) % 2 != 0:
        fib_list.append(fibonacci(10))
    if not fibonacci(11) % 2 != 0:
        fib_list.append(fibonacci(11))
    if not fibonacci(12) % 2 != 0:
        fib_list.append(fibonacci(12))
    if not fibonacci(13) % 2 != 0:
        fib_list.append(fibonacci(13))
    if not fibonacci(14) % 2 != 0:
        fib_list.append(fibonacci(14))
    if not fibonacci(15) % 2 != 0:
        fib_list.append(fibonacci(15))
    if not fibonacci(16) % 2 != 0:
        fib_list.append(fibonacci(16))

    for i in fib_list:
        summ += i

    return summ


# Uncomment to test.
# answer = even_fibonacci()
# print(answer)

# !!!Number 46: Find the sum of all the odd Fibonacci numbers up to 1000.


def odd_fibonacci() -> int:
    """
    This function calculates the sum of all the odd
    Fibonacci numbers up to 1000 with the help of the
    function `fibonacci`. The final result is 1785.
    P.S. I know this is not the most effective way of
    solving such a problem. I am open to criticism.

    :return: The sum of all the odd Fibonacci numbers
        up to 1000.
    """

    fib_list = []
    summ = 0

    if not fibonacci(1) % 2 == 0:
        fib_list.append(fibonacci(1))
    if not fibonacci(2) % 2 == 0:
        fib_list.append(fibonacci(2))
    if not fibonacci(3) % 2 == 0:
        fib_list.append(fibonacci(3))
    if not fibonacci(4) % 2 == 0:
        fib_list.append(fibonacci(4))
    if not fibonacci(5) % 2 == 0:
        fib_list.append(fibonacci(5))
    if not fibonacci(6) % 2 == 0:
        fib_list.append(fibonacci(6))
    if not fibonacci(7) % 2 == 0:
        fib_list.append(fibonacci(7))
    if not fibonacci(8) % 2 == 0:
        fib_list.append(fibonacci(8))
    if not fibonacci(9) % 2 == 0:
        fib_list.append(fibonacci(9))
    if not fibonacci(10) % 2 == 0:
        fib_list.append(fibonacci(10))
    if not fibonacci(11) % 2 == 0:
        fib_list.append(fibonacci(11))
    if not fibonacci(12) % 2 == 0:
        fib_list.append(fibonacci(12))
    if not fibonacci(13) % 2 == 0:
        fib_list.append(fibonacci(13))
    if not fibonacci(14) % 2 == 0:
        fib_list.append(fibonacci(14))
    if not fibonacci(15) % 2 == 0:
        fib_list.append(fibonacci(15))
    if not fibonacci(16) % 2 == 0:
        fib_list.append(fibonacci(16))

    for i in fib_list:
        summ += i

    return summ


# Uncomment to test.
# answer = odd_fibonacci()
# print(answer)
