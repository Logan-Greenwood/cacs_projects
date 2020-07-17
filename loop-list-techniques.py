# removing evens from start of list
def delete_starting_evens(lst):
    while len(lst) > 0 and lst[0] % 2 == 0:
        lst = lst[1:]
    return lst



#print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
#print(delete_starting_evens([4, 8, 10]))

# returning numbers in a list with odd indices
def odd_indices(lst):
    new_lst = lst[1::2]
    return new_lst

#print(odd_indices([4, 3, 7, 10, 11, -2]))


# return largest number in list without max()
def max_num(nums):
    max = nums[0]
    for i in nums:
        if i > max:
            max = i
    return max


#print(max_num([50, -10, 0, 75, 20]))



# how to return certain indices
def same_values(lst1, lst2):
    return [index for index in range(len(lst1)) if lst2[index] == lst1[index]]


print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))



# two ways of checking lists back to front and front to back
def reversed_list(lst1, lst2):
    #return lst1[0:] == lst2[::-1]
    for index in range(len(lst1)):
        if lst1[index] != lst2[len(lst2) - 1 - index]:
            return False
    else:
        return True


print(reversed_list([1, 5, 3], [3, 2, 1]))
print(reversed_list([1, 2, 3], [3, 2, 1]))
