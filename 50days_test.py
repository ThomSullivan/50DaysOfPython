#Day 1 tests
from day1 import divide_or_square, longest_value

def test_divide_or_square():
    assert divide_or_square(10) == 3.16

def test_longest_value():
    fruits = {'fruit': 'apple', 'color': 'green'}
    assert longest_value(fruits) == 'apple'

#Day 2 tests
from day2 import convert_add, check_duplicates

def test_convert_add():
    example =  ['1', '3', '5']
    assert convert_add(example) == 9

def test_check_duplicates():
    fruits = ['apple', 'orange', 'banana', 'apple']
    names = ['Yoda', 'Moses', 'Joshua', 'Mark']
    assert check_duplicates(fruits) == {'apple'} and check_duplicates(names) == 'No duplicates'

#Day 3 tests
from day3 import register_check, lowercase_check

def test_register_check():
    register = {'Michael':'yes','John': 'no', 'Peter':'yes', 'Mary': 'yes'}
    assert register_check(register) == 3

def test_lowercase_check():
    names = ["kerry", "dickson", "John", "Mary", "carol", "Rose", "adam", "zuul"]
    assert lowercase_check(names) == ('zuul','kerry', 'dickson', 'carol', 'adam')

#Day 4 tests
from day4 import only_floats, word_index

def test_only_floats():
    assert only_floats(12.1, 23) == 1

def test_word_index():
    words1 = ["Hate", "remorse", "vengeance"]
    words2 = ["Love", "Hate"]
    assert word_index(words1) == 2 and word_index(words2) == 0

#Day 5 tests
from day5 import my_discount, gender_count

def test_my_discount():
    assert my_discount(150, 15) == 127.5

def test_gender_count():
    students = ['Male', 'Female', 'female', 'male', 'male', 'male', 'female', 'male', 'Female', 'Male', 'Female', 'Male', 'female']
    assert gender_count(students) == [('Male',7), ('female',6)]

#Day 6 tests
from day6 import user_name, zeroed

def test_user_name():
    user = 'ben@gmail.com'
    assert user_name(user) == 'ben'

def test_zeroed():
    input = [2, 5, 7, 8, 9]
    assert zeroed(input) == [0, 5, 7, 8, 0]

#Day 7 tests
from day7 import string_range, find_s

def test_string_range():
    assert string_range(6) == '0.1.2.3.4.5'

def test_find_s():
    names = ["Joseph","Nathan", "Sasha", "Kelly", "Muhammad", "Jabulani", 'Sera' , "Patel" , 'Sera']
    assert find_s(names) == {'Sasha': 1, 'Sera': 2}

#Day 8 tests
from day8 import odd_even, prime_numbers

def test_odd_even():
    list = [1,2,4,6]
    assert odd_even(list) == 5

def test_prime_numbers():
    assert prime_numbers(10) == [2,3,5,7]

#Day 9 tests
from day9 import biggest_odd, zeros_last

def test_biggest_odd():
    assert biggest_odd('23569') == 9

def test_zeros_last():
    input = [2,1,4,7,6]
    input2 = [1,4,6,0,7,0,9]
    assert zeros_last(input) == [1, 2, 4, 6, 7] and zeros_last(input2) == [1, 4, 6, 7, 9, 0, 0]
    
#Day 10 tests
from day10 import hide_password, convert_numbers

def test_hide_password():
    assert hide_password('hello') == '***** user password is 5 characters long'

def test_convert_numbers():
    input = [1000000, 2356989, 2354672, 9878098]
    assert convert_numbers(input) == [ '1,000,000', '2,356,989', '2,354,672', '9,878,098']

#Day 11 test
from day11 import equal_strings, swap_values

def test_equal_strings():
    assert equal_strings('love','evol') == True

def test_swap_values():
    list = [2,4,67,7]
    assert swap_values(list) == [7,4,67,2]
