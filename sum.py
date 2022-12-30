def my_sum(alist: list) -> int:
    if len(alist) == 0:
        return 0
    else:
        return alist[0] + my_sum(alist[1 : len(alist)])


my_list = [0, 3, 5, 8, 1, 90, 0]
print(my_sum(my_list))
