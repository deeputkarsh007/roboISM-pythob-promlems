def order(*tp):
    if tp[0]=="asc":
        tp[1].sort()

    elif tp[0]=="desc":
        tp[1].sort()
        tp[1].reverse()

    elif tp[0] == "none":
        return user_list


input_string = input('Enter elements of a list separated by space ')
print("\n")
user_list = input_string.split()

print('list before operation: ', user_list)
work = input('asc/desc/none\t')
order(work,user_list)
print(user_list)
