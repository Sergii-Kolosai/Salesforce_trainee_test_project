"""Function to read from file"""

def read_file (file):
    if type(file) not in [str]:
        raise TypeError("Type must be string only")
    with open(file) as file_r:
        st = file_r.readlines()
    return st