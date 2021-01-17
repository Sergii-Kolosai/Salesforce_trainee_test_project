from reverse_fib import reverse_fib
from read_file import read_file
from write_output import write_output

st1 = read_file('source.txt')
"""Read from the file and write the contents of the file to the variable st1"""
st2 = reverse_fib(st1)
"""Check for compliance of each line with the Fibonacci sequence and do reverse"""
write_output(st2, 'output.txt')
"""Write the result to a file"""