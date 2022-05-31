import math

def my_1filter(list_of_strings):
    return list(filter(str.isdigit,list_of_strings))
def my_filter(iterable):
    return list(filter(lambda x: x > 3,iterable))

def test_my_filter():
    assert my_filter([1, 2, 3, 4, 5]) == [4, 5]
def test_my_1filter():
    assert my_1filter(['10','66','memo']) == ['10','66']

def my_map(list_1,list_2):
    return list(map(lambda x, y: x - y,list_1,list_2))
def my_2map(numbers):
    return list(map(lambda x: x * 2 + 3, numbers))

def test_my_map():
    assert my_map([2, 4, 6], [1, 3, 5]) == [1,1,1]
def test_2map():
    assert my_2map([1,2,3]) == [5,7,9]

def my_sorted(list_name):
    return sorted(list_name)

def test_my_sorted():
    assert my_sorted(['leo','kate','alex','kirill']) == ['alex','kate','kirill','leo']


def square_root(namber):
    return math.sqrt(namber)
def square_root2(numbers):
    return [math.sqrt(number) for number in numbers]

def test_square_root():
    assert square_root(25) == 5
def test_square_root2():
    assert square_root2([25, 16, 9]) == [5, 4, 3]

def exponentiation(namber):
    return math.pow(namber, 3)
def test_exponentiation():
    assert exponentiation(3) == 27


def hypotenuse(x, y):
    return math.hypot(x, y)


def test_hypotenuse():
    assert hypotenuse(2, 1) == 2.23606797749979