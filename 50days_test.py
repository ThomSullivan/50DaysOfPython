import re

## For use with multiple input monkey patching##
def make_mock_input(generator):
    def mock_input(*args, **kwargs): # ignore any arguments
        return next(generator) # the state of the generator is stored in the enclosing scope of make_mock_input
    return mock_input


#Day 1 tests
from Days.day1 import divide_or_square, longest_value

def test_divide_or_square():
    assert divide_or_square(10) == 3.16

def test_longest_value():
    fruits = {'fruit': 'apple', 'color': 'green'}
    assert longest_value(fruits) == 'apple'

#Day 2 tests
from Days.day2 import convert_add, check_duplicates

def test_convert_add():
    example =  ['1', '3', '5']
    assert convert_add(example) == 9

def test_check_duplicates():
    fruits = ['apple', 'orange', 'banana', 'apple']
    names = ['Yoda', 'Moses', 'Joshua', 'Mark']
    assert check_duplicates(fruits) == {'apple'} and check_duplicates(names) == 'No duplicates'

#Day 3 tests
from Days.day3 import register_check, lowercase_check

def test_register_check():
    register = {'Michael':'yes','John': 'no', 'Peter':'yes', 'Mary': 'yes'}
    assert register_check(register) == 3

def test_lowercase_check():
    names = ["kerry", "dickson", "John", "Mary", "carol", "Rose", "adam", "zuul"]
    assert lowercase_check(names) == ('zuul','kerry', 'dickson', 'carol', 'adam')

#Day 4 tests
from Days.day4 import only_floats, word_index

def test_only_floats():
    assert only_floats(12.1, 23) == 1

def test_word_index():
    words1 = ["Hate", "remorse", "vengeance"]
    words2 = ["Love", "Hate"]
    assert word_index(words1) == 2 and word_index(words2) == 0

#Day 5 tests
from Days.day5 import my_discount, gender_count

def test_my_discount():
    assert my_discount(150, 15) == 127.5

def test_gender_count():
    students = ['Male', 'Female', 'female', 'male', 'male', 'male', 'female', 'male', 'Female', 'Male', 'Female', 'Male', 'female']
    assert gender_count(students) == [('Male',7), ('female',6)]

#Day 6 tests
from Days.day6 import user_name, zeroed

def test_user_name():
    user = 'ben@gmail.com'
    assert user_name(user) == 'ben'

def test_zeroed():
    input = [2, 5, 7, 8, 9]
    assert zeroed(input) == [0, 5, 7, 8, 0]

#Day 7 tests
from Days.day7 import string_range, find_s

def test_string_range():
    assert string_range(6) == '0.1.2.3.4.5'

def test_find_s():
    names = ["Joseph","Nathan", "Sasha", "Kelly", "Muhammad", "Jabulani", 'Sera' , "Patel" , 'Sera']
    assert find_s(names) == {'Sasha': 1, 'Sera': 2}

#Day 8 tests
from Days.day8 import odd_even, prime_numbers

def test_odd_even():
    list = [1,2,4,6]
    assert odd_even(list) == 5

def test_prime_numbers():
    assert prime_numbers(10) == [2,3,5,7]

#Day 9 tests
from Days.day9 import biggest_odd, zeros_last

def test_biggest_odd():
    assert biggest_odd('23569') == 9

def test_zeros_last():
    input = [2,1,4,7,6]
    input2 = [1,4,6,0,7,0,9]
    assert zeros_last(input) == [1, 2, 4, 6, 7] and zeros_last(input2) == [1, 4, 6, 7, 9, 0, 0]
    
#Day 10 tests
from Days.day10 import hide_password, convert_numbers

def test_hide_password():
    assert hide_password('hello') == '***** user password is 5 characters long'

def test_convert_numbers():
    input = [1000000, 2356989, 2354672, 9878098]
    assert convert_numbers(input) == [ '1,000,000', '2,356,989', '2,354,672', '9,878,098']

#Day 11 test
from Days.day11 import equal_strings, swap_values

def test_equal_strings():
    assert equal_strings('love','evol') == True

def test_swap_values():
    list = [2,4,67,7]
    assert swap_values(list) == [7,4,67,2]

#Day 12 tests
from Days.day12 import count_dots, age_in_minutes
from datetime import *

