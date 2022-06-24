# Sum of three Integer adds to ZERO
# a. Desc -> A program with cubic running time. Read in N integers and counts the
# number of triples that sum to exactly 0.
# b. I/P -> N number of integer, and N integer input array
# c. Logic -> Find distinct triples (i, j, k) such that a[i] + a[j] + a[k] = 0
# d. O/P -> One Output is number of distinct triplets as well as the second output is to
# print the distinct triplets.

# function to find the triplet value and return it on invocation

def find_triplets(n, arr):
    """
    Function to calculate sum of three integers that add to zero
    :param n: number of integers
    :param arr: N integer input array
    :return: the three elements if their sum is zero
    """
    found = False
    for i in range(0, n - 2):  # Looping in to the array elements till (n-2) element for the 'i' th element
        for j in range(i + 1, n - 1):  # Looping in to the array from the (i+1)th elements position till  penultimate
            # element
            for k in range(j + 1, n):  # Taking the jth elements position till the last elements position
                if (arr[i] + arr[j] + arr[k]) == 0:  # Checking the sum of ith jth and kth  to be Zero
                    found = True
                    return arr[i], arr[j], arr[k]  # Returning the elements If a+b+c = 0
    if not found:
        return "Does not exist "


user_input = input("Please provide the number of integers : ")
try:
    N = int(user_input)
    arr1 = list()
    print("Please input the elements : ")
    for num in range(N):
        arr1.append(int(input("element : ")))
    print(find_triplets(N, arr1))
except TypeError:
    print("Please provide proper numeric values")

