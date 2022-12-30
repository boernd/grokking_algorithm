def my_max(alist: list) -> int:
    max_nr = alist[0]
    if len(alist) == 1:
        return max_nr
    else:
        return (
            max_nr
            if max_nr > my_max(alist[1 : len(alist)])
            else my_max(alist[1 : len(alist)])
        )


my_list = [0, 3, 5, 8, 1, 90, 0]
print(my_max(my_list))
