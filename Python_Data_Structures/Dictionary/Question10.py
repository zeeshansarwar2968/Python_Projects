"""
10. Write a Python program to count the values associated with key in a
dictionary.
Sample data: = [{'id': 1, 'success': True, 'name': 'Lary'}, {'id': 2, 'success':
False, 'name': 'Rabi'}, {'id': 3, 'success': True, 'name': 'Alex'}]
Expected result: Count of how many dictionaries have success as True
"""
# Solved by Zeeshan Sarwar

sample_list = [{'id': 1, 'success': True, 'name': 'Lary'},
               {'id': 2, 'success':False, 'name': 'Rabi'},
               {'id': 3, 'success': True, 'name': 'Alex'}]

output_list = ['true' for i in sample_list if i['success'] is True]
print(f"Count of dictionaries that have success as True : {len(output_list)}")
