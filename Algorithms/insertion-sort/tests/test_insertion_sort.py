from insertion_sort.insertion_sort import insertion_sort

def test_simple_lst():
    lst = [8,4,23,42,16,15]
    insertion_sort(lst)
    assert lst == [4, 8, 15, 16, 23, 42]

def test_list_reverse_order():
    lst = [42, 23, 16, 15, 8, 4]
    insertion_sort(lst)
    assert lst == [4, 8, 15, 16, 23, 42]



def test_list_zeros_and_negative():
    lst = [-23, -0.5, -4, 0, -1]
    insertion_sort(lst)
    assert lst == [-23, -4, -1, -0.5, 0]