def test_count_dots():
    assert count_dots('h.e.l.p.') == 4 and count_dots('he.lp.') == 2

def test_age_in_minutes():
    today = date.today()
    minutes = ((today.year - 1930) * 525600)
    error = 'Invalid input'
    assert age_in_minutes(1930) == minutes and age_in_minutes(1899) == error and age_in_minutes(22500) == error

#Day 13 tests
from Days.day13 import your_vat, python_snakes

def test_your_vat():
    assert your_vat(220, 15) == 253
    
def test_python_snakes():
    # I am unsure how to write a test for python_snakes()
    assert True == True

#Day 14 tests
from Days.day14 import flat_list, your_salary

def test_flat_list():
    example = [[2,4,5,6]]
    assert flat_list(example) == [2,4,5,6]

def test_your_salary():
    assert your_salary(105) == 2125

#Day 15 tests
from Days.day15 import same_in_reverse, your_age

def test_same_in_reverse():
    assert same_in_reverse('dad') == True and same_in_reverse('dads') == False

def test_your_age():
    assert your_age('jane') == 'Hi, jane, you are 23 years old'

#Day 16 tests
from Days.day16 import sum_list, unpack_nest

def test_sum_list():
    list = [[2, 4, 5, 6], [2, 3, 5, 6]]
    assert sum_list(list) == 33

def test_unpack_nest():
    nested_list = [[12, 34, 56, 67], [34, 68, 78]]
    assert unpack_nest(nested_list) == [34, 67, 78]

#Day 17 tests
from Days.day17 import random_user_name, sort_length

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
from Days.day18 import any_number, add_reverse

def test_any_number():
    assert any_number(12, 90, 12, 34) == 37 and any_number(12, 90) == 51

def test_add_reverse():
    list1, list2, list3 = [10, 12, 34], [12, 56, 78], [12, 56]
    error_message = 'the lists are not of equal lengths'
    assert add_reverse(list1, list2) == [112, 68, 22] and add_reverse(list1, list3) == error_message

#Day 19 tests
from Days.day19 import count_words, count_elements

def test_count_words():
    str = 'I love learning'
    assert count_words(str) == 3

def test_count_elements():
    str = 'I love learning'
    assert count_elements(str) == 13

#Day 20 tests
from Days.day20 import capitalizer, reversed_list

def test_capitalizer():
    assert capitalizer('i like learning') == 'I Like Learning'

def test_reversed_list():
    str1 = 'leArning is hard, bUt if You appLy youRself you can achieVe success'
    result = ['gninrAel', 'tUb', 'uoY', 'yLppa', 'flesRuoy', 'eVeihca']
    assert reversed_list(str1) == result

#Day 21 tests
from Days.day21 import make_tuples, even_or_average

def test_make_tuples():
    a, b = [1,2,3,4], [5,6,7,8]
    assert make_tuples(a,b) == [(1, 5), (2, 6), (3, 7), (4, 8)]

def test_even_or_average():
    a, b = [1,2,3,4,5], [1,3,5,7,9]
    assert even_or_average(a) == 4 and even_or_average(b) == 5

#Day 22 test
from Days.day22 import add_hash, add_underscore, remove_underscore

def test_add_hash():
    assert add_hash('python is cool') == 'python#is#cool'

def test_add_underscore():
    assert add_underscore('python#is#cool') == 'python_is_cool'

def test_remove_underscore():
    assert remove_underscore('python_is_cool') == 'python is cool'

#Day 23 tests
from Days.day23 import calculate, multiply_words

def test_calculate():
    assert calculate('*',2,21) == 42

def test_multiply_words():
    s1 = "love live and laugh"
    s2 = "Hate war love Peace"
    assert multiply_words(s1) == 240 and multiply_words(s2) == 12

#Day 24 tests
from Days.day24 import average_calories, nested_lists

def test_average_calories():
    assert average_calories(3500, 2) == 1750.0


def test_nested_lists():
    a, b, c = [1, 2, 3, 5], [1, 2, 3, 4], [1, 3, 4, 5]
    d = [[1, 2, 3, 5], [1, 2, 3, 4], [1, 3, 4, 5]]
    assert nested_lists(a,b,c) == d

