"""Function to write to file"""

def write_output (list1, way):
    if type(list1) not in [list]:
        raise TypeError("Type var1 must be list only")
    if type(way) not in [str]:
        raise TypeError("Type var2 must be str only")
    with open(way, mode='w+') as file_w:
        for i in range(len(list1)):
            file_w.write(list1[i])