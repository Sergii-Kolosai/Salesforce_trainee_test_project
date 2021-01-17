from is_fibonacci import is_fibonacci
"""Function to reverse list"""

def reverse_fib(list1):
    if type(list1) not in [list]:
        raise TypeError("Type must be list only")
    list2 = []
    for i in range(len(list1)):
        if is_fibonacci(i + 1):
            list2.append(list1[i][::-1])
    return list2