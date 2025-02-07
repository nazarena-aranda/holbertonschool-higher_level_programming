

>>> my_list = MyList([1, 4, 2, 3, 5])
>>> my_list.print_sorted()
[1, 2, 3, 4, 5]

>>> my_list = MyList([1, 2, 3])
>>> my_list.append(4)
>>> my_list
[1, 2, 3, 4]

>>> my_list = MyList([5, -1, -4, -2])
>>> my_list.print_sorted()
[-4, -2, -1, 5]

>>> my_list = MyList()
>>> my_list.print_sorted()
[]

>>> my_list = MyList([500, 300, 200, 100])
>>> my_list.print_sorted()
[100, 200, 300, 500]

>>> my_list = MyList([100, 200, 320, 300])
>>> my_list.print_sorted()
[100, 200, 300, 320]

>>> my_list
[100, 200, 320, 300]