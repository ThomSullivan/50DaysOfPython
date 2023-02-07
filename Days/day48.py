#       Day 48: Binary Search
# Write a function called search_binary that searches for the 
# number 22 in the following list and returns its index. The 
# function should take two parameters, the list and the item that 
# is being searched for. Use binary search (iterative Method).
list1 = [12, 34, 56, 78, 98, 22, 45, 13]

def search_binary(list, x):
    list.sort()
    low = 0
    high = len(list) - 1
    mid = 0

    while low <= high:
        mid = (high + low) // 2
        if list[mid] < x:
            low = mid + 1
        elif list[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1

print(search_binary(list1,22))