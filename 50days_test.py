import re

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

#Day 12 tests
from day12 import count_dots, age_in_minutes
from datetime import *

def test_count_dots():
    assert count_dots('h.e.l.p.') == 4 and count_dots('he.lp.') == 2

def test_age_in_minutes():
    today = date.today()
    minutes = ((today.year - 1930) * 525600)
    error = 'Invalid input'
    assert age_in_minutes(1930) == minutes and age_in_minutes(1899) == error and age_in_minutes(22500) == error

#Day 13 tests
from day13 import your_vat, python_snakes

def test_your_vat():
    assert your_vat(220, 15) == 253
    
def test_python_snakes():
    # I am unsure how to write a test for python_snakes()
    assert True == True

#Day 14 tests
from day14 import flat_list, your_salary

def test_flat_list():
    example = [[2,4,5,6]]
    assert flat_list(example) == [2,4,5,6]

def test_your_salary():
    assert your_salary(105) == 2125

#Day 15 tests
from day15 import same_in_reverse, your_age

def test_same_in_reverse():
    assert same_in_reverse('dad') == True and same_in_reverse('dads') == False

def test_your_age():
    assert your_age('jane') == 'Hi, jane, you are 23 years old'

#Day 16 tests
from day16 import sum_list, unpack_nest

def test_sum_list():
    list = [[2, 4, 5, 6], [2, 3, 5, 6]]
    assert sum_list(list) == 33

def test_unpack_nest():
    nested_list = [[12, 34, 56, 67], [34, 68, 78]]
    assert unpack_nest(nested_list) == [34, 67, 78]

#Day 17 tests
from day17 import random_user_name, sort_length

def test_random_user_name():
    s= random_user_name('Starla')
    match = re.search(r'alrats+[0-9]', s)
    if match:
        assert True == True
    else:
        assert False == True

def test_sort_length():
    names = ['Peter','Jon','','Andrew','zuul']
    assert sort_length(names) == ['','Jon','zuul','Peter','Andrew']

#Day 18 tests
from day18 import any_number, add_reverse

def test_any_number():
    assert any_number(12, 90, 12, 34) == 37 and any_number(12, 90) == 51

def test_add_reverse():
    list1, list2, list3 = [10, 12, 34], [12, 56, 78], [12, 56]
    error_message = 'the lists are not of equal lengths'
    assert add_reverse(list1, list2) == [112, 68, 22] and add_reverse(list1, list3) == error_message

#Day 19 tests
from day19 import count_words, count_elements

def test_count_words():
    str = 'I love learning'
    assert count_words(str) == 3

def test_count_elements():
    str = 'I love learning'
    assert count_elements(str) == 13

#Day 20 tests
from day20 import capitalizer, reversed_list

def test_capitalizer():
    assert capitalizer('i like learning') == 'I Like Learning'

def test_reversed_list():
    str1 = 'leArning is hard, bUt if You appLy youRself you can achieVe success'
    result = ['gninrAel', 'tUb', 'uoY', 'yLppa', 'flesRuoy', 'eVeihca']
    assert reversed_list(str1) == result

#Day 21 tests
from day21 import make_tuples, even_or_average

def test_make_tuples():
    a, b = [1,2,3,4], [5,6,7,8]
    assert make_tuples(a,b) == [(1, 5), (2, 6), (3, 7), (4, 8)]

def test_even_or_average():
    a, b = [1,2,3,4,5], [1,3,5,7,9]
    assert even_or_average(a) == 4 and even_or_average(b) == 5
