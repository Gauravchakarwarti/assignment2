#Write a Python program to get a list, sorted in increasing order by the last element in
#each tuple from a given list of non-empty tuples


#Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

#Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]

# solution:

tuple_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
def get_last_element(t):
    return t[-1]
sorted_list = sorted(tuple_list, key=get_last_element)
print(sorted_list)
