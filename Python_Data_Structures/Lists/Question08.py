"""
8. Write a Python program to find the list of words that are longer than n from a
given list of words.
"""
# Solved by Zeeshan Sarwar


sample_list = ['abcde', 'xyz123', 'aba234', '12214354', 'qes', 'port', 'word', 'temp123']

try:
    print(f"The sample list is : {sample_list}")
    word_count = int(input("Please provide the minimum word count : "))
    filtered_list = [i for i in sample_list if len(i) > word_count]
    print(f"The filtered list is : {filtered_list}")

except ValueError:
    print("Please provide numeric value")


