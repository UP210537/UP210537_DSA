my_list = [8, 10, 6, 2, 4]    #list to sort
swapped = True                #mIt's a little fake, we need it to enter the while.

while swapped:
    swapped = False    # no swaps so far
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True   # a swap occurred.
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
my_list.sort()
my_list.reverse()
print(my_list)