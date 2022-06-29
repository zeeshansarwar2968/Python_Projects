"""
16. Write a Python program to split a list based on first character of word.
"""

sample_list = ['About', 'Absolutely', 'After', 'Aint', 'Alabama', 'AlabamaBill', 'All', 'Also', 'Amos', 'And',
               'Anyhow', 'Are', 'As', 'At', 'Aunt', 'Aw', 'Bedlam', 'Behind', 'Besides', 'Biblical', 'Bill',
               'Billgone']


dict_temp = {}
for word in sample_list:
    f = word[0]
    if f in dict_temp.keys():
        dict_temp[f].append(word)
    else:
        dict_temp[f] = [word]



print(dict_temp)