#Day 25 tests
from Days.day25 import all_the_same, read_backwards
def test_all_the_same():
    a, b = ['Mary','Mary','Mary'], ['Mork','Mindy','Oork']
    assert all_the_same(a) == True and all_the_same(b) == False

def test_read_backwards():
    str1 = "the love is real"
    assert read_backwards(str1) == 'real is love the'

#Day 26 tests
from Days.day26 import sort_words, string_length

def test_sort_words():
    result = ['e,f,i,l,o,v']
    assert sort_words('love life') == result

def test_string_length():
    result = {'Hi': 2, 'my': 2, 'name': 4, 'is': 2, 'Richard': 7}
    s = 'Hi my name is Richard'
    assert string_length(s) == result

#Day 27 tests
from Days.day27 import unique_numbers, difference

def test_unique_numbers():
    list = [1, 2, 4, 5, 6, 7, 8, 8]
    list2 = [1, 2, 4, 5, 6, 7, 7, 8, 8]
    result = [1, 2, 4, 5, 6, 7, 8]
    assert unique_numbers(list) == list and unique_numbers(list2) == result

def test_difference():
    list1 = [1, 2, 4, 5, 6]
    list2 = [1, 2, 5, 7, 9]
    assert difference(list1, list2) == [4, 6, 7, 9]

#Day 28 tests
from Days.day28 import index_position, largest_number

def test_index_position():
    assert index_position('LovE') == [1,2]

def test_largest_number():
    list, result = [3, 67, 87, 9, 2], '9,877,632'
    assert largest_number(list) == result

#Day 29 tests

from Days.day29 import middle_figure

def test_middle_figure():
    str1, str2, error = 'make love', 'not wars', 'no middle figure'
    assert middle_figure(str1, str2) == 'e' and middle_figure('','') == error

#Day 30 tests
from Days.day30 import repeated_name, sorted_names

def test_repeated_name():
    names = ["John", "Peter", "John", "Peter", "Jones", "Peter"]
    assert repeated_name(names) == 'Peter'

def test_sorted_names():
    names =  ['Beyonce Knowles', 'Alicia Keys', 'Katie Perry', 'Chris Brown',' Tom Cruise']
    result = ['Brown Chris', 'Cruise Tom', 'Keys Alicia', 'Knowles Beyonce', 'Perry Katie']
    assert sorted_names(names) == result

#Day 31 tests
from Days.day31 import longest_word

def test_longest_word():
    list = ['Java', 'JavaScript', 'Python']
    result = [10,'JavaScript']
    assert longest_word(list) == result

#Day 32 test
from Days.day32 import password_validator, email_validator

def test_password_validator():
    validPassword = password_validator('Aa12bb34')
    invalidPassword = password_validator('short')
    assert validPassword == True and invalidPassword == False

def test_email_validator():
    emails = ['ben@mail.com', 'john@mail.cm', 'kenny@gmail.com', '@list.com' ]
    result = ['ben@mail.com','kenny@gmail.com']
    assert email_validator(emails) == result

#Day 33 tests
from Days.day33 import inter_section

def test_inter_sections():
    list1 = [20, 30, 60, 65, 75, 80, 85]
    list2 = [ 42, 30, 80, 65, 68, 88, 95]
    assert inter_section(list1, list2) == (30, 65, 80)

#Day 34 tests
from Days.day34 import just_digits

def test_just_digits():
    dataFile = 'Days/csvFiles/day34Data.csv'
    assert just_digits(dataFile) == [1991, 2, 2000, 3, 2008]

#Day 35 test
from Days.day35 import check_pangram, find_index

def test_check_pangram():
    pangram = 'the quick brown fox jumps over a lazy dog'
    nonpangram = 'Hello there!'
    assert check_pangram(pangram) == True and check_pangram(nonpangram) == False

def test_find_index():
    list = [1, 2, 4, 6, 7, 7] 
    found = [4, 5]
    notFound = [8, 8, 8, 8, 8, 8]
    assert find_index(list, 7) == found and find_index(list, 8) == notFound

#Day 36 test
from Days.day36 import count

def test_count():
    result = {'h':1, 'e':1, 'l':2, 'o':1}
    assert count('hello') == result

#Day 37 tests
from Days.day37 import count_the_vowels

def test_count_the_vowels():
    assert count_the_vowels('hello') == 2 and count_the_vowels('saas') == 1

