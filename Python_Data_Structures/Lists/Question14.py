"""
14. Write a python program to check whether two lists are circularly identical.
"""

def check_logic(list1,list2):
    """
    Return true if two lists are circularly identical
    :param list1: first list
    :param list2: second list
    :return: boolean
    """
    list1.sort()
    list2.sort()
    return list1 == list2


list_1 = [10, 10, 0, 0, 10]
list_2 = [10, 10, 10, 1, 0]
print(f"List 01 : {list_1} \nList 02 : {list_2}")

print(f"Are the two lists circularly identical? : {check_logic(list_1, list_2)}")


# method 2


def circularly(list1, list2):
    return ''.join(map(str, list2)) in ''.join(map(str, list1 * 2))


print("Are identical" if circularly(list_1, list_2) else "Not Identical")
