def my_count(alist: list) -> int:
    if len(alist) == 0:
        return 0
    else:
        return 1 + my_count(alist[1 : len(alist)])


my_list = [0, 3, 5, 8, 1, 90, 0]
print(my_count(my_list))