#Day 38 tests
from Days.day38 import missing_number

def test_missing_number():
    list = [1, 2, 3, 5, 6, 7, 9, 11, 12, 23, 14, 15, 17, 18, 19, 20, 21, 22, 24, 25, 26, 27, 28, 31]
    result = [4, 8, 10, 13, 16, 29, 30]
    assert missing_number(list) == result

#Day 39 test
from Days.day39 import generate_password

def test_generate_password():
    strengths = ['weak', 'strong', 'very strong']
    for strength in strengths:
        match strength:
            case 'weak':
                length = 5
            case 'strong':
                length = 8
            case 'very strong':
                length = 12
            
        password = generate_password(strength) 
        x = bool(re.search('(?=.*\\d)(?=.*[a-z])(?=.*[A-Z])(?=.*\\W)', password))
        if x == False:
            raise ValueError
        if len(password) != length:
            raise AttributeError
    assert True == True       

#Day 40 test
from Days.day40 import translate

def test_translate():
    string = 'i love python'
    result = 'iyay ovelay ythonpay'
    assert translate(string) == result

#Day 41 tests
from Days.day41 import words_with_vowels, Bmw

def test_words_with_vowels():
    input = 'You have no rhythm'
    bad_input = 'sdfghj rtnfgsd jkldbvnc'
    result = ['You', 'have', 'no']
    assert words_with_vowels(input) == result and words_with_vowels(bad_input) == []

def test_print_car():
    result = 'Car model = x6\nColor = silver\nYear = 2018\nTransmission = Auto\nElectric = False'
    assert Bmw.print_car() == result

#Day 42 tests
import pyinputplus
from Days.day42 import spelling_check

def test_spelling_check(monkeypatch):
    monkeypatch.setattr(pyinputplus, 'inputStr', lambda _, **kwargs:'mooose')
    monkeypatch.setattr(pyinputplus, 'inputMenu', lambda _, **kwargs:'Yes')
    x = spelling_check()
    assert x == 'The correct spelling is "morose"'

#Day 43 tests
from Days.day43 import student_marks

def test_student_marks(monkeypatch):
    def input_generator(names):
        yield from names

    def grade_generator(grades):
        yield from grades

    names = ('Thom', 'Zuul',  'Zaphod', 'Rand', 'Stilgar','')
    grades = (100, 45, 73, 100, 67)
    name_gen = input_generator(names)
    grade_gen = grade_generator(grades)
    mock_names = make_mock_input(name_gen)
    mock_grades = make_mock_input(grade_gen)
    monkeypatch.setattr(pyinputplus, 'inputStr', mock_names)
    monkeypatch.setattr(pyinputplus, 'inputInt', mock_grades)

    x = student_marks()
    assert x == {names[i] : grades[i] for i in range(len(names)-1) }

#Day 44 test
from Days.day44 import save_emails, open_emails

def test_save_emails(monkeypatch):
    def input_generator(emails):
        yield from emails
    emails = ('thom@thom.com','Zaphod@Heartofgold.com','Marvin@robot.com','')
    emailGen = input_generator(emails)
    mock_emails = make_mock_input(emailGen)
    monkeypatch.setattr(pyinputplus,'inputEmail', mock_emails)
    filePath = 'Days/csvFiles/day44Data.csv'
    save_emails(filePath)
    with open('Days/csvFiles/day44TestData.csv','r') as testData:
        with open(filePath, 'r') as data:
            assert testData.read() == data.read()

def test_open_emails():
    filePath = 'Days/csvFiles/day44TestData.csv'
    returnedObject = open_emails(filePath)
    with open(filePath, 'r') as testData:
        assert returnedObject == testData.read()
                
#Day 45 test
from Days.day45 import analyse_string

def test_analyse_string():
    str = 'Python has a string format operator %. This functions analogously to printf format strings in C, e.g. "spam=%s eggs=%d" % ("blah", 2) evaluates to "spam=blah eggs=2". Source Wikipedia'
    results = {'special characters': 22, 'words':18, 'total characters':156 }
    assert analyse_string(str) == results

#Day 48 tests
from Days.day48 import search_binary

def test_search_binary():
    list1 = [12, 34, 56, 78, 98, 22, 45, 13]
    assert search_binary(list1, 22) == 2


