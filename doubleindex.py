#Write your function here
def double_index(lst, index):
    try:
        newlst = lst[:index]
        doubled = lst[index] * 2
        newlst.append(doubled)
        newlst += lst[index + 1:]
        return newlst
    except IndexError:
        return lst

#Uncomment the line below when your function is done
print(double_index([3, 8, -10, 12], 2))