"""
17. Write a program to get execution time for a Python method.
"""
"""
solved by : Zeeshan Sarwar
"""

import time

start_time = time.time()  # The time() function of a time module is used to get the time in seconds since epoch
process_strt = time.process_time()
sum_i = 0
for i in range(100000000):
    sum_i += i

time.sleep(5)
print(f"The sum of first 100000000 numbers : {sum_i}")

end_time = time.time()
process_stp = time.process_time()

elapsed_t = end_time - start_time
elapsed_t_process = process_stp - process_strt
print(f"Wall Execution Time : {elapsed_t}seconds")
print(f"CPU Process Execution Time : {elapsed_t_process}seconds")