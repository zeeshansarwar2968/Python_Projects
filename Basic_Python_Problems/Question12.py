"""
12. Write a python program to call an external command in Python.
"""
"""
solved by : Zeeshan Sarwar
"""

import subprocess

"""
The subprocess module is the recommended method of invoking and executing external commands in Python.
It provides a flexible way of suppressing the input and output of various external/shell commands and, once invoked,
it triggers new processes and then obtains their return codes.
The call() function of the subprocess module is used to start an external process, waits until the command completes, 
and then provides a return code.
"""

return_code_call = subprocess.call(['ipconfig', 'localhost'])
print(f"Observed output of call() subprocess method : {return_code_call}")


"""
The run() function is more flexible than the call() function and instead of returning a return code, 
it returns a CompletedProcess object once the code completes its execution.
"""

return_code_run = subprocess.run(['ping', 'localhost'])
print(f"Observed output of run() subprocess method : {return_code_run}")
