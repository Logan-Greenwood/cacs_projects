# two ways of checking lists back to front and front to back
def reversed_list(lst1, lst2):
    #return lst1[0:] == lst2[::-1]
    for index in range(len(lst1)):
        if lst1[index] != lst2[len(lst2) - 1 - index]:
            return False
    else:
        return True




#Uncomment the lines below when your function is done
print(reversed_list([1, 5, 3], [3, 2, 1]))
print(reversed_list([1, 2, 3], [3, 2, 1]))
