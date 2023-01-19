#       Day 29: Middle Figure
# Write a function called middle_figure that takes two 
# parameters a, and b. The two parameters are strings. The 
# function joins the two strings and finds the middle element. 
# If the combined string has a middle element, the function should 
# return the element, otherwise, return ‘no middle figure’. Use
# ‘make love’ as an argument for a and ‘not wars’ as an 
# argument for b. Your function should return ‘e’ as the middle 
# element. Whitespaces should be removed

def middle_figure(str1, str2):
    wordList = str1.split(' ') + str2.split(' ')
    wordList = ''.join(wordList)
    middleIndex = round(len(wordList)/2) - 1
    if middleIndex <= 0:
        return 'no middle figure' 
    return wordList[middleIndex]

print(middle_figure('a','bc'))